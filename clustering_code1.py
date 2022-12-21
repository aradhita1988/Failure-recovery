# -*- coding: utf-8 -*-
"""Clustering code1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fi-NOHaYs9FEEuu6-aLc7P_XVtYPgAxT
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from scipy.spatial.distance import squareform
import sklearn.metrics as sm
import scipy.cluster.hierarchy as shc 
import matplotlib.pyplot as plt
import networkx as nx
from sklearn.cluster import SpectralClustering
from scipy.cluster.hierarchy import dendrogram
import tensorflow as tf
import os
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from collections import defaultdict

data=pd.read_csv('sai.csv')
data

mydata=np.asarray(data)

print(len(mydata))
def add_edge(adj, src, dest): 
    adj[src].append(dest);
    adj[dest].append(src);

maxValues = data.max()
 
v=maxValues+1

adj = [[] for i in range(v)];
for i in range(len(mydata)):
  j=0
  r=mydata[i][j]
  c=mydata[i][j+1]
  add_edge(adj,r,c)
adj

def BFS(adj, src, dest, v, pred, dist):
 
    # a queue to maintain queue of vertices whose
    # adjacency list is to be scanned as per normal
    # DFS algorithm
    queue = []
  
    # boolean array visited[] which stores the
    # information whether ith vertex is reached
    # at least once in the Breadth first search
    visited = [False for i in range(v)];
  
    # initially all vertices are unvisited
    # so v[i] for all i is false
    # and as no path is yet constructed
    # dist[i] for all i set to infinity
    for i in range(v):
 
        dist[i] = 1000000
        pred[i] = -1;
     
    # now source is first to be visited and
    # distance from source to itself should be 0
    visited[src] = True;
    dist[src] = 0;
    queue.append(src);
  
    # standard BFS algorithm
    while (len(queue) != 0):
        u = queue[0];
        queue.pop(0);
        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.append(adj[u][i]);
  
                # We stop BFS when we find
                # destination.
                if (adj[u][i] == dest):
                    return True;
  
    return False;
  
# utility function to print the shortest distance
# between source vertex and destination vertex
def printShortestDistance(adj, s, dest, v):
     
    # predecessor[i] array stores predecessor of
    # i and distance array stores distance of i
    # from s
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)];
    
    if (BFS(adj, s, dest, v, pred, dist) == False):
        print("Given source and destination are not connected")
  
    # vector path stores the shortest path
    path = []
    crawl = dest;
    crawl = dest;
    path.append(crawl);
     
    while (pred[crawl] != -1):
        path.append(pred[crawl]);
        crawl = pred[crawl];
     
       
    # distance from source is in distance array
    #print(dist[dest]), end = '')
    return(dist[dest])
  
    # printing path from source to destination
    #print("\nPath is : : ")
     
   # for i in range(len(path)-1, -1, -1):
       # print(path[i], end=' ')

dist=np.zeros((v,v),dtype='int8')
for i in range(v):
  for j in range(v):
    p=printShortestDistance(adj, i, j, v)
    dist[i][j]=p
pd.DataFrame(dist)

k=[]
#silhouette_scores_single = []
#silhouette_scores_complete = []
silhouette_scores_average = []
for i in range(2,10):
    k.append(i)
   # ac_single = AgglomerativeClustering(n_clusters = i, affinity='precomputed', linkage='single')
    #ac_complete = AgglomerativeClustering(n_clusters = i, affinity='precomputed', linkage='complete')
    ac_average = AgglomerativeClustering(n_clusters = i, affinity='precomputed', linkage='average')
    #silhouette_scores_single.append(silhouette_score(dist, ac_single.fit_predict(dist))) 
    #silhouette_scores_complete.append(silhouette_score(dist, ac_complete.fit_predict(dist))) 
    silhouette_scores_average.append(silhouette_score(dist, ac_average.fit_predict(dist)))

# Plotting a bar graph to compare the results 
plt.bar(k, silhouette_scores_average)
plt.xlabel('Number of clusters', fontsize = 10) 
plt.ylabel('Silhouette score', fontsize = 10) 
#plt.show() 

from google.colab import files
plt.savefig('sisynth.eps',dpi=1200,format= 'eps')
files.download('sisynth.eps')

k=[]
ch_scores = []
for i in range(2,11):
    k.append(i)
    ac = AgglomerativeClustering(n_clusters=i, affinity='precomputed', linkage='average')
    ch_scores.append(sm.calinski_harabasz_score(dist, ac.fit_predict(dist)))

plt.plot(k, ch_scores) 
plt.xlabel('Number of clusters', fontsize = 10) 
plt.ylabel('Calinski Harabasz score', fontsize = 10) 
#plt.show() 

# Plotting a bar graph to compare the results 
from google.colab import files
plt.savefig('chsynth.eps',dpi=1200,format= 'eps')
files.download('chsynth.eps')

cluster = AgglomerativeClustering(n_clusters=9, affinity='precomputed', linkage='average')

lab=cluster.fit_predict(dist)
lab  
lab1 = pd.DataFrame(lab)
lab1
lab1.to_csv('file1.csv',sep=',')