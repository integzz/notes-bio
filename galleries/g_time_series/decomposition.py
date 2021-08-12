from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd

passengers = pd.read_csv('../data/air_passengers.csv')

date = passengers['date'].astype('datetime64')
dates = pd.DatetimeIndex(data=date)

passengers.set_index(dates, inplace=True)

result = seasonal_decompose(passengers['value'], model='multiplicative')

fig, axes = plt.subplots(4,
                         1,
                         dpi=100,
                         figsize=(10, 6),
                         sharex=True,
                         constrained_layout=True)

ys = (result.observed, result.trend, result.seasonal, result.resid)
ylabels = ('Value', 'Trend', 'Seasonal', 'Residual')

for ax, y, ylabel in zip(axes.flatten(), ys, ylabels):
    ax.plot(dates, y)
    ax.set(ylabel=ylabel)

fig.suptitle('Time Series Decomposition of Air Passengers')
plt.show()
