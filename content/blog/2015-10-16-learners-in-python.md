+++
author="AJDA"
date= '2015-10-16 08:32:43+00:00'
draft= false
title="Learners in Python"
type="blog"
categories=["classification" ,"examples" ,"orange3" ,"python" ,"scripting" ]
tags=["classification" ,"orange3" ,"predictions" ,"probability" ,"python" ]

+++

We've already written about [classifying instances in Python](http://blog.biolab.si/2015/08/14/classifying-instances-with-orange-in-python/). However, it's always nice to have a comprehensive list of classifiers and a step-by-step procedure at hand.




**TRAINING THE CLASSIFIER**


We start with simply importing Orange module into Python and loading our data set.

    
    <code><span style="font-weight: 400;">>>> import Orange</span>
    <span style="font-weight: 400;">>>> data = Orange.data.Table("titanic")</span></code>


We are using 'titanic.tab' data. You can load any data set you want, but it does have to have a categorical class variable (for numeric targets use regression). Now we want to train our classifier.

    
    <code><span style="font-weight: 400;">>>> learner = Orange.classification.LogisticRegressionLearner()</span>
    <span style="font-weight: 400;">>>> classifier = learner(data)</span>
    <span style="font-weight: 400;">>>> classifier(data[0])</span></code>


Python returns the index of the value, as usual.

    
    <code><span style="font-weight: 400;">array[0.]</span></code>


To check what's in the class variable we print:

    
    <code><span style="font-weight: 400;">>>>print("Name of the variable: ", data.domain.class_var.name)</span>
    <span style="font-weight: 400;">>>>print("Class values: ", data.domain.class_var.values)</span>
    <span style="font-weight: 400;">>>>print("Value of our instance: ", data.domain.class_var.values[0])</span>
    
    <span style="font-weight: 400;">Name of the variable: survived</span>
    <span style="font-weight: 400;">Class values: no, yes</span>
    <span style="font-weight: 400;">Value of our instance: no
    </span></code>





**PREDICTIONS**


If you want to get predictions for the entire data set, just give the classifier the entire data set.

    
    <code><span style="font-weight: 400;">>>> classifier(data)</span>
    
    <span style="font-weight: 400;">array[0, 0, 0, ..., 1, 1, 1]</span></code>


If we want to append predictions to the data table, first use classifier on the data, then create a new domain with an additional meta attribute and finally form a new data table with appended predictions:

    
    <code><span style="font-weight: 400;">svm = classifier(data)</span>
    
    <span style="font-weight: 400;">new_domain = Orange.data.Domain(data.domain.attributes, data.domain.class_vars, [data.domain.class_var])</span>
    
    <span style="font-weight: 400;">table2 = Orange.data.Table(new_domain, data.X, data.Y, svm.reshape(-1, 1))</span></code>


We use .reshape to transform vector data into a reshaped array. Then we print out the data.

    
    <code><span style="font-weight: 400;">print(table2)</span></code>





**PARAMETERS**


Want to use another classifier? The procedure is the same, simply use:

    
    <code><span style="font-weight: 400;">Orange.classification.<algorithm-name>()</span></code>


For most classifiers, you can set a whole range of parameters. Logistic Regression, for example, uses the following:

    
    <code><span style="font-weight: 400;">learner = Orange.classification.LogisticRegressionLearner(</span>**penalty**<span style="font-weight: 400;">='l2', </span>**dual**<span style="font-weight: 400;">=False, </span>**tol**<span style="font-weight: 400;">=0.0001, </span>**C**<span style="font-weight: 400;">=1.0, </span>**fit_intercept**<span style="font-weight: 400;">=True, </span>**intercept_scaling**<span style="font-weight: 400;">=1, </span>**class_weight**<span style="font-weight: 400;">=None, </span>**random_state**<span style="font-weight: 400;">=None, </span>**preprocessors**<span style="font-weight: 400;">=None)</span></code>


To check the parameters for the classifier, use:

    
    <code><span style="font-weight: 400;">print(Orange.classification.SVMLearner())
    </span></code>





**PROBABILITIES**


Another thing you can check with classifiers are the probabilities.

    
    <code><span style="font-weight: 400;">classifier(data[0], Orange.classification.Model.ValueProbs)</span>
    
    <span style="font-weight: 400;">>>></span><span style="font-weight: 400;"> (array([ 0.]), array([[ 1.,  0.]]))</span></code>


The first array is the value for your selected instance (data[0]), while the second array contains probabilities for class values (probability for ‘no’ is 1 and for ‘yes’ 0).




**CLASSIFIERS**


And because we care about you, we’re giving you here a full list of classifier names:

_LogisticRegressionLearner()_

_NaiveBayesLearner()_

_KNNLearner()_

_TreeLearner()_

_MajorityLearner()_

_RandomForestLearner()_

_SVMLearner()_



For other learners, you can find all the parameters and descriptions [in the documentation](https://docs.orange.biolab.si/3/data-mining-library/reference/classification.html).


