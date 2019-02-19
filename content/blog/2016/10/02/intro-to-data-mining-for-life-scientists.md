+++
author="BLAZ"
date= '2016-10-02 11:21:20+00:00'
draft= false
title="Intro to Data Mining for Life Scientists"
type="blog"
categories=["bioinformatics" ,"bioorange" ,"education" ,"orange3" ,"tutorial" ,"workshop"  ]
tags=["bioinformatics" ,"datamining" ,"education" ,"workshop" ]

+++

[RNA Club Munich](http://www.helmholtz-muenchen.de/rna-club/index.html) has organized [Molecular Life of Stem Cells Conference](https://www.stemcells2016.org) in Ljubljana this past Thursday, Friday and Saturday. They asked us to organize a [four-hour workshop on data mining](https://www.stemcells2016.org/program/workshops/2-introduction-to-data-mining/index.html). And here we were: four of us, Ajda, Anze, Marko and myself (Blaz) run a workshop for 25 students with molecular biology and biochemistry background.

![](/images/2016/10/IMG_20160929_133840.jpg)

We have covered some basic data visualization, modeling (classification) and model scoring, hierarchical clustering and data projection, and finished with a touch of deep-learning by diving into image analysis by deep learning-based embedding.


**Related:** [Data Mining Course at Baylor College of Medicine in Houston](/blog/2016/09/15/data-mining-in-houston-2/)


It’s not easy to pack so many new things on data analytics within four hours, but working with [Orange](http://orange.biolab.si) helps. This was a hands-on workshop. Students brought their own laptops with Orange and several of its add-ons for bioinformatics and image analytics. We also showed how to prepare one’s own data using [Google Forms](https://www.google.com/forms/about/) and designed a questionary, augment it in a class, run it with students and then analyze the questionary with Orange.

![](/images/2016/10/PANO_20160929_113352.jpg)

![](/images/2016/10/IMG_0355.jpg)

![](/images/2016/10/IMG_0353.jpg)

The hard part of any short course that includes machine learning is how to explain overfitting. The concept is not trivial for data science newcomers, but it is so important it simply cannot be left out. Luckily, Orange has some cool widgets to help us understanding the overfitting. Below is a workflow we have used. We read some data (this time it was a yeast gene expression data set called brown-selected that comes with Orange), “destroyed the data” by randomly permuting the column with class values, trained a classification tree, and observed near perfect results when the model was checked on the training data.

![](/images/2016/10/yeast-overfitting-distributions.png)

Sure this works, you are probably saying. The models should have been scored on a separate test set! Exactly, and this is what we have done next with [Data Sampler](http://docs.orange.biolab.si/3/visual-programming/widgets/data/datasampler.html), which lead us to cross-validation and [Test & Score widget](http://docs.orange.biolab.si/3/visual-programming/widgets/evaluation/testlearners.html).

This was a great and interesting short course and we were happy to contribute to the success of the student-run [MLSC-2016](https://www.stemcells2016.org) conference.
