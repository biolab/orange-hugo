+++
author="BIOLAB"
date= '2011-07-20 11:35:00+00:00'
draft= false
title="'Orange GSoC: Multi-label Classification Implementation'"
type="blog"
categories=["gsoc" ,"multilabel" ]
tags=["gsoc" ,"multilabel" ]

+++

Multi-label classification is one of the three projects of Google Summer Code 2011 for Orange. The main goal is to extend the Orange to support multi-label, including dataset support, two basic multi-label classifications-problem-transformation methods & algorithm adaptation methods, evaluation measures, GUI support, documentation, testing, and so on.

My name is Wencan Luo, from China. I'm very happy to work with my mentor Matija. Until now, we have finished a framework for multi-label support for Orange.

To support multi-label data structure, a special value is added into their 'attributes' dictionary. In this way, we can know whether the attribute is a type of class without altering the old Example Table class. 

Moreover, a transformation classification method to support multilabel is implemented, named Binary Relevance. All the codes are extended from the old Orange code using Python to be compatible with single-label classification methods.

In addition, the evaluator for multilalbel classification is also implemented based on the old single-label evaluator in Orange.evaluator.testing and Orange.evaluator.scoring modules. 

At last, the widget for Binary Relevance method and Evaluator is implemented.

Many work has to be done as following:  * one more transformation method  * two adaptive methods  * ranking-based evaluator  * widgets to support the above methods  * testing
