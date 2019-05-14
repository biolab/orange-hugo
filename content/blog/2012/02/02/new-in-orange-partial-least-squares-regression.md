+++
author="BIOLAB"
date= '2012-02-02 16:21:00+00:00'
draft= false
title="New in Orange: Partial least squares regression"
type="blog"
categories=["multitarget" ,"pls" ,"regression" ]
tags=["multitarget" ,"pls" ,"regression" ]

+++

[Partial least squares regression](http://en.wikipedia.org/wiki/Partial_least_squares_regression) is a regression technique which supports multiple response variables. PLS regression is very popular in areas such as bioinformatics, chemometrics etc. where the number of observations is usually less than the number of measured variables and where there exists multicollinearity among the predictor variables. In such situations, standard regression techniques would usually fail. The PLS regression is now available in Orange (see [documentation](/doc/reference/Orange.regression.pls))!

You can use PLS regression model on single-target or [multi-target](/blog/2012/01/09/multi-label-classification-and-multi-target-prediction-in-orange/) data sets. Simply load the data set [multitarget-synthetic.tab](/doc/reference/_downloads/multitarget-synthetic.tab) and see that it contains three predictor variables and four responses using this code.


    data = Orange.data.Table("multitarget-synthetic.tab")
    print "Input variables:"
    print data.domain.features
    print "Response variables:"
    print data.domain.class_vars


Output:
    
    Input variables:
    <FloatVariable 'X1', FloatVariable 'X2', FloatVariable 'X3'>
    Response variables:
    <FloatVariable 'Y1', FloatVariable 'Y2', FloatVariable 'Y3', FloatVariable 'Y4'>


As you can see, all variables in this data set are continuous. The PLS regression is intended forsuch situations although it can be used for discrete input variables as well (using 0-1 continuation). Currently, discrete response variables are not yet supported.

Let's try to fit the PLS regression model on our data set.


   learner = Orange.multitarget.pls.PLSRegressionLearner()
   classifier = learner(data)


The classifier can be now used to predict values of the four responses based onthree predictors. Let's see how it manages this task on the first data instance.

    
    actual = data[0].get_classes()
    predicted = classifier(data[0]) 

    print "Actual", "Predicted"
    for a, p in zip(actual, predicted):
        print "%6.3f %6.3f" % (a,p)


Output:
    
    Actual Predicted
     0.490  0.613
     1.237  0.826
     1.808  1.084
     0.422  0.534


To test the usefulness of PLS as a multi-target method let's compare it to a single-target method - linear regression. We did this by comparing [Root mean squared error](http://en.wikipedia.org/wiki/Mean_squared_error) (RMSE) of predicted values for a single response variable. We constructed synthetic data sets and performed the RMSE analysis using [this script](/images/2012/02/02/pls_vs_linear.py). The results can be seen in the following output:

    
     Training set sizes      5     10     20     50    100    200    500   1000
     Linear (single-target) 0.5769 0.3128 0.2703 0.2529 0.2493 0.2446 0.2436 0.2442
     PLS (multi-target) 0.3663 0.2955 0.2623 0.2517 0.2487 0.2447 0.2441 0.2448


We can see that PLS regression outperforms linear regression when the number of training instances is low. Such situations (low number of instances compared to high number of variables) are quite common when analyzing data sets in bioinformatics. However, with increasing number of training instances, the advantages of PLS regression diminish.
