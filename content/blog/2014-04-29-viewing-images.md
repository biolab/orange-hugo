+++
author="BIOLAB"
date= '2014-04-29 21:28:00+00:00'
draft= false
title="Viewing Images"
type="blog"
categories=["clustering" ,"images" ,"visualization" ]
tags=["clustering" ,"images" ,"visualization" ]

+++

I am lately having fun with Image Viewer. The widget has been recently updated and can display images stored locally or on the internet. But wait, what images? How on earth can Orange now display images if it can handle mere tabular or basket-based data?

Here's an example. I have considered a subset of animals from the [download id="864"] data set (comes with Orange installation), and for demonstration purposes selected only a handful of attributes. I have added a new string attribute ("images") and declared that this is a meta attribute of the type "image". The values of this attribute are links to images on the web:

[![](/images/2014/04/29/animals-dataset_1.png__610x213_q95_crop_upscale.png)
](http://blog.biolab.si/wp-content/uploads/2014/04/29/animals-dataset_1.png)

Here is the resulting data set, [download id="859"]. I have used this data set in a schema with hierarchical clustering, where upon selection of the part of the clustering tree I can display the associated images:

[![](/images/2014/04/29/animals-schema.png__610x428_q95_crop_upscale.png)
](http://blog.biolab.si/wp-content/uploads/2014/04/29/animals-schema.png)

Typically and just like above, you would use a string meta attribute to store the link to images. Images can be referred to using a HTTP address, or, if stored locally, using a relative path from the data file location to the image files.

Here is another example, where all the images were local and we have associated them with a famous [digits data set](https://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits) ([download id="868"] is a data set in the Orange format with the image files). The task for this data set is to classify handwritten digits based on their bitmap representation. In the schema below we wanted to find out which are the most frequent errors some classification algorithm would make, and how do the images of the misclassified digits look like. Turns out that SVM with RBF kernel most often misclassify the digit 9 and confuses it with a digit 3:

[![](/images/2014/04/29/digits-schema.png__610x495_q95_crop_upscale.png)
](http://blog.biolab.si/wp-content/uploads/2014/04/29/digits-schema.png)
