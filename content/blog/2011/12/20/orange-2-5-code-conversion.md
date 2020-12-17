+++
author="MARKO"
date= '2011-12-20 12:21:00+00:00'
draft= false
title="Orange 2.5: code conversion"
type="blog"
blog=["orange25" ]
+++

Orange 2.5 unifies Orange's C++ core and Python modules into a single module hierarchy. To use the new module hierarchy, import **Orange** instead of **orange** and accompanying **orng*** modules. While we will maintain backward compatibility in 2.* releases, we nevertheless suggest programmers to use the new interface. The provided [conversion tool](http://orange.biolab.si/trac/intertrac/wiki%3AOrange25/RefactoringTool) can help refactor your code to use the new interface.

The conversion script, **orange2to25.py**, resides in Orange's main directory. To refactor **accuracy8.py** from the "Orange for beginners" tutorial run**python orange2to25.py -w -o accuracy8_25.py doc/ofb-rst/code/accuracy8.py**.

The old code




    
    import orange
    import orngTest, orngStat, orngTree

    # set up the learners
    bayes = orange.BayesLearner()
    tree = orngTree.TreeLearner(mForPruning=2)
    bayes.name = "bayes"
    tree.name = "tree"
    learners = [bayes, tree]

    # compute accuracies on data
    data = orange.ExampleTable("voting")
    res = orngTest.crossValidation(learners, data, folds=10)
    cm = orngStat.computeConfusionMatrices(res,
            classIndex=data.domain.classVar.values.index('democrat'))





is refactored to




    
    import Orange

    # set up the learners
    bayes = Orange.classification.bayes.NaiveLearner()
    tree = Orange.classification.tree.TreeLearner(mForPruning=2)
    bayes.name = "bayes"
    tree.name = "tree"
    learners = [bayes, tree]

    # compute accuracies on data
    data = Orange.data.Table("voting")
    res = Orange.evaluation.testing.cross_validation(learners, data, folds=10)
    cm = Orange.evaluation.scoring.compute_confusion_matrices(res,
            classIndex=data.domain.classVar.values.index('democrat'))





Read more about [the refactoring tool on the wiki](http://orange.biolab.si/trac/intertrac/wiki%3AOrange25/RefactoringTool) and on the help page (**python orange2to25.py --help**).
