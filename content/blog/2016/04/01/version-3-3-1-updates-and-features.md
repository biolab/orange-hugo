+++
author="AJDA"
date= '2016-04-01 12:43:53+00:00'
draft= false
title="Version 3.3.1 - Updates and Features"
type="blog"
blog=["distribution" ,"orange3" ,"release" ,"version" ]

+++

About a week ago we issued an updated stable release of Orange, version 3.3.1. We've introduced some new functionalities and improved a few old ones.

Here's what's new in this release:


* New widgets: Distance Matrix for visualizing distance measures in a matrix, Distance Transformation for normalization and inversion of distance matrix, Save Distance Matrix and Distance File for saving and loading distances. Last week we also mentioned a really amazing [Silhouette Plot](/blog/2016/03/23/all-i-see-is-silhouette/), which helps you visually assess cluster quality.

	![](/images/2016/04/blog11.png)


* Orange can now read **datetime** variables in its Time Variable format.

	![](/images/2016/04/blog12.png)


* Rank outputs **scores** for each scoring method.

	![](/images/2016/04/blog13.png)



* **Report** function had been added to Linear Regression, Univariate Regression, Stochastic Gradient Descent and Distance Transformation widgets.

	![](/images/2016/04/blog14.png)


* **FCBF** algorithm has been added to Rank for feature scoring and ReliefF now supports missing target values.

* Graphs in Classification Tree Viewer can be saved in **.dot** format.



You can view the entire [changelog](https://github.com/biolab/orange3/blob/master/CHANGELOG.md) here. :) Enjoy the improvements!
