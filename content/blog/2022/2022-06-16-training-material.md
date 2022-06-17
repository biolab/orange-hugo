+++
author = "Blaž Zupan"
date = "2022-06-16"
draft = false
title = "Ideas and Notes for Teachers"
type = "blog"
thumbImage = "/blog_img/2022/2022-06-16-randomized-data.png"
frontPageImage = "/blog_img/2022/2022-06-16-randomized-data.png"
blog = ["education"]
shortExcerpt = "We are crafting free educational material to help in data science training."
longExcerpt = "We are crafting free educational material to help in data science training."
x2images = true  # true if using retina screenshots, else false
+++

On May 26, 2002, we had our first [webinar targeting teaching with Orange](https://orangedatamining.com/blog/2022/2022-04-26-edu-webinar/). During the first part of the webinar, I demonstrated how we could use Orange to introduce classification trees. On their own, classification trees are quite lousy classifiers. They are, nevertheless, important as we can assemble them into very powerful classifiers. The lessons I have presented deal with overfitting and the idea that we should never report classification accuracy on the training data. The trick we use when teaching this is to show the trainees that classification trees also perform well on data with random, that is, useless labels (see the figure below). And then, of course, we ask the audience what went wrong and why and how we should fix the workflow. 

{{< window-screenshot src="/blog_img/2022/2022-05-26-ouverfitting-trees.png" >}}

I presented this and several other lessons this week during [the tutorial at Artificial Intelligence in Medicine conference](https://orangedatamining.com/blog/2022/2022-04-26-amia-tutorial/). This year [AIME](http://aime22.aimedicine.info) took place in Halifax, and I am writing this blog on a plane to Brussels, where I will attend a kick-off meeting of an ARISA, a European project to devise certified lessons and training of AI for the EU industry. Training in AI is becoming a hot topic. :). Back to Halifax. I packed the presentation with a short showcase of lectures we usually use in training. The tutorial started at 14.00 with an introduction, and a complete showcase on image analytics, whereas the lessons I have presented included those from the following list. I am here showing the timing to appreciate what can one cover with Orange in a concise time:

* [15.00] Orange mechanics: data exploration on human development index data
* [15.10] Hierarchical clustering: data on grades in english and math
* [15.25] Cluster explanation: data on student grades, discussion on choosing the number of clusters
* [15.40] Clustering and geo maps: back to human development data, showcase of widgets in geo add-on
* [15.50] Outliers and inliers: silhouette score
* [15.55] K-means clustering on painted data
* [16.00] Introduction to classification tree: on Iris dataset, manual tree construction with widget that displays distributions
* [16.10] Overfitting: with classification trees on iris with randomized classes, accuracy estimate through random sampling, cross-validation
* [16.20] Regression: overfitting in training with polynomial expansion, introduction to regularization
* [16.30] Data projections: PCA, MDS and t-SNE on zoo dataset
* [16.40] single cell analytics, data projections
* [16.50] Image analytics, outlier detection, example with images of traffic signs
* [16.55] Gene expression analysis: dataset with single-cell gene expression analysis, classification, utility of gene markers, cell type discovery, discovery of new markers

During AIME, I also pointed out that the minimum time for training on different topics from above takes hours, not minutes. For example, here are some estimates of how long would a typical training block with Orange take:

* Data Exploration and Clustering: 3 hours
* Classification, evaluation of accuracy: 5 hours
* Regression, evaluation of accuracy: 5 hours
* Image analytics, including image clustering, classification, and regression: 3 hours
* Text Mining: 5 hours
* Gene expression analysis: 3 hours

During both events, the webinar and AIME tutorial, we presented the material that teachers, professors, and instructors can use in training. The material includes:

* [Lecture notes, material in LaTeX](https://github.com/biolab/orange-lecture-notes), see also [blog with examples of rendered notes]()
* [YouTube videos](http://youtube.com/orangedatamining)
* our publications in training with Orange on [outliers](https://journals.plos.org/ploscompbiol/article/authors?id=10.1371/journal.pcbi.1008671), [gene expression analysis](https://academic.oup.com/bioinformatics/article/35/14/i4/5529249), and [image analytics](https://www.nature.com/articles/s41467-019-12397-x)

You are most welcome to review and use the above material. We also welcome any suggestions and comments. Let us know about your ideas in the [support channel on Discord](https://discord.gg/FWrfeXV).