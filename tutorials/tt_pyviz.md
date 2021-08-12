# Python 可视化漫谈

![pyviz](images/pyviz.png)

## 1. Matplotlib

Matplotlib 是 Python 的默认可视化库，也是 SciPy 生态的默认绘图后端。

- Matplotlib (⭐13.4k)

  - Seaborn (⭐8.3k)
  - PlotNine (⭐2.6k)
  - Yellowbrick (⭐3.1k)
  - CartoPy (⭐0.8k)
  - WordCloud (⭐8k)

- Pandas
- SciPy
  - StatsModels
  - Scikit-Learn
- NetWorkX

## 2. HoloViz

HoloViz 是 Anaconda 资助的可视化项目。形成了以 Bokeh 为中心和底层，以 HoloViews 和 Panel 为主打产品的 Python 第二大可视化生态系统。

Bokeh 可以被看作 Python 社区里默认的交互绘图后端。毕竟 Anaconda 爸爸的钱不是白给的。

- Bokeh (⭐14.9k)
- Holoviews (⭐1.8k)
  - Geoviews (⭐0.3k)
  - hvPlot (⭐0.3k)
- DataShader (⭐2.5k)
- Panel (⭐0.9k)

![holoviz](images/holoviz.png)

## 3. Plot.ly

Plot.ly 是一家位于蒙特利尔的数据可视化公司。

- Plotly (⭐9.2k)
  - Plotly_Express (⭐0.6k)
- Dash (⭐14.2k)

## 4. Altair-Viz

Altair 是 JS 可视化库 Vega-Lite 的 Python 封装。Vega-Lite 又继承于 Vega，由 Vega-Viz 团队维护，故 Altair 的改进和迭代严重依赖于上游。

- Altair (⭐6.5k)
- Streamlit (⭐14k)

## 5. 生态支持

### 5.1. 仪表盘

|            | Panel | Streamlit | Dash  |
| :--------: | ----- | :-------: | ----- |
|  Stars ⭐  | 0.9k  |    14k    | 14.2k |
| Matplotlib | ✓     |     ✓     |       |
|   Bokeh    | 默认  |     ✓     |       |
|   Altair   | ✓     |   默认    |       |
|   Plotly   | ✓     |     ✓     | 默认  |

### 5.2. 数据框

|            | Pandas 整合 |     EDA 工具     |
| :--------: | :---------: | :--------------: |
| Matplotlib |  默认后端   | Pandas-Profiling |
|   Bokeh    |      ✓      |     DataPrep     |
|   Altair   |   pdVega    |     Lux-API      |
|   Plotly   |  cufflinks  |     SweetViz     |

## 6. 其他

还有一些较为流行，但不属于上述生态的可视化库，因为没有形成生态，而且我本人没有亲自试用过（PyEcharts 除外），这里就不再评价了。

- PyEcharts (⭐10.8k)
- VisPy (⭐2.6k)
- PyGAL (⭐2.3k)
