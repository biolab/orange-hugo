+++
author="MATEVZKREN"
date= '2016-08-05 11:52:39+00:00'
draft= false
title="Rule Induction (Part I - Scripting)"
type="blog"
categories=["classification" ,"gsoc2016" ,"orange3" ]
post_format=["Quote" ]
tags=["cn2" ,"gsoc" ,"predictive induction" ,"rule induction" ,"rules" ]

+++

_This is a guest blog from the Google Summer of Code project._



We’ve all heard the saying, “Rules are meant to be broken.” Regardless of how you might feel about the idea, one thing is certain. Rules must first be learnt. My 2016 [Google Summer of Code](https://summerofcode.withgoogle.com) project revolves around doing just that. I am developing classification rule induction techniques for [Orange](http://orange.biolab.si), and here describing the code currently available in the [pull request](https://github.com/biolab/orange3/pull/1397) and that will become part of official distribution in an upcoming [release 3.3.8](https://github.com/biolab/orange3/blob/master/CHANGELOG.md).

Rule induction from examples is recognised as a fundamental component of many machine learning systems. My goal was foremost to implement supervised rule induction algorithms and rule-based classification methods, but also to devise a more general framework of replaceable individual components that users could fine-tune to their needs. To this purpose, [separate-and-conquer strategy](http://dx.doi.org/10.1023/A:1006524209794) was applied. In essence, learning instances are covered and removed following a chosen rule. The process is repeated while learning set examples remain. To evaluate found hypotheses and to choose the best rule in each iteration, search heuristics are used (primarily, rule class distribution is the decisive determinant).

The use of the created module is straightforward. New rule induction algorithms can be easily introduced, by either utilising predefined components or developing new ones (these include various search algorithms, search strategies, evaluators, and others). Several well-known rule induction algorithms have already been included. Let’s see how they perform!

[Classic CN2](http://dx.doi.org/10.1023/A:1022641700528) inducer constructs a list of ordered rules (decision list). Here, we load the _titanic_ data set and create a simple classifier, which can already be used to predict data.

    
    import Orange
    data = Orange.data.Table('titanic')
    learner = Orange.classification.CN2Learner()
    classifier = learner(data)


Similarly, a set of unordered rules can be constructed using [Unordered CN2](http://dx.doi.org/10.1007/BFb0017011) inducer. Rules are learnt for each class individually, in regard to the original learning data. To evaluate found hypotheses, Laplace accuracy measure is used. Having first initialised the learner, we then control the algorithm by modifying its parameters. The underlying components are available to us by accessing the rule finder.

    
    data = Table('iris.tab')
    learner = CN2UnorderedLearner()
    
    # consider up to 10 solution streams at one time
    learner.rule_finder.search_algorithm.beam_width = 10
    
    # continuous value space is constrained to reduce computation time
    learner.rule_finder.search_strategy.bound_continuous = True
    
    # found rules must cover at least 15 examples
    learner.rule_finder.general_validator.min_covered_examples = 15
    
    # found rules must combine at most 2 selectors (conditions)
    learner.rule_finder.general_validator.max_rule_length = 2
    
    classifier = learner(data)
    


Induced rules can be quickly reviewed and interpreted. They are each of the form ‘_if_ cond _then_ predict class”. That is, a conjunction of selectors followed by the predicted class.

    
    for rule in classifier.rule_list:
    ... print(rule, rule.curr_class_dist.tolist())
    
    >>> IF petal length<=3.0 AND sepal width>=2.9 THEN iris=Iris-setosa [49, 0, 0]
    >>> IF petal length>=3.0 AND petal length<=4.8 THEN iris=Iris-versicolor [0, 46, 3]
    >>> IF petal width>=1.8 AND petal length>=4.9 THEN iris=Iris-virginica [0, 0, 43]
    >>> IF TRUE THEN iris=Iris-virginica [50, 50, 50]  # the default rule
    


If no other rules fire, default rule (majority classification) is used. Specific to each individual rule inducer, the application of the default rule varies.

Though rule learning is most frequently used in the context of predictive induction, it can be adapted to subgroup discovery. In contrast, subgroup discovery aims at learning individual patterns or interesting population subgroups, rather than to maximise classification accuracy. Induced rules prove very valuable in terms of their descriptive power. To this end, [CN2-SD](http://www.jmlr.org/papers/volume5/lavrac04a/lavrac04a.pdf) algorithms were also implemented.

Hopefully, the addition to the Orange software suite will benefit both novice and expert users looking advance their knowledge in a particular area of study, through a better understanding of given predictions and underlying argumentation.
