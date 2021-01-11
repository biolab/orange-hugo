+++
author="AJDA"
date= '2015-10-16 08:32:43+00:00'
draft= false
title="Learners in Python"
type="blog"
blog=["classification" ,"examples" ,"orange3" ,"python" ,"scripting" ]
+++

We've already written about [classifying instances in Python](/blog/2015/08/14/classifying-instances-with-orange-in-python/). However, it's always nice to have a comprehensive list of classifiers and a step-by-step procedure at hand.




**TRAINING THE CLASSIFIER**


We start with simply importing Orange module into Python and loading our data set.

    
    >>>> import Orange
    >>>> data = Orange.data.Table("titanic")


We are using 'titanic.tab' data. You can load any data set you want, but it does have to have a categorical class variable (for numeric targets use regression). Now we want to train our classifier.

    
    >>>> learner = Orange.classification.LogisticRegressionLearner()
    >>>> classifier = learner(data)
    >>>> classifier(data[0])


Python returns the index of the value, as usual.

    
    array[0.]


To check what's in the class variable we print:

    
    >>>>print("Name of the variable: ", data.domain.class_var.name)
    >>>>print("Class values: ", data.domain.class_var.values)
    >>>>print("Value of our instance: ", data.domain.class_var.values[0])
    
    Name of the variable: survived
    Class values: no, yes
    Value of our instance: no





**PREDICTIONS**


If you want to get predictions for the entire data set, just give the classifier the entire data set.

    
    >>>> classifier(data)
    
    array[0, 0, 0, ..., 1, 1, 1]


If we want to append predictions to the data table, first use classifier on the data, then create a new domain with an additional meta attribute and finally form a new data table with appended predictions:

    
    svm = classifier(data)
    
    new_domain = Orange.data.Domain(data.domain.attributes, data.domain.class_vars, [data.domain.class_var])
    
    table2 = Orange.data.Table(new_domain, data.X, data.Y, svm.reshape(-1, 1))


We use .reshape to transform vector data into a reshaped array. Then we print out the data.

    
    print(table2)





**PARAMETERS**


Want to use another classifier? The procedure is the same, simply use:

    
    Orange.classification.<algorithm-name>()


For most classifiers, you can set a whole range of parameters. Logistic Regression, for example, uses the following:

    
    learner = Orange.classification.LogisticRegressionLearner(**penalty**='l2', **dual**=False, **tol**=0.0001, **C**=1.0, **fit_intercept**=True, **intercept_scaling**=1, **class_weight**=None, **random_state**=None **preprocessors**=None)


To check the parameters for the classifier, use:

    
    print(Orange.classification.SVMLearner())





**PROBABILITIES**


Another thing you can check with classifiers are the probabilities.

    
    classifier(data[0], Orange.classification.Model.ValueProbs)
    
    >>>(array([ 0.]), array([[ 1.,  0.]]))


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



For other learners, you can find all the parameters and descriptions [in the documentation](https://docs.biolab.si/orange/3/data-mining-library/tutorial/classification.html).


