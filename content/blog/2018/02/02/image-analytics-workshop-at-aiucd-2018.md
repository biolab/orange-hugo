+++
author="AJDA"
date= '2018-02-02 10:32:28+00:00'
draft= false
title="Image Analytics Workshop at AIUCD 2018"
type="blog"
categories=["addons" ,"analysis" ,"conference" ,"embedding" ,"images" ,"visualization"  ,"workshop" ]
+++

This week, Primož and I flew to the south of Italy to hold a workshop on [Image Analytics through Data Mining](http://www.aiucd2018.uniba.it/workshops.html) at [AIUCD 2018 conference](http://www.aiucd2018.uniba.it/index.html). The workshop was intended to familiarize digital humanities researchers with options that visual programming environments offer for image analysis.

![](/images/2018/02/IMG_20180130_172350.jpg)

In about 5 hours we discussed image embedding, clustering, finding closest neighbors and classification of images. While it is often a challenge to explain complex concepts in such a short time, it is much easier when working with Orange.


**Related:** [Image Analytics: Clustering](/blog/2017/04/03/image-analytics-clustering/)


One of the workflows we learned at the workshop was the one for finding the most similar image in a set of images. This is better explained with an example.

We had 15 paintings from different authors. Two of them were painted by [Claude Monet](https://en.wikipedia.org/wiki/Claude_Monet), a famous French impressionist painter. Our task was, given a reference image of Monet, to find his other painting in a collection.

![](/images/2018/02/Screen-Shot-2018-02-02-at-10.33.07.png)

A collection of images. It includes two Monet paintings.

First, we loaded our [data set](http://file.biolab.si/images/Paintings.zip) with Import Images. Then we sent our images to Image Embedding. We selected Painters embedder since it was specifically [trained to recognize authors of paintings](http://blog.kaggle.com/2016/11/17/painter-by-numbers-competition-1st-place-winners-interview-nejc-ilenic/).

![](/images/2018/02/Screen-Shot-2018-02-02-at-10.33.54.png)


![](/images/2018/02/Screen-Shot-2018-02-02-at-10.34.51.png)

We used Painters embedder here.

Once we have described our paintings with vectors (embeddings), we can compare them by similarity. To find the second Monet in a data set, we will have to compute the similarity of paintings and find the one most similar one to our reference painting.


**Related:** [Video on image clustering](https://www.youtube.com/watch?v=Iu8g2Twjn9U)


Let us connect Image Embedding to Neighbors from Prototypes add-on. Neighbors widget is specifically intended to find a number of closest neighbors given a reference data point.

We will need to adjust the widget a bit. First, we will need cosine distance, since we will be comparing images by the content, not the magnitude of features. Next, we will tick off _Exclude reference_, in order to receive the reference image on the output. We do this just for visualization purposes. Finally, we set the number of neighbors to 2. Again, this is just for a nicer visualization, since we know there are only two Monet's paintings in the data set.

![](/images/2018/02/Screen-Shot-2018-02-02-at-10.42.59.png)

Neighbors was set to provide a nice visualization. Hence we ticked off Exclude references and set Neighbors to 2.

Then we need to give Neighbors a reference image, for which we want to retrieve the neighbors. We do this by adding Data Table to Image Embedding, selecting one of Monet's paintings in the spreadsheet and then connecting the Data Table to Neighbors. The widget will automatically consider the second input as a reference.

![](/images/2018/02/Screen-Shot-2018-02-02-at-10.47.57.png)


![](/images/2018/02/Screen-Shot-2018-02-02-at-10.45.37.png)

Monet.jpg is our reference painting. We select it in Data Table.

Now, all we need to do is to visualize the output. Connect Image Viewer to Neighbors and open it.

![](/images/2018/02/Screen-Shot-2018-02-02-at-10.48.13.png)


Voila! The widget has indeed found the second Monet's painting. So useful when you have thousands of images in your archive!
