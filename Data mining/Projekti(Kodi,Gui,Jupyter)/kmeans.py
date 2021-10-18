import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as snsco
from sklearn.cluster import KMeans

df=pd.read_csv('shpenzimet_tot4.csv')
df.columns = [col.strip() for col in list(df.columns)]
df['Shuma'] = df['Shuma'].astype(int)

   #Python Clastering
    #si ndodhen elementet para clusterimit
plt.figure(figsize=(10,6))
plt.scatter(df['Shuma'],df['tremujori'])
plt.xlabel('Shpenzimet')
plt.ylabel('tremujori')
plt.title('Shpenzimet ne kuader te viteve')
plt.show()

    ###Clusterimi
X = df.iloc[:, [4,5]].values
print(X[:5])

    #The Elbow Method
    #prcaktimi i rangut te clusterimin
clustering_score = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'random', random_state = 42)
    kmeans.fit(X)
    clustering_score.append(kmeans.inertia_)

plt.figure(figsize=(10,6))
plt.plot(range(1, 11), clustering_score)
plt.scatter(5,clustering_score[4], s = 200, c = 'red', marker='*')
plt.title('The Elbow Method')
plt.xlabel('No. of Clusters')
plt.ylabel('Clustering Score')
plt.show()

kmeans= KMeans(n_clusters = 5, random_state = 42)
kmeans.fit(X)
pred = kmeans.predict(X)
print(pred)

df['Cluster'] = pd.DataFrame(pred, columns=['cluster'] )
print('Number of data points in each cluster= \n', df['Cluster'].value_counts())

plt.figure(figsize=(14,6))
plt.scatter(X[pred == 0, 0], X[pred == 0, 1], c = 'brown', label = 'Cluster 0')
plt.scatter(X[pred == 1, 0], X[pred == 1, 1], c = 'green', label = 'Cluster 1')
plt.scatter(X[pred == 2, 0], X[pred == 2, 1], c = 'blue', label = 'Cluster 2')
plt.scatter(X[pred == 3, 0], X[pred == 3, 1], c = 'purple', label = 'Cluster 3')
plt.scatter(X[pred == 4, 0], X[pred == 4, 1], c = 'orange', label = 'Cluster 4')

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:, 1],s = 300, c = 'red', label = 'Centroid', marker='*')

plt.xlabel('Shpenzimet')
plt.ylabel('tremujori')
plt.legend()
plt.title('Shpenzimet ne kuader te viteve')

  

