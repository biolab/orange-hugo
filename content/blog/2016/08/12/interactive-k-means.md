+++
author="PRIMOZGODEC"
date= '2016-08-12 12:45:36+00:00'
draft= false
title="Interactive k-Means"
type="blog"
categories=["addons" ,"clustering" ,"education" ,"gsoc" ,"gsoc2016" ,"orange3" ,"widget"  ]
+++

_This is a guest blog from the Google Summer of Code project._



As a part of my [Google Summer of Code](https://summerofcode.withgoogle.com/) project I started developing educational widgets and assemble them in an [Educational Add-On](http://orange3-educational.readthedocs.io/) for [Orange](http://orange.biolab.si). Educational widgets can be used by students to understand how some key data mining algorithms work and by teachers to demonstrate the working of these algorithms.

Here I describe an educational widget for interactive [_k_-means clustering](https://en.wikipedia.org/wiki/K-means_clustering), an algorithm that splits the data into clusters by finding cluster centroids such that the distance between data points and their corresponding centroid is minimized. Number of clusters in _k_-means algorithm is denoted with _k_ and has to be specified manually.

The algorithm starts by randomly positioning the centroids in the data space, and then improving their position by repetition of the following two steps:



1. Assign each point to the closest centroid.
2. Move centroids to the mean position of points assigned to the centroid.

The widget needs the data that can come from [File](http://orange3.readthedocs.io/en/latest/widgets/data/file.html) widget, and outputs the information on clusters (Annotated Data) and centroids:


![](/images/2016/08/kmans_shema.png)


Educational widget for k-means works finds clusters based on two continuous features only, all other features are ignored. The screenshot shows plot of an Iris data set and clustering with _k_=3. That is partially cheating, because we know that iris data set has three classes, so that we can check if clusters correspond well to original classes:

![](/images/2016/08/kmeans2-stamped.png)

1. Select two features that are used in _k_-means
2. Set number of centroids
3. Randomize positions of centroids
4. Show lines between centroids and corresponding points
5. Perform the algorithm step by step. Reassign membership connects points to nearest centroid, Recompute centroids moves centroids.
6. Step back in the algorithm
7. Set speed of automatic stepping
8. Perform the whole algorithm as fast preview
9.  Anytime we can change number of centroids with spinner or with click in desired position in the graph.

If we want to see the correspondence of clusters that are denoted by _k_-means and classes, we can open _Data Table_ widget where we see that all _Iris-setosas_ are clustered in one cluster and but there are just few _Iris-versicolor_ that are classified is same cluster together with _Iris-virginica_ and vice versa.


![](/images/2016/08/kmeans3-4.png)


Interactive k-means works great in combination with [Paint Data](http://orange3.readthedocs.io/en/latest/widgets/data/paintdata.html). There, we can design data sets where k-mains fails, and observe why.

![](/images/2016/08/kmeans-failt.png)

We could also design data sets where k-means fails under specific initialization of centroids. Ah, I did not tell you that you can freely move the centroids and then restart the algorithm. Below we show the case of centroid initialization and how this leads to non-optimal clustering.


![](/images/2016/08/kmeans-f-join.png)
