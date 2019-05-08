+++
author="AJDA"
date= '2018-05-15 09:15:58+00:00'
draft= false
title="'Python Script: Managing Data on the Fly'"
type="blog"
categories=["orange3" ,"python" ,"scripting" ]
+++

Python Script is this mysterious widget most people don't know how to use, even those versed in Python. Python Script is the widget that supplements Orange functionalities with (almost) everything that Python can offer. And it's time we unveil some of its functionalities with a simple example.


### Example: Batch Transform the Data


There might be a time when you need to apply a function to all your attributes. Say you wish to log-transform their values, as it is common in gene expression data. In theory, you could do this with Feature Constructor, where you would log-transform every attribute individually. Sounds laborious? It's because it is. Why else we have computers if not to reduce manual labor for certain tasks? Let's do it the fast way - with Python Script.

First, open File widget and load _geo-gds360.tab_ from _Browse documentation data sets_. This data set has 9485 features, so imagine having to transform each feature individually.

![](/images/2018/05/Screen-Shot-2018-05-11-at-12.18.56.png)


Instead, we will connect Python Script to File and use a simple script to apply the same transformation to all attributes.

    
    <code>import numpy as np
    from Orange.data import Table
    
    new_X = np.log(in_data.X)
    out_data = Table(in_data.domain, new_X, in_data.Y, in_data.metas)
    </code>


This is really simple. Use in_data.X, which accesses all features in the data set, to transform the data with np.log (or any other numpy function). Set out_data to new_X and, voila, the transformed data is on the output. In a few lines we have instantly handled all 9485 features.

![](/images/2018/05/Screen-Shot-2018-05-11-at-13.32.25.png)

You can inspect the data before and after transformation in a Data Table widget.

![](/images/2018/05/Screen-Shot-2018-05-11-at-13.33.28.png)

Original data.

![](/images/2018/05/Screen-Shot-2018-05-11-at-13.33.38.png)

Log-transformed data.



This is it. Now we can do our standard analysis on the transformed data. Even better! We can save our script and use it in Python Script widget any time we want.

![](/images/2018/05/Screen-Shot-2018-05-15-at-10.13.26.png)

For your convenience I have already added the [download id="2083"], so you can download and use it instantly!

Have a more interesting example with Python Script? We'd love to hear about it!
