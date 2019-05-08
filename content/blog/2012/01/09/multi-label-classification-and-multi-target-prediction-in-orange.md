+++
author="BIOLAB"
date= '2012-01-09 12:41:00+00:00'
draft= false
title="Multi-label classification (and Multi-target prediction) in Orange"
type="blog"
categories=["classification" ,"gsoc" ,"mlc" ,"multilabel" ]
+++

The last summer, student Wencan Luo participated in [Google Summer of Code](https://code.google.com/soc/) to implement [Multi-label Classification in Orange](/blog/2011/09/02/gsoc-review-multi-label-classification-implementation/). He provided a framework, implemented a few algorithms and some prototype widgets. His work has been "hidden" in our repositories for too long; finally, we have merged part of his code into Orange (widgets are not there yet ...) and added a more general support for multi-target prediction.

You can load multi-label tab-delimited data (e.g. [emotions.tab](http://orange.biolab.si/trac/intertrac/export%3Atrunk/orange/doc/datasets/emotions.tab)) just like any other [tab-delimited data](/doc/reference/Orange.data.formats/#tab-delimited-format):

    
    >>> zoo = Orange.data.Table('zoo')            # single-target
    >>> emotions = Orange.data.Table('emotions')  # multi-label



The difference is that now zoo's domain has a non-empty **class_var** field, while a list of **emotions**' labels can be obtained through it's domain's **class_vars**:

    
    >>> zoo.domain.class_var
    EnumVariable 'type'
    >>> emotions.domain.class_vars
    <EnumVariable 'amazed-suprised',
     EnumVariable 'happy-pleased',
     EnumVariable 'relaxing-calm',
     EnumVariable 'quiet-still',
     EnumVariable 'sad-lonely',
     EnumVariable 'angry-aggresive'>


A simple example of a [multi-label classification](/doc/reference/Orange.multilabel/) learner is a "binary relevance" learner. Let's try it out.

    
    >>> learner = Orange.multilabel.BinaryRelevanceLearner()
    >>> classifier = learner(emotions)
    >>> classifier(emotions[0])
    [<orange.Value 'amazed-suprised'='0'>,
     <orange.Value 'happy-pleased'='0'>,
     <orange.Value 'relaxing-calm'='1'>,
     <orange.Value 'quiet-still'='1'>,
     <orange.Value 'sad-lonely'='1'>,
     <orange.Value 'angry-aggresive'='0'>]
    >>> classifier(emotions[0], Orange.classification.Classifier.GetProbabilities)
    [<1.000, 0.000>, <0.881, 0.119>, <0.000, 1.000>,
     <0.046, 0.954>, <0.000, 1.000>, <1.000, 0.000>]



Real values of label variables of **emotions[0]** instance can be obtained by calling **emotions[0].get_classes()**, which is analogous to the **get_class** method in the single-target case.

For multi-label classification, we can also perform testing like usual, however, [specialised evaluation measures](/doc/reference/Orange.evaluation.scoring/#scoring-for-multilabel-classification) have to be used:


    
    >>> test = Orange.evaluation.testing.cross_validation([learner], emotions)
    >>> Orange.evaluation.scoring.mlc_hamming_loss(test)
    [0.2228780213603148]



In one of the following blog posts, a multi-target regression method PLS that is in the process of implementation will be described.
