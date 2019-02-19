+++
author="BIOLAB"
date= '2012-02-05 20:30:00+00:00'
draft= false
title="Random decisions behind your back"
type="blog"
categories=["tree" ]
tags=["decisiontree" ,"relieff" ,"tree" ]

+++

When Orange builds a decision tree, candidate attributes are evaluated and the best candidate is chosen. But what if two or more share the first place? Most machine learning systems don't care about it and always take the first, which is unfair and, besides, has strange effects: the induced model and, consequentially, its accuracy depends upon the order of attributes. Which shouldn't be.

This is not an isolated problem. Another instance is when a classifier has to choose between two equally probable classes when there is no additional information (such as classification costs) to help make the prediction. Or selecting random reference examples when computing ReliefF. Returning a modus of a distribution with two or more competing values...

The old solution was to make a random selection in such cases. Take a random class (out of the most probable, of course), random attribute, random examples... Although theoretically correct, it comes with a price: the only way to ensure repeatability of experiments is by setting the global random generator, which is not a good practice in component-based systems.

What Orange does now is more cunning. When, for instance, choosing between n equally probable classes, Orange computes something like a hash value from the example to be classified. Its remainder at division by n is then used to select the class. Thus, the class will be random, but always the same for same example.

A similar trick is used elsewhere. To choose an attribute when building a tree, it simply divides the number of learning examples at that node by the number of candidate attributes and the remainder is used again.

When more random numbers are needed, for instance for selecting m random reference examples for computing ReliefF, the number of examples is used for a random seed for a temporary random generator.

To conclude: Orange will sometimes make decisions that will look random. The reason for this is that it is more fair than most of machine learning systems that pick the first (or the last) candidate. But whatever decision is taken, it will be the same if you run the program twice. The message is thus: be aware that this is happenning, but don't care about it.
