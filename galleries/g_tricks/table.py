import numpy as np
import matplotlib.pyplot as plt

_, ax = plt.subplots(figsize=(10, 6), dpi=100)

x = np.random.rand(5, 8) * .7

ax.plot(x.mean(axis=0), '-o', label='average per column')
ax.set(xticks=[])
ax.table(cellText=[[f'{xxx}%1.2f' for xxx in xx] for xx in x],
         cellColours=plt.cm.GnBu(x),
         fontsize='large',
         loc='bottom')
plt.show()
