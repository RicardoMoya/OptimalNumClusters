# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Constant
DATASET1 = "./dataSet/DS_3Clusters_999Points.txt"
DATASET2 = "./dataSet/DS2_3Clusters_999Points.txt"
DATASET3 = "./dataSet/DS_5Clusters_10000Points.txt"
DATASET4 = "./dataSet/DS_7Clusters_100000Points.txt"
LOOPS = 20
MAX_ITERATIONS = 10
INITIALIZE_CLUSTERS = 'k-means++'
CONVERGENCE_TOLERANCE = 0.001
NUM_THREADS = 8


def dataSet2ListPoints(dirDataSet):
    '''
    Read a txt file with a set of points and return a list of objects Point
    '''
    points = list()
    with open(dirDataSet, 'rt') as reader:
        for point in reader:
            points.append(np.asarray(map(float, point.split("::"))))
    return points


def plotResults(inertials):
    x, y = zip(*[inertia for inertia in inertials])
    plt.plot(x, y, 'ro-', markersize=8, lw=2)
    plt.grid(True)
    plt.xlabel('Num Clusters')
    plt.ylabel('Inertia')
    plt.show()



def SelectClusters(dataSet, loops, maxIterations, initCluster, tolerance,
                   numThreads):
    # Read data set
    points = dataSet2ListPoints(dataSet)

    inertiaClusters = list()

    for i in range(1, loops + 1, 1):
        # Object KMeans
        kmeans = KMeans(n_clusters=i, max_iter=maxIterations,
                        init=initCluster, tol=tolerance, n_jobs=numThreads)

        # Calculate Kmeans
        kmeans.fit(points)

        # Obtain inertia
        inertiaClusters.append([i, kmeans.inertia_])

    plotResults(inertiaClusters)




if __name__ == '__main__':
    SelectClusters(DATASET1, LOOPS, MAX_ITERATIONS, INITIALIZE_CLUSTERS,
                   CONVERGENCE_TOLERANCE, NUM_THREADS)
