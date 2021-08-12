import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

email = pd.read_csv('../data/email_campaign_funnel.csv')

group_col = 'Gender'
order_of_bars = email.Stage.unique()[::-1]

_, ax = plt.subplots(dpi=100)

colors = [
    plt.cm.Spectral(i / float(len(email[group_col].unique()) - 1))
    for i, _ in enumerate(email[group_col].unique())
]

for c, group in zip(colors, email[group_col].unique()):
    sns.barplot(x='Users',
                y='Stage',
                data=email.loc[email[group_col] == group, :],
                order=order_of_bars,
                color=c,
                label=group,
                ax=ax)

ax.set(xlabel="$Users$",
       ylabel="Stage of Purchase",
       title="Population Pyramid of the Marketing Funnel")
ax.legend('')
plt.show()
