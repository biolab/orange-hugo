+++
title= "Train and Test Data"
images =  ["/workflow_images/data-sampler.png"]
type = "workflows"
blog =  ""
video = ""
download = "420-data-sampler.ows"
workflows = ["Classification", "Data Sampler", "Predictive models"]
weight = 420
+++

In building predictive models it is important to have a separate train and test data sets in order to avoid overfitting and to properly score the models. Here we use Data Sampler to split the data into training and test data, use training data for building a model and, finally, test on test data. Try several other classifiers to see how the scores change.
