+++
author="AJDA"
date= '2016-11-25 14:55:39+00:00'
draft= false
title="Celebrity Lookalike or How to Make Students Love Machine Learning"
type="blog"
categories=["education" ,"images" ,"interactive data visualization" ,"orange3" ]
tags=["demo" ,"education" ,"embeddings" ,"imagenet" ,"neighbors" ]

+++

Recently we've been participating at [Days of Computer Science](http://www.tms.si/index.php?e_id=484&lang=2), organized by the Museum of Post and Telecommunications and the Faculty of Computer and Information Science, University of Ljubljana, Slovenia. The project brought together pupils and students from around the country and hopefully showed them what computer science is mostly about. Most children would think programming is just typing lines of code. But it's more than that. It's a way of thinking, a way to solve problems creatively and efficiently. And even better, computer science can be used for solving a great variety of problems.


**Related:** [On teaching data science with Orange](http://orange.biolab.si/features/education-in-data-science/)


Orange team has prepared a small demo project called _Celebrity Lookalike_. We found 65 celebrity photos online and loaded them in [Orange](http://orange.biolab.si/). Next we cropped photos to faces and turned them black and white, to avoid bias in background and color. Next we inferred embeddings with [ImageNet](http://image-net.org/) widget and got 2048 features, which are the penultimate result of the ImageNet neural network.

[![](/images/2016/11/black-and-white.png)
](http://blog.biolab.si/wp-content/uploads/2016/11/black-and-white.png) We find faces in photos and turn them to black and white. This eliminates the effect of the background and distinct colors for embeddings.



Still, we needed a reference photo to find the celebrity lookalike for. Students could take a selfie and similarly extracted black and white face out of it. Embeddings were computed and sent to Neighbors widget. Neighbors finds n closest neighbors based on the defined distance measure to the provided reference. We decided to output 10 closest neighbors by cosine distance.

[![](/images/2016/11/workflow111.png)
](http://blog.biolab.si/wp-content/uploads/2016/11/workflow111.png) Celebrity Lookalike workflow. We load photos, find faces and compute embeddings. We do the same for our Webcam Capture. Then we find 10 closest neighbors and observe the results in Lookalike widget.



Finally, we used Lookalike widget to display the result. Students found it hilarious when curly boys were the Queen of England and girls with glasses Steve Jobs. They were actively trying to discover how the algorithm works by taking photo of a statue, person with or without glasses, with hats on or by making a funny face.

![](/images/2016/11/lookalike6181683.jpg)


Hopefully this inspires a new generation of students to become scientists, researchers and to actively find solutions to their problems. Coding or not. :)

[![](/images/2016/11/DSC_4982.jpg)
](http://blog.biolab.si/wp-content/uploads/2016/11/DSC_4982.jpg)

_Note: __Most widgets we have designed for this projects (like Face Detector, Webcam Capture, and Lookalike) are available in [Orange3-Prototypes](https://github.com/biolab/orange3-prototypes) and are not actively maintained. They can, however, be used for personal projects and sheer fun. Orange does not own the copyright of the images._
