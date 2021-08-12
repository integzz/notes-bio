# Gallery

|        Code        |                                              Viewer                                               |                                                 Editor                                                 |
| :----------------: | :-----------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: |
| Matplotlib-Seaborn | [view](https://nbviewer.jupyter.org/github/integzz/notes-bio/blob/master/galleries/mpl_sns.ipynb) | [edit](https://colab.research.google.com/github/integzz/notes-bio/blob/master/galleries/mpl_sns.ipynb) |
|       Pandas       | [view](https://nbviewer.jupyter.org/github/integzz/notes-bio/blob/master/galleries/pandas.ipynb)  | [edit](https://colab.research.google.com/github/integzz/notes-bio/blob/master/galleries/pandas.ipynb)  |

## 1. Technical Stacks

|                     |   Python    |       Julia        |
| :-----------------: | :---------: | :----------------: |
|  Language Version   |    v3.9     |        v1.6        |
|       Basics        | Matplotlib  |     CairoMakie     |
| Grammar of Graphics |   Seaborn   | AlgerbraOfGraphics |
|      Enhanced       |             |      WGLMakie      |
|  Machine Learning   | Yellowbrick |                    |

## 2. Code Styles

### 2.1. Basics

- prefer `enumerate()` over `range(len())`

```python
xs = range(3)

# good
for ind, x in enumerate(xs):
  print(f'{ind}: {x}')

# bad
for i in range(len(xs)):
  print(f'{i}: {xs[i]}')
```

### 2.2. Matplotlib

> including seaborn

- prefer `Axes` object over `Figure` object
- use `constrained_layout=True` when draw subplots

```python
# good
_, axes = plt.subplots(1, 2, figsize=(10, 6), constrained_layout=True)
axes[0].plot(x1, y1)
axes[1].hist(x2, y2)

# bad
plt.subplot(121)
plt.plot(x1, y1)
plt.subplot(122)
plt.hist(x2, y2)
```

- prefer `axes.flatten()` over `plt.subplot()` in cases where subplots' data is iterable
- prefer `zip()` or `enumerate()` over `range()` for iterable objects

```python
# good
_, ax = plt.subplots(2, 2, constrained_layout=True)

for ax, x, y in zip(axes.flatten(), xs, ys):
  ax.plot(x, y)

# bad
for i in range(4):
  ax = plt.subplot(2, 2, i+1)
  ax.plot(x[i], y[i])
```

- prefer `set()` method over `set_*()` method

```python
# good
ax.set(xlabel='x', ylabel='y')

# bad
ax.set_xlabel('x')
ax.set_ylabel('y')
```

- Prefer `despine()` over `ax.spines[*].set_visible()`

```python
# good
sns.despine()

# bad
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
```

### 2.3. Pandas

- prefer `df['col']` over `df.col`

```python
# good
movies['duration']

# bad
movies.duration
```

- prefer `df.query` over `df[]` or `df.loc[]` in simple-selection

```python
# good
movies.query('duration >= 200')

# bad
movies[movies['duration'] >= 200]
movies.loc[movies['duration'] >= 200, :]
```

- prefer `df.loc` and `df.iloc` over `df[]` in multiple-selection

```python
# good
movies.loc[movies['duration'] >= 200, 'genre']
movies.iloc[0:2, :]

# bad
movies[movies['duration'] >= 200].genre
movies[0:2]
```

- prefer `.astype('category')` over `.factorize()`

## 3. LaTeX Styles

### 3.1. Multiple lines

Reduce the use of `begin{array}...end{array}`

- equations: `begin{aligned}...end{aligned}`

$$
\begin{aligned}
y_1 = x^2 + 2*x \\
y_2 = x^3 + x
\end{aligned}
$$

```latex
$$
\begin{aligned}
y_1 = x^2 + 2*x \\
y_2 = x^3 + x
\end{aligned}
$$
```

- equations with conditions: `begin{cases}...end{cases}`

$$
\begin{cases}
y = x^2 + 2*x & x > 0 \\
y = x^3 + x & x ≤ 0
\end{cases}
$$

```latex
$$
\begin{cases}
y = x^2 + 2*x & x > 0 \\
y = x^3 + x & x ≤ 0
\end{cases}
$$
```

- matrix: `begin{matrix}...end{matrix}`

$$
\begin{vmatrix}
  a + a^′ & b + b^′ \\ c & d
  \end{vmatrix} = \begin{vmatrix}
  a & b \\ c & d
  \end{vmatrix} + \begin{vmatrix}
  a^′ & b^′ \\ c & d
\end{vmatrix}
$$

```latex
$$
\begin{vmatrix}
  a + a^′ & b + b^′ \\ c & d
  \end{vmatrix} = \begin{vmatrix}
  a & b \\ c & d
  \end{vmatrix} + \begin{vmatrix}
  a^′ & b^′ \\ c & d
\end{vmatrix}
$$
```

### 3.2. Brackets

- prefer `\Bigg...\Bigg` over `\left...\right`

$$
A\Bigg[\frac12\ \frac13\ ⋯\ \frac1{99}\Bigg]
$$

```latex
$$
A\Bigg[\frac12\ \frac13\ ⋯\ \frac1{99}\Bigg]
$$
```

- prefer `\underset{}{}` over `\underset{}`

$$
\underset{θ}{\rm argmax}\ p(x_i|θ)
$$

```latex
$$
\underset{θ}{\rm argmax}\ p(x_i|θ)
$$
```

### 3.3. Expressions

- prefer `^{\top}` over `^T` for transpose

$$
𝐀^⊤
$$

```latex
$$
𝐀^{\top}
$$
```

- prefer `\to` over `\rightarrow` for limit

$$
\lim_{n → ∞}
$$

```latex
$$
\lim_{n\to \infty}
$$
```

- prefer `underset{}{}` over `\limits_`

$$
\underset{w}{\rm argmin}\ (wx +b)
$$

```latex
$$
\underset{w}{\rm argmin}\ (wx +b)
$$
```

### 3.4. Fonts

- prefer `{rm }` over `\mathop{}` or `\operatorname{}`

$$
θ_{\rm MLE} = \underset{θ}{\rm argmax}\ ∑_{i = 1}^{N}\log p(x_i|θ)
$$

```latex
$$
θ_{\rm MLE} = \underset{θ}{\rm argmax}\ ∑_{i = 1}^{N}\log p(x_i|θ)
$$
```

- prefer `{\bf }` over `\mathbf{}`
- prefer `{\it }` over `\mathit{}`

$\frac12$
