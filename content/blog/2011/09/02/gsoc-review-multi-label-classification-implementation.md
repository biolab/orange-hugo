+++
author="BIOLAB"
date= '2011-09-02 05:47:00+00:00'
draft= false
title="GSoC Review: Multi-label Classification Implementation"
type="blog"
categories=["classification" ,"gsoc" ,"multilabel" ]
+++

Traditional single-label classification is concerned with learning from a set of examples that are associated with a single label **l** from a set of disjoint labels **L**, **|L|** > **1**. If **|L|** = **2**, then the learning problem is called a binary classification problem, while if **|L|** > **2**, then it is called a multi-class classification problem (Tsoumakas & Katakis, 2007).

Multi-label classification methods are increasingly used by many applications, such as textual data classification, protein function classification, music categorization and semantic scene classification. However, currently, Orange can only handle single-label problems. As a result, the project _Multi-label classification Implementation_ has been proposed to extend Orange to support multi-label.

We can group the existing methods for multi-label classification into two main categories: a) problem transformation method, and b) algorithm adaptation methods. In the former one, multi-label problems are converted to single-label, and then the traditional binary classification can apply; in the latter case, methods directly classify the multi-label data, instead.

In this project, two transformation methods and two algorithm adaptation methods are implemented. Along with the methods, their widgets are also added. As the evaluation metrics for multi-label data are different from the single-label ones, new evaluation measures are supported. The code is available in [SVN branch](http://orange.biolab.si/trac/intertrac/browser%3Abranches/multilabel).

Fortunately, benefiting from the Tab file format, the **ExampleTable** can store multi-label data without any modification. Now, we can add a special value – **label** into the **attributes** dictionary of the domain with value 1. In this way, if the attribute description has the keyword **label**, then it is a label; otherwise, it is a normal feature.


### What have been done in this project




#### Transformation methods

* br – Binary Relevance Learner (Tsoumakas & Katakis, 2007)
* lp – Label Powerset Classification (Tsoumakas & Katakis, 2007)



#### Algorithm Adaptation methods


* mlknn – Multi-kNN Classification (Zhang & Zhou, 2007)
* brknn – BR-kNN Classification (Spyromitros et al. 2008)


#### Evaluation methods


* mlc_hamming_loss – Example-based Hamming Loss (Schapire and Singer 2000)
* mlc_accuracy, mlc_precision, mlc_recall – Example-based accuracy, precision, recall (Godbole & Sarawagi, 2004)



#### Widgets


* OWBR – Widget for Binary Relevance Learner
* OWLP – Widget for Label Powerset Classification
* OWMLkNN – Widget for Multi-kNN Classification
* OWBRkNN – Widget for BR-kNN Classification
* OWTestLearner – Widget for Evaluation



#### File Format Extension


* extend the loadARFF function to support sparse Weka format
* new support [mulan xml and arff format](http://mulan.sourceforge.net/format.html)



### Plan for the future


* add more classification methods for multi-label, such as PT1 to PT6
* add feature extraction method
* add ranking-based evaluation methods



### How to use


Basically, the way to use multi-label classification and evaluation is nearly the same as the single-label ones. The only difference between them is the different types of input data.


#### Example for Classification

    import Orange

    data = Orange.data.Table("emotions.tab")

    classifier = Orange.multilabel.BinaryRelevanceLearner(data)

    for e in data:
        c,p = classifier(e,Orange.classification.Classifier.GetBoth)
        print c,p

    powerset_cliassifer = Orange.multilabel.LabelPowersetLearner(data)
    for e in data:
        c,p = powerset_cliassifer(e,Orange.classification.Classifier.GetBoth)
        print c,p

    mlknn_cliassifer = Orange.multilabel.MLkNNLearner(data,k=1)
    for e in data:
        c,p = mlknn_cliassifer(e,Orange.classification.Classifier.GetBoth)
        print c,p
       
    br_cliassifer = Orange.multilabel.BRkNNLearner(data,k=1)
    for e in data:
        c,p = br_cliassifer(e,Orange.classification.Classifier.GetBoth)
        print c,p






#### Example for Evaluation



    import Orange

    learners = [
        Orange.multilabel.BinaryRelevanceLearner(name="br"),
        Orange.multilabel.BinaryRelevanceLearner(name="br", \
            base_learner=Orange.classification.knn.kNNLearner),
        Orange.multilabel.LabelPowersetLearner(name="lp"),
        Orange.multilabel.LabelPowersetLearner(name="lp", \
            base_learner=Orange.classification.knn.kNNLearner),
        Orange.multilabel.MLkNNLearner(name="mlknn",k=5),
        Orange.multilabel.BRkNNLearner(name="brknn",k=5),
    ]

    data = Orange.data.Table("emotions.xml")

    res = Orange.evaluation.testing.cross_validation(learners, data,2)
    loss = Orange.evaluation.scoring.mlc_hamming_loss(res)
    accuracy = Orange.evaluation.scoring.mlc_accuracy(res)
    precision = Orange.evaluation.scoring.mlc_precision(res)
    recall = Orange.evaluation.scoring.mlc_recall(res)
    print 'loss=', loss
    print 'accuracy=', accuracy
    print 'precision=', precision
    print 'recall=', recall






### References


* G. Tsoumakas and I. Katakis. _Multi-label classification: An overview". International Journal of Data Warehousing and Mining, 3(3):1-13, 2007._
* E. Spyromitros, G. Tsoumakas, and I. Vlahavas, _An Empirical Study of Lazy Multilabel Classification Algorithms_. Proc. 5th Hellenic Conference on Artificial Intelligence (SETN 2008), Springer, Syros, Greece, 2008.
* M. Zhang and Z. Zhou. _ML-KNN: A lazy learning approach to multi-label learning_. Pattern Recognition, 40, 7 (Jul. 2007), 2038-2048.
* S. Godbole and S. Sarawagi. _Discriminative Methods for Multi-labeled Classification_, Proceedings of the 8th Pacific-Asia Conference on Knowledge Discovery and Data Mining, PAKDD 2004.
* R. E. Schapire and Y. Singer. _Boostexter: a bossting-based system for text categorization_, Machine Learning, vol.39, no.2/3, 2000, pp:135-68.

