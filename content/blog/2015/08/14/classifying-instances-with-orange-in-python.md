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

First we’re going to create a [new data table](/blog/2015/08/07/creating-a-new-data-table-in-orange-through-python/) with 10 fruits as our instances.

    
    import Orange
    from Orange.data import *
    
    color = DiscreteVariable("color", values=["orange", "green", "yellow"])calories = ContinuousVariable("calories")
    fiber = ContinuousVariable("fiber")
    fruit = DiscreteVariable("fruit", values=["orange", "apple", "peach"])
    
    domain = Domain([color, calories, fiber], class_vars=fruit)
    
    data=Table(domain, [</span>
    ["green", 4, 1.2, "apple"], 
    ["orange", 5, 1.1, "orange"],
    ["yellow", 4, 1.0, "peach"],
    ["orange", 4, 1.1, "orange"],
    ["yellow", 4, 1.1,"peach"],
    ["green", 5, 1.3, "apple"],
    ["green", 4, 1.3, "apple"],
    ["orange", 5, 1.0, "orange"],
    ["yellow", 4.5, 1.3, "peach"],
    ["green", 5, 1.0, "orange"]])
    
    print(data)


Now we have to select a model for classification. Among the many learners in Orange library, we decided to use the **Tree Learner** for this example. Since we’re dealing with fruits, we thought it’s only appropriate. :)

Let’s create a learning algorithm and use it to induce the classifier from the data.

    
    tree_learner = Orange.classification.TreeLearner()
    tree = tree_learner(data)


Now we can predict what variety **a green fruit** with **3.5 calories** and **2g of fiber** is with the help of our model. To do this, simply call the model and use a list of new data as argument.

    
    print(tree(["green", 3.5, 2]))


Python returns index as a result:

    
    1


To check the index, we can call **class variable** values with the corresponding index:

    
    domain.class_var.values[1]


Final result:

    
    "apple"


You can use your own data set to see how this model works for different data types. Let us know how it goes! :)
