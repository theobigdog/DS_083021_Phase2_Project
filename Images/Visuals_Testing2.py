import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import Seaborn_Color_Palettes as col
import pandas as pd

df = pd.read_csv('../Data/kc_house_data.csv')
# print(df.head())

x = df['price']

fig, ax = plt.subplots(figsize=(20,15))
fig.suptitle('Kings County Home Sale Prices:', fontsize=30, fontweight='bold')
sns.histplot(x, ax=ax, bins=50, color="gold", log_scale=True, element='poly')
plt.xlabel('Price ($)', fontsize=24, fontweight='bold')
plt.xticks(fontsize=18)
plt.ticklabel_format(style='sci', axis=1, scilimits=(0,0))
plt.ylabel('Count (homes sold)', fontsize=24)
plt.yticks(fontsize=18)
ax2 = ax.twinx()
sns.kdeplot(x, ax=ax2, color="darkblue")
plt.title('2014-2015 (Log-Scale)', fontsize=24, fontweight='bold')
plt.yticks(fontsize=18)
plt.ylabel('Density', fontsize=24)
plt.savefig('Home_Sale_Prices')

plt.show()