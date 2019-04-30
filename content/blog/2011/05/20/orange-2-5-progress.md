+++
author="MARKO"
date= '2011-05-20 15:08:00+00:00'
draft= false
title="Orange 2.5 progress"
type="blog"
categories=["orange25" ]
tags=["orange25" ]

+++

We decided that we should reorganize Orange to provide more intuitive interface to the scripting interface. The next release, Orange 2.5 is getting better every day. But fear not, dear reader, we are working hard to ensure that your scripts will still work.

In the last morning of the camp in Bohinj we decided to use **undercase_separated** names instead of **CamelCase**. We have been steadily converting them and the [deprecation utilities](/doc/orange25/Orange.misc.html#deprecation-utility-functions) by Aleš help a lot. We just list the name changes for class attributes or arguments and their renaming is handled gracefully; they also remain accessible with the old names. Therefore, the code does not need to be duplicated to ensure backwards compatibility.

A simple example from the documentation of bagging and boosting. The old version first:



    import orange, orngEnsemble, orngTree
    import orngTest, orngStat

    tree = orngTree.TreeLearner(mForPruning=2, name="tree")
    bs = orngEnsemble.BoostedLearner(tree, name="boosted tree")
    bg = orngEnsemble.BaggedLearner(tree, name="bagged tree")

    data = orange.ExampleTable("lymphography.tab")

    learners = [tree, bs, bg]
    results = orngTest.crossValidation(learners, data, folds=3)
    print "Classification Accuracy:"
    for i in range(len(learners)):
        print ("%15s: %5.3f") % (learners[i].name, orngStat.CA(results)[i])




Orange 2.5 version:




    
    import Orange

    tree = Orange.classification.tree.TreeLearner(m_pruning=2, name="tree")
    bs = Orange.ensemble.boosting.BoostedLearner(tree, name="boosted tree")
    bg = Orange.ensemble.bagging.BaggedLearner(tree, name="bagged tree")

    table = Orange.data.Table("lymphography.tab")

    learners = [tree, bs, bg]
    results = Orange.evaluation.testing.cross_validation(learners, table, folds=3)
    print "Classification Accuracy:"
    for i in range(len(learners)):
        print ("%15s: %5.3f") % (learners[i].name, Orange.evaluation.scoring.CA(results)[i])





In new Orange we only need to import a single module, **Orange**, the root of the new hierarchy.
