+++
author = "Blaž Zupan"
date = "2021-03-05"
draft = false
title = "Hands-On Training About Overfitting"
type = "blog"
thumbImage = "/blog_img/2021/2021-01-11-orange-in-education-small.png"
frontPageImage = "/blog_img/2021/2021-03-05-overfitting-tree-small.png"
blog = ["education", "teaching", "machine learning"]
shortExcerpt = "We have designed a course on overfitting."
longExcerpt = "PLOS Computation Biology has just published our paper on training about overfitting."
x2images = false  # true if using retina screenshots, else false
+++

[PLOS Computation Biology](https://journals.plos.org/ploscompbiol/) has just published our paper on training about overfitting:

* Demšar J, Zupan B (2021) [Hands-on training about overfitting](https://doi.org/10.1371/journal.pcbi.1008671). PLoS Comput Biol 17(3): e1008671. 

Machine learning has recently propelled approaches for the analysis of data, but "for the uninitiated, the technology poses significant difficulties" (Deep learning for biology, Nature, Feb 22, 2018). One of the hard concepts for starters in machine learning is overfitting. Overfitting can lead to models that include patterns that do not generalize well and could be meaningless. It is thus vital to include teaching about overfitting in any data science course.

{{% workflow-screenshot src="/blog_img/2021/2021-03-05-overfitting-tree.png" %}}

For years, we have been developing Orange, a data science platform. Since we are also educators, we have designed Orange to support the teaching of concepts in machine learning. In the paper, we lay out a short course that uses Orange to teach about overfitting. The specific advantage of our proposed course is that it is entirely hands-on, can be carried out in few hours, does not require any prerequisites or much background knowledge, and is suitable for students of biomedicine or molecular biology that do not necessarily know how to code. The course layout we are proposing is practical; students learn by analyzing the data, making mistakes in the analysis that lead to overfitting, and correcting these by adjusting the workflows.

In the past several years, we have been giving and perfecting the lecture we are reporting in the paper. The lecture is carried out yearly at the University of Ljubljana, Slovenia, and at Baylor College of Medicine in Houston. The lecture was also included in over 50 short hands-on courses on machine learning we have been giving around the world. Our paper reports on the course structure, pedagogical principles we use in teaching, and a walk through the course that educators can use for teaching material and ideas within their lessons.

Our other manuscripts, where we report on Orange as a tool for education in data science, include

* Stražar M, Žagar L, Kokošar J, Tanko V, Erjavec A, Poličar P, Starič A, Demšar J, Shaulsky G, Menon V, Lamire A, Parikh A, and Zupan B (2019) [scOrange – A Tool for Hands-On Training of Concepts from Single Cell Data Analytics](https://doi.org/10.1093/bioinformatics/btz348), Bioinformatics 35(14):i4-i12.
* Godec P, Pančur M, Ilenič N, Čopar A, Stražar M, Erjavec A, Pretnar A, Demšar J, Starič A, Toplak M, Žagar L, Hartman J, Wang H, Bellazzi R, Petrovič U, Garagna S, Zuccotti M, Park D, Shaulsky G, Zupan B (2019) [Democratized image analytics by visual programming through integration of deep models and small-scale machine learning](https://www.nature.com/articles/s41467-019-12397-x), Nature Communications 10(1):4551.
