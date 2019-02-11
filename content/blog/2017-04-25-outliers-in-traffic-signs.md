+++
author="BLAZ"
date= '2017-04-25 07:35:38+00:00'
draft= false
title="Outliers in Traffic Signs"
type="blog"
categories=["addons" ,"analysis" ,"images" ,"interactive data visualization" ,"orange3"  ,"visualization" ]
tags=["image analytics" ,"image embedding" ,"silhouette" ,"silhouette plot" ]

+++

Say I am given a collection of images of traffic signs, and would like to find which signs stick out. That is, which traffic signs look substantially different from the others. I would assume that the traffic signs are not equally important and that some were designed to be noted before the others.

I have assembled a small set of regulatory and warning traffic signs and stored the references to their images in a [traffic-signs-w.tab](http://file.biolab.si/datasets/traffic-signs-rw.tab) data set.


**Related:** [Viewing images](/blog/2014-04-29-viewing-images/)




**Related:** [Video on image clustering](https://www.youtube.com/watch?v=Iu8g2Twjn9U)




**Related:** [Video on image classification](https://www.youtube.com/watch?v=lvgx62a8XQk)


The easiest way to display the images is by loading this data file with File widget and then passing the data to the Image Viewer,

![](/images/2017/04/traffic-signs-file-image-viewer.png)

Opening the Image Viewer allows me to see the images:

![](/images/2017/04/Screen-Shot-2017-04-25-at-09.59.16.png)

Note that initially the data table we have loaded contains no valuable features on which we can do any machine learning. It includes just a category of traffic sign, its name, and the link to its image.

![](/images/2017/04/traffic-signs-data-table2.png)


We will use deep-network embedding to turn these images into numbers to describe them with 2048 real-valued features. Then, we will use Silhouette Plot to find which traffic signs are outliers in their own group. We would like to select these and visualize them in the Image Viewer.


**Related:** [All I see is silhouette](/blog/2016-03-23-all-i-see-is-silhouette/)


Our final workflow, with selection of three biggest outliers (we used shift-click to select its corresponding silhouettes in the Silhouette Plot), is:

![](/images/2017-04-Screen-Shot-2017-04-25-at-10.08.56.png)

Isn't this great? Turns out that traffic signs were carefully designed, such that the three outliers are indeed the signs we should never miss. It is great that we can now reconfirm this design choice by deep learning-based embedding and by using some straightforward machine learning tricks such as Silhouette Plot.
