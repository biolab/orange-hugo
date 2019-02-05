+++
author="BIOLAB"
date= '2011-09-02 05:47:00+00:00'
draft= false
title="'GSoC Review: Multi-label Classification Implementation'"
type="blog"
categories=["classification" ,"gsoc" ,"multilabel" ]
tags=["classification" ,"gsoc" ,"multilabel" ]

+++

Traditional single-label classification is concerned with learning from a set of examples that are associated with a single label l from a set of disjoint labels L, |L| > 1. If |L| = 2, then the learning problem is called a binary classification problem, while if |L| > 2, then it is called a multi-class classification problem (Tsoumakas & Katakis, 2007).

Multi-label classification methods are increasingly used by many applications, such as textual data classification, protein function classification, music categorization and semantic scene classification. However, currently, Orange can only handle single-label problems. As a result, the project _Multi-label classification Implementation_ has been proposed to extend Orange to support multi-label.

We can group the existing methods for multi-label classification into two main categories: a) problem transformation method, and b) algorithm adaptation methods. In the former one, multi-label problems are converted to single-label, and then the traditional binary classification can apply; in the latter case, methods directly classify the multi-label data, instead.

In this project, two transformation methods and two algorithm adaptation methods are implemented. Along with the methods, their widgets are also added. As the evaluation metrics for multi-label data are different from the single-label ones, new evaluation measures are supported. The code is available in [SVN branch](http://orange.biolab.si/trac/intertrac/browser%3Abranches/multilabel).

Fortunately, benefiting from the Tab file format, the ExampleTable can store multi-label data without any modification. Now, we can add a special value – label into the attributes dictionary of the domain with value 1. In this way, if the attribute description has the keyword label, then it is a label; otherwise, it is a normal feature.


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






    
    <span class="kn">import</span> <span class="nn">Orange</span>
    
    data <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">"emotions.tab"</span><span class="p">)</span>
    
    classifier <span class="o">=</span> Orange<span class="o">.</span>multilabel<span class="o">.</span>BinaryRelevanceLearner<span class="p">(</span>data<span class="p">)</span>
    
    <span class="k">for</span> e <span class="ow">in</span> data<span class="p">:</span>
        c<span class="p">,</span>p <span class="o">=</span> classifier<span class="p">(</span>e<span class="p">,</span>Orange<span class="o">.</span>classification<span class="o">.</span>Classifier<span class="o">.</span>GetBoth<span class="p">)</span>
        <span class="k">print</span> c<span class="p">,</span>p
    
    powerset_cliassifer <span class="o">=</span> Orange<span class="o">.</span>multilabel<span class="o">.</span>LabelPowersetLearner<span class="p">(</span>data<span class="p">)</span>
    <span class="k">for</span> e <span class="ow">in</span> data<span class="p">:</span>
        c<span class="p">,</span>p <span class="o">=</span> powerset_cliassifer<span class="p">(</span>e<span class="p">,</span>Orange<span class="o">.</span>classification<span class="o">.</span>Classifier<span class="o">.</span>GetBoth<span class="p">)</span>
        <span class="k">print</span> c<span class="p">,</span>p
    
    mlknn_cliassifer <span class="o">=</span> Orange<span class="o">.</span>multilabel<span class="o">.</span>MLkNNLearner<span class="p">(</span>data<span class="p">,</span>k<span class="o">=</span><span class="mi">1</span><span class="p">)</span>
    <span class="k">for</span> e <span class="ow">in</span> data<span class="p">:</span>
        c<span class="p">,</span>p <span class="o">=</span> mlknn_cliassifer<span class="p">(</span>e<span class="p">,</span>Orange<span class="o">.</span>classification<span class="o">.</span>Classifier<span class="o">.</span>GetBoth<span class="p">)</span>
        <span class="k">print</span> c<span class="p">,</span>p
       
    br_cliassifer <span class="o">=</span> Orange<span class="o">.</span>multilabel<span class="o">.</span>BRkNNLearner<span class="p">(</span>data<span class="p">,</span>k<span class="o">=</span><span class="mi">1</span><span class="p">)</span>
    <span class="k">for</span> e <span class="ow">in</span> data<span class="p">:</span>
        c<span class="p">,</span>p <span class="o">=</span> br_cliassifer<span class="p">(</span>e<span class="p">,</span>Orange<span class="o">.</span>classification<span class="o">.</span>Classifier<span class="o">.</span>GetBoth<span class="p">)</span>
        <span class="k">print</span> c<span class="p">,</span>p







#### Example for Evaluation






    
    <span class="kn">import</span> <span class="nn">Orange</span>
    
    learners <span class="o">=</span> <span class="p">[</span>
        Orange<span class="o">.</span>multilabel<span class="o">.</span>BinaryRelevanceLearner<span class="p">(</span>name<span class="o">=</span><span class="s">"br"</span><span class="p">),</span>
        Orange<span class="o">.</span>multilabel<span class="o">.</span>BinaryRelevanceLearner<span class="p">(</span>name<span class="o">=</span><span class="s">"br"</span><span class="p">,</span> \
            base_learner<span class="o">=</span>Orange<span class="o">.</span>classification<span class="o">.</span>knn<span class="o">.</span>kNNLearner<span class="p">),</span>
        Orange<span class="o">.</span>multilabel<span class="o">.</span>LabelPowersetLearner<span class="p">(</span>name<span class="o">=</span><span class="s">"lp"</span><span class="p">),</span>
        Orange<span class="o">.</span>multilabel<span class="o">.</span>LabelPowersetLearner<span class="p">(</span>name<span class="o">=</span><span class="s">"lp"</span><span class="p">,</span> \
            base_learner<span class="o">=</span>Orange<span class="o">.</span>classification<span class="o">.</span>knn<span class="o">.</span>kNNLearner<span class="p">),</span>
        Orange<span class="o">.</span>multilabel<span class="o">.</span>MLkNNLearner<span class="p">(</span>name<span class="o">=</span><span class="s">"mlknn"</span><span class="p">,</span>k<span class="o">=</span><span class="mi">5</span><span class="p">),</span>
        Orange<span class="o">.</span>multilabel<span class="o">.</span>BRkNNLearner<span class="p">(</span>name<span class="o">=</span><span class="s">"brknn"</span><span class="p">,</span>k<span class="o">=</span><span class="mi">5</span><span class="p">),</span>
    <span class="p">]</span>
    
    data <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">"emotions.xml"</span><span class="p">)</span>
    
    res <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>testing<span class="o">.</span>cross_validation<span class="p">(</span>learners<span class="p">,</span> data<span class="p">,</span><span class="mi">2</span><span class="p">)</span>
    loss <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>scoring<span class="o">.</span>mlc_hamming_loss<span class="p">(</span>res<span class="p">)</span>
    accuracy <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>scoring<span class="o">.</span>mlc_accuracy<span class="p">(</span>res<span class="p">)</span>
    precision <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>scoring<span class="o">.</span>mlc_precision<span class="p">(</span>res<span class="p">)</span>
    recall <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>scoring<span class="o">.</span>mlc_recall<span class="p">(</span>res<span class="p">)</span>
    <span class="k">print</span> <span class="s">'loss='</span><span class="p">,</span> loss
    <span class="k">print</span> <span class="s">'accuracy='</span><span class="p">,</span> accuracy
    <span class="k">print</span> <span class="s">'precision='</span><span class="p">,</span> precision
    <span class="k">print</span> <span class="s">'recall='</span><span class="p">,</span> recall







### References





	  * G. Tsoumakas and I. Katakis. _Multi-label classification: An overview". International Journal of Data Warehousing and Mining, 3(3):1-13, 2007._
	  * E. Spyromitros, G. Tsoumakas, and I. Vlahavas, _An Empirical Study of Lazy Multilabel Classification Algorithms_. Proc. 5th Hellenic Conference on Artificial Intelligence (SETN 2008), Springer, Syros, Greece, 2008.
	  * M. Zhang and Z. Zhou. _ML-KNN: A lazy learning approach to multi-label learning_. Pattern Recognition, 40, 7 (Jul. 2007), 2038-2048.
	  * S. Godbole and S. Sarawagi. _Discriminative Methods for Multi-labeled Classification_, Proceedings of the 8th Pacific-Asia Conference on Knowledge Discovery and Data Mining, PAKDD 2004.
	  * R. E. Schapire and Y. Singer. _Boostexter: a bossting-based system for text categorization_, Machine Learning, vol.39, no.2/3, 2000, pp:135-68.

