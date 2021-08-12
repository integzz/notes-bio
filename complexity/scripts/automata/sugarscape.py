import cell2d


class Agent:
    def __init__(self, loc, params):
        self.loc = tuple(loc)
        self.age = 0

        # extract the parameters
        max_vision = params.get('max_vision', 6)
        max_metabolism = params.get('max_metabolism', 4)
        min_lifespan = params.get('min_lifespan', 10000)
        max_lifespan = params.get('max_lifespan', 10000)
        min_sugar = params.get('min_sugar', 5)
        max_sugar = params.get('max_sugar', 25)

        # choose attributes
        self.vision = np.random.randint(1, max_vision + 1)
        self.metabolism = np.random.uniform(1, max_metabolism)
        self.lifespan = np.random.uniform(min_lifespan, max_lifespan)
        self.sugar = np.random.uniform(min_sugar, max_sugar)

    def step(self, scape):
        self.loc = scape.look_and_move(self.loc, self.vision)
        self.sugar += scape.harvest(self.loc) - self.metabolism
        self.age += 1

    def is_starving(self):
        return self.sugar < 0

    def is_old(self):
        return self.age > self.lifespan


class Sugarscape(cell2d.Cell2D):
    def __init__(self, n_rows, **params):
        self.n = n_rows
        self.params = params

        # track variables
        self.agent_count_seq = []

        # make the capacity array
        self.capacity = self.make_capacity()

        # initially all cells are at capacity
        self.array = self.capacity.copy()

        # make the agents
        self.make_agents()

    def make_capacity(self):
        # compute the distance of each cell from the peaks.
        dist1 = compute_distances_from(self.n, 15, 15)
        dist2 = compute_distances_from(self.n, 35, 35)
        dist = np.minimum(dist1, dist2)

        # cells in the capacity array are set according to dist from peak
        bins = [21, 16, 11, 6]
        a = np.digitize(dist, bins)
        return a

    def make_agents(self):
        # determine where the agents start and generate locations
        n, m = self.params.get('starting_box', self.array.shape)
        locs = make_locs(n, m)
        np.random.shuffle(locs)

        # make the agents
        num_agents = self.params.get('num_agents', 400)
        assert (num_agents <= len(locs))
        self.agents = [Agent(locs[i], self.params) for i in range(num_agents)]

        # keep track of which cells are occupied
        self.occupied = set(agent.loc for agent in self.agents)

    def grow(self):
        grow_rate = self.params.get('grow_rate', 1)
        self.array = np.minimum(self.array + grow_rate, self.capacity)

    def look_and_move(self, center, vision):
        # find all visible cells
        locs = make_visible_locs(vision)
        locs = (locs + center) % self.n

        # convert rows of the array to tuples
        locs = [tuple(loc) for loc in locs]

        # select unoccupied cells
        empty_locs = [loc for loc in locs if loc not in self.occupied]

        # if all visible cells are occupied, stay put
        if len(empty_locs) == 0:
            return center

        # look up the sugar level in each cell
        t = [self.array[loc] for loc in empty_locs]

        # find the best one and return it
        # (in case of tie, argmax returns the first, which
        # is the closest)
        i = np.argmax(t)
        return empty_locs[i]

    def harvest(self, loc):
        sugar = self.array[loc]
        self.array[loc] = 0
        return sugar

    def step(self):
        replace = self.params.get('replace', False)

        # loop through the agents in random order
        random_order = np.random.permutation(self.agents)
        for agent in random_order:

            # mark the current cell unoccupied
            self.occupied.remove(agent.loc)

            # execute one step
            agent.step(self)

            # if the agent is dead, remove from the list
            if agent.is_starving() or agent.is_old():
                self.agents.remove(agent)
                if replace:
                    self.add_agent()
            else:
                # otherwise mark its cell occupied
                self.occupied.add(agent.loc)

        # update the time series
        self.agent_count_seq.append(len(self.agents))

        # grow back some sugar
        self.grow()
        return len(self.agents)

    def add_agent(self):
        new_agent = Agent(self.random_loc(), self.params)
        self.agents.append(new_agent)
        self.occupied.add(new_agent.loc)
        return new_agent

    def random_loc(self):
        while True:
            loc = tuple(np.random.randint(self.n, size=2))
            if loc not in self.occupied:
                return loc

    def draw(self):
        draw_array_2d(self.array, cmap='YlOrRd', vmax=9, origin='lower')

        # draw the agents
        xs, ys = self.get_coords()
        self.points = ax.plot(xs, ys, '.', color='red')[0]

    def get_coords(self):
        agents = self.agents
        rows, cols = np.transpose([agent.loc for agent in agents])
        xs = cols + 0.5
        ys = rows + 0.5
        return xs, ys

    def plot_num_agents(self):
        ax.plot(self.agent_count_seq)
        ax.set(xlabel='Time steps')
        ax.set(ylabel='Number of Agents')

    def plot_avg_metabolism(self):
        ax.plot(self.avg_metabolism_seq)
        ax.set(xlabel='Time steps')
        ax.set(ylabel='Average metabolism')

    def plot_avg_vision(self):
        ax.plot(self.avg_vision_seq)
        ax.set(xlabel='Time steps')
        ax.set(ylabel='Average vision')


class EvoSugarscape(Sugarscape):
    def __init__(self, n_rows, **params):
        Sugarscape.__init__(self, n_rows, **params)

        # track variables
        self.avg_vision_seq = []
        self.avg_metabolism_seq = []

    def step(self):
        Sugarscape.step(self)

        # average vision
        avg_vision = np.mean([agent.vision for agent in self.agents])
        self.avg_vision_seq.append(avg_vision)

        # average metabolism
        avg_metabolism = np.mean([agent.metabolism for agent in self.agents])
        self.avg_metabolism_seq.append(avg_metabolism)

        # add an agent
        add_agents = self.params.get('add_agents', False)
        if add_agents:
            self.add_agent()

        return len(self.agents)
