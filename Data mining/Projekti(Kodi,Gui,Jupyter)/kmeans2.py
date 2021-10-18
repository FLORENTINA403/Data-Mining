import pandas as pd # working with data
import numpy as np # working with arrays
import matplotlib.pyplot as plt # visualization
import seaborn as sb # visualization
from mpl_toolkits.mplot3d import Axes3D # 3d plot
from termcolor import colored as cl # text customization

from sklearn.preprocessing import StandardScaler # data normalization
from sklearn.cluster import KMeans # K-means algorithm

plt.rcParams['figure.figsize'] = (20, 10)
sb.set_style('whitegrid')
df=pd.read_csv('shpenzimet_tot4.csv', encoding='ISO-8859-1')
del df["Drejtoria"]
del df["Kategoria_Ekonomike"]
df['Viti']=df['Viti'].astype(int)
df['Shuma'] = df['Shuma'].astype(int)

X = df.values
X = np.nan_to_num(X)

sc = StandardScaler()

cluster_data = sc.fit_transform(X)
print(cl('Cluster data samples : ', attrs = ['bold']), cluster_data[:5])

# MODELING

clusters = 3
model = KMeans(init = 'k-means++', 
               n_clusters = clusters, 
               n_init = 12)
model.fit(X)

labels = model.labels_
print(cl(labels[:100], attrs = ['bold']))
df['cluster_num'] = labels
df.head()
df.groupby('cluster_num').mean()





sb.scatterplot(df['Viti'].astype(str), df['Shuma'].astype(int), 
               data = df, 
               s = 380, 
               alpha = 0.8, 
               hue = 'cluster_num', 
               palette = 'spring', 
               edgecolor = 'darkgrey')
plt.title('Shpenzimet nder Vite', 
          fontsize = 18)
plt.xlabel('Viti', 
           fontsize = 16)
plt.ylabel('SHpenzimet', 
           fontsize = 16)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.legend(loc = 'upper left', fontsize = 14)

plt.show()





fig = plt.figure(1)
plt.clf()
ax = Axes3D(fig, 
            rect = [0, 0, .95, 1], 
            elev = 48, 
            azim = 134)

plt.cla()
ax.scatter(df['tremujori'], df['Viti'], df['Shuma'], 
           c = df['cluster_num'], 
           s = 200, 
           cmap = 'spring', 
           alpha = 0.5, 
           edgecolor = 'darkgrey')
ax.set_xlabel('tremujori', 
              fontsize = 16)
ax.set_ylabel('Viti', 
              fontsize = 16)
ax.set_zlabel('Shuma', 
              fontsize = 16)

plt.show()












