+++
author="AJDA"
date= '2015-08-07 13:57:49+00:00'
draft= false
title="Creating a new data table in Orange through Python"
type="blog"
categories=["data" ,"examples" ,"python" ]
+++

**IMPORT DATA**



One of the first tasks in Orange data analysis is of course loading your data. If you are using Orange through Python, this is as easy as riding a bike:

    
    import Orange
    data = Orange.data.Table(“iris”)
    print (data)


This will return a neat data table of the famous Iris data set in the console.



**CREATE YOUR OWN DATA TABLE**



What if you want to create your own data table from scratch? Even this is surprisingly simple. First, import the Orange data library.

    
    from Orange.data import *




Set all the attributes you wish to see in your data table. For discrete attributes call **DiscreteVariable** and set the name and the possible values, while for a continuous variable call **ContinuousVariable** and set only the attribute name.

    
    color = DiscreteVariable(“color”, values=[“orange”, “green”, “yellow”])
    
    calories = ContinuousVariable(“calories”)
    
    fiber = ContinuousVariable(“fiber”)]
    
    fruit = DiscreteVariable("fruit”, values=[”orange", “apple”, “peach”])




Then set the domain for your data table. See how we set class variable with **class_vars**?

    
    domain = Domain([color, calories, fiber], class_vars=fruit)




Time to input your data!

    
    data = Table(domain, [
    
    [“green”, 4, 1.2, “apple”],
    
    ["orange", 5, 1.1, "orange"],
    
    ["yellow", 4, 1.0, "peach"]])




And now print what you have created!

    
    print(data)




One final step:

    
    Table.save(table, "fruit.tab")




Your data is safely stored to your computer (in the Python folder)! Good job!
