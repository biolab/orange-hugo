+++
author="AJDA"
date= '2015-08-14 12:31:57+00:00'
draft= false
title="Classifying instances with Orange in Python"
type="blog"
categories=["classification" ,"data" ,"examples" ,"orange3" ,"python" ,"tree" ]
tags=["classification" ,"example" ,"python" ,"Tree Learner" ]

+++

Last week we showed you how to create your own data table in Python shell. Now we’re going to take you a step further and show you how to easily **classify data** with Orange.

First we’re going to create a [new data table](http://blog.biolab.si/2015/08/07/creating-a-new-data-table-in-orange-through-python/) with 10 fruits as our instances.

    
    <code><span style="font-weight: 400;">import Orange
    from Orange.data import *</span>
    
    <span style="font-weight: 400;">color = DiscreteVariable("color", values=["orange", "green", "yellow"])</span>
    <span style="font-weight: 400;">calories = ContinuousVariable("calories")</span>
    <span style="font-weight: 400;">fiber = ContinuousVariable("fiber")</span>
    <span style="font-weight: 400;">fruit = DiscreteVariable("fruit", values=["orange", "apple", "peach"])</span>
    
    <span style="font-weight: 400;">domain = Domain([color, calories, fiber], class_vars=fruit)</span>
    
    <span style="font-weight: 400;">data=Table(domain, [</span>
    <span style="font-weight: 400;">["green", 4, 1.2, "apple"], </span>
    <span style="font-weight: 400;">["orange", 5, 1.1, "orange"],</span>
    <span style="font-weight: 400;">["yellow", 4, 1.0, "peach"],</span>
    <span style="font-weight: 400;">["orange", 4, 1.1, "orange"],</span>
    <span style="font-weight: 400;">["yellow", 4, 1.1,"peach"],</span>
    <span style="font-weight: 400;">["green", 5, 1.3, "apple"],</span>
    <span style="font-weight: 400;">["green", 4, 1.3, "apple"],</span>
    <span style="font-weight: 400;">["orange", 5, 1.0, "orange"],</span>
    <span style="font-weight: 400;">["yellow", 4.5, 1.3, "peach"],</span>
    <span style="font-weight: 400;">["green", 5, 1.0, "orange"]])</span>
    
    <span style="font-weight: 400;">print(data)</span></code>


Now we have to select a model for classification. Among the many learners in Orange library, we decided to use the **Tree Learner** for this example. Since we’re dealing with fruits, we thought it’s only appropriate. :)

Let’s create a learning algorithm and use it to induce the classifier from the data.

    
    <code><span style="font-weight: 400;">tree_learner = Orange.classification.TreeLearner()</span>
    <span style="font-weight: 400;">tree = tree_learner(data)</span></code>


Now we can predict what variety **a green fruit** with **3.5 calories** and **2g of fiber** is with the help of our model. To do this, simply call the model and use a list of new data as argument.

    
    <code><span style="font-weight: 400;">print(tree(["green", 3.5, 2]))</span></code>


Python returns index as a result:

    
    <code><span style="font-weight: 400;">1</span></code>


To check the index, we can call **class variable** values with the corresponding index:

    
    <code><span style="font-weight: 400;">domain.class_var.values[1]</span></code>


Final result:

    
    <code><span style="font-weight: 400;">"apple"
    </span></code>


You can use your own data set to see how this model works for different data types. Let us know how it goes! :)
