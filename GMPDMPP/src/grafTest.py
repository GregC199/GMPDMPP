import pandas as pd
#matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame()

df['x'] = random.sample(range(1, 100), 25)
df['y'] = random.sample(range(1, 100), 25)

df.head()

fig, ax = plt.subplots()

sns.kdeplot(df['x'],df['y'], n_levels=3, shade="True", ax=ax).set_title('Mapa prawdopodobieństwa metodą pól potencjałów')

sns.kdeplot(df['x'],df['y'], n_levels=3, ax=ax)

sns.regplot(x=df['x'],y=df['y'],fit_reg=False, ax=ax)


plt.show()