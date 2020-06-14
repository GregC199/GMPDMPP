import pandas as pd
#matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import colorbar

df = pd.DataFrame()

df['x'] = random.sample(range(1, 100), 25)
df['y'] = random.sample(range(1, 100), 25)

df.head()

fig, ax = plt.subplots()

sns.kdeplot(df['x'],df['y'], n_levels=2, shade="True", ax=ax).set_title('Mapa prawdopodobieństwa metodą pól potencjałów')

sns.kdeplot(df['x'],df['y'], n_levels=2, ax=ax)

sns.regplot(x=df['x'],y=df['y'], fit_reg=False, ax=ax)

#plt.streamplot(df['x'],df['y'])
#streamplot - histogram przepływu

#same punkty z nakladaniem sie
sns.lmplot( x="x", y="y", data=df, fit_reg=False)

#ten z rozkladem punktow na bokach
sns.jointplot(x=df["x"], y=df["y"],n_levels=2, kind='kde')



plt.show()