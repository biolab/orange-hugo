+++
author="BLAZ"
date= '2016-12-22 08:55:36+00:00'
draft= false
title="The Beauty of Random Forest"
type="blog"
categories=["classification" ,"interactive data visualization" ,"orange3" ,"regression"  ,"tree" ,"visualization" ]
tags=["classification tree" ,"Pythagoras trees" ,"pythagoreantree" ,"random forest"
  ,"regression tree" ,"visualization" ]

+++

It is the time of the year when we adore Christmas trees. But these are not the only trees we, at Orange team, think about. In fact, through almost life-long professional deformation of being a data scientist, when I think about trees I would often think about classification and regression trees. And they can be beautiful as well. Not only for their elegance in explaining the hidden patterns, but aesthetically, when rendered in Orange. And even more beautiful then a single tree is Orange's rendering of a forest, that is, a random forest.


**Related:** [Pythagorean Trees and Forests](http://blog.biolab.si/2016/07/29/pythagorean-trees-and-forests/)


Here are six trees in the random forest constructed on the [housing data set](https://archive.ics.uci.edu/ml/datasets/Housing):
[![](/images/2016/12/pythagorean-forest-housing.png)
](http://blog.biolab.si/wp-content/uploads/2016/12/pythagorean-forest-housing.png)

The random forest for [annealing data set](https://archive.ics.uci.edu/ml/datasets/Annealing) includes a set of smaller-sized trees:
[![](/images/2016/12/random-forest-anneal2.png)
](http://blog.biolab.si/wp-content/uploads/2016/12/random-forest-anneal2.png)

A Christmas-lit random forest inferred from [pen digits data set](http://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits) looks somehow messy in trying to categorize to ten different classes:
[![](/images/2016/12/pythagorean-forest-pendigits.png)
](http://blog.biolab.si/wp-content/uploads/2016/12/pythagorean-forest-pendigits.png)

The power of beauty! No wonder random forests are one of the best machine learning tools. Orange renders them according to the idea of Fabian Beck and colleagues who proposed [Pythagoras trees for visualizations of hierarchies](http://publications.fbeck.com/ivapp14-pythagoras.pdf). The actual implementation for classification and regression trees for Orange was created by [Pavlin Policar.](https://github.com/pavlin-policar)
