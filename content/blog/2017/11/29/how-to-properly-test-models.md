+++
author="AJDA"
date= '2017-11-29 12:26:44+00:00'
draft= false
title="How to Properly Test Models"
type="blog"
blog=["analysis" ,"classification" ,"education" ,"overfitting" ,
"predictive  analytics" ,"scoring" ,"workshop" ]
+++

On Monday we finished the second part of the workshop for the [Statistical Office](http://www.stat.si/StatWeb/en) of Republic of Slovenia. The crowd was tough - these guys knew their numbers and asked many challenging questions. And we loved it!

![](/images/2017/11/IMG_20171124_120523.jpg)

One thing we discussed was how to properly test your model. Ok, we know never to test on the same data you've built your model with, but even training and testing on separate data is sometimes not enough. Say I've tested Naive Bayes, Logistic Regression and Tree. Sure, I can select the one that gives the best performance, but we could potentially (over)fit our model, too.

To account for this, we would normally split the data to 3 parts:

1. training data for building a model
2. validation data for testing which parameters and which model to use
3. test data for estmating the accurracy of the model

Let us try this in Orange. Load _heart-disease.tab_ data set from _Browse documentation data sets_ in File widget. We have 303 patients diagnosed with blood vessel narrowing (1) or diagnosed as healthy (0).

![](/images/2017/11/Screen-Shot-2017-11-29-at-11.19.15.png)

Now, we will split the data into two parts, 85% of data for training and 15% for testing. We will send the first 85% onwards to build a model.

![](/images/2017/11/Screen-Shot-2017-11-29-at-10.37.18.png)

![](/images/2017/11/Screen-Shot-2017-11-29-at-10.37.24.png)
We sampled by a fixed proportion of data and went with 85%, which is 258 out of 303 patients.

We will use Naive Bayes, Logistic Regression and Tree, but you can try other models, too. This is also a place and time to try different parameters. Now we will send the models to Test & Score. We used cross-validation and discovered Logistic Regression scores the highest AUC. Say this is the model and parameters we want to go with.

![](/images/2017/11/Screen-Shot-2017-11-29-at-11.11.10.png)


![](/images/2017/11/Screen-Shot-2017-11-29-at-11.11.57.png)

Now it is time to bring in our test data (the remaining 15%) for testing. Connect Data Sampler to Test & Score once again and set the connection Remaining Data - Test Data.

![](/images/2017/11/Screen-Shot-2017-11-29-at-10.38.15.png)

Test & Score will warn us we have test data present, but unused. Select Test on test data option and observe the results. These are now the proper scores for our models.

![](/images/2017/11/Screen-Shot-2017-11-29-at-11.12.56.png)


![](/images/2017/11/Screen-Shot-2017-11-29-at-11.00.17.png)

Seems like LogReg still performs well. Such procedure would normally be useful when testing a lot of models with different parameters (say +100), which you would not normally do in Orange. But it's good to know how to do the scoring properly. Now we're off to report on the results in Nature... ;)
