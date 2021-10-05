import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import Seaborn_Color_Palettes as col
import pandas as pd

X = [random.randint(1,2500) for x in range(1,25)]
Y = [random.randint(58,10000) for x in range(1,25)]
Z = [random.randint(12,20100) for x in range(1,25)]
A = [random.randint(15,3800) for x in range(1,25)]
C = [random.randint(350,40000) for x in range(1,25)]
D = [random.randint(1,22000) for x in range(1,25)]
arr = np.array([X,Y,Z,A,C,D])
column = ["apple","banana","grape","strawberry","raspberry","blueberry","blackberry","boysenberry","peach","nectarine","plum","pluot","orange","tangerine",\
    "blood-orange","pear","lettuce","cabbage","mustard","kale","chard","onion","garlic","broccoli"]
ind = ["fruit","vegetable","animal","mineral","chemical","stuff"]
df = pd.DataFrame(data=arr, index=ind, columns=column)

# plt.figure(figsize=(15,15))
# mask = np.triu(np.ones_like(df.corr(), dtype=bool))
# sns.heatmap(df.corr().abs(), annot=True, fmt=".2f", cmap='YlOrRd', mask=mask)
x=df['apple']
y=df['banana']

# sns.regplot(x=x, y=y)

sns.histplot(x)

plt.show()

