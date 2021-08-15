using CSV
using AlgebraOfGraphics
using Colors

adsdf = CSV("https://raw.githubusercontent.com/gitony0101/X4DS/main/data/Advertising.csv")

layers = linear() + visual(Scatter)

p1 = data(adsdf) * mapping(:TV, :sales, color=:red) * layers;
p2 = data(adsdf) * mapping(:radio, :sales, color=:red) * layers;
p3 = data(adsdf) * mapping(:newspaper, :sales, color=:red) * layers;

fig = Figure()

ax1 = draw!(fig[1, 1], p1)
ax2 = draw!(fig[1, 2], p2)
ax3 = draw!(fig[1, 3], p3)

fig
