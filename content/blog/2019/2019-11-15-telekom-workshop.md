
+++
author="Ajda Pretnar"
date= '2019-11-15'
draft= false
title="Explaining Customer Segments for Business"
type="blog"
thumbImage = "/blog_img/2019/2019-11-15_ws-title.JPG"
frontPageImage = "/blog_img/2019/2019-11-15_ws-title.JPG"
categories=["workshop", "telco", "clustering", "nomogram"]
shortExcerpt = "Explaining customer base enables businesses to make informed decisions. We present the case for Telco companies."
longExcerpt = "Explaining customer base for businesses to make informed decisions. We present the case for Telco companies."
+++

Last month we held a workshop for a large Slovenian Telco company. Their two key questions were - what machine learning techniques can we use on our data and how do we explain the models afterwards. So the workshop focused on three use cases - product segmentation, modeling churn, and clustering customers. With any kind of models, especially unsupervised ones, we often get the question - but how can we explain the clusters? What do these clusters tell us about the customers?

{{% figure src="/blog_img/2019/2019-11-15_FRI2016.JPG" %}}
\
\

Let us see how we do this in Orange. We will use *Telecom customer churn* data set, which you can load with the Datasets widget. But we will not be interested in predicting churn, but rather how to segment customers. Orange already ignores target variable for clustering, but we can remove it with Select Columns to make the example clearer.

{{% figure src="/blog_img/2019/2019-11-15_selcol.png" %}}
\
\

Next, let us design a standard hierarchical clustering workflow. Pass the data to Distances and then to Hierarchical Clustering. Our data set is quite big and 20 variables is not negligible, but for the sake of simplicity we can use Euclidean distance in Distances and Average linkage in Hierarchical Clustering. Finally, let us select three clusters. You can of course try different parameters - say cosine distance and Ward linkage.

{{% figure src="/blog_img/2019/2019-11-15_hierclust.png" %}}
\
\

Now for the fun part. Connect another Select Columns to Hierarchical Clustering and put the Cluster variable into the *target variable* section. Then connect Naive Bayes to Select Columns and Nomogram to Naive Bayes. Like so:

{{% figure src="/blog_img/2019/2019-11-15_workflow.png" %}}
\
\

Basically, we will use cluster labels as target variable and try to predict clusters with Naive Bayes. Nomogram then helps us explain the model. Remember, Naive Bayes assumes independence between variables, so it doesn't take correlation into account. Logistic Regression does, so feel free to use it instead of Naive Bayes. Anyhow, Nomogram lists the top 10 variables that are important for defining the selected cluster. It seems that cluster C1 does not use internet (or at least does not buy internet from us). C3 on the other hand normally has the whole package.

{{% figure src="/blog_img/2019/2019-11-15_c1-explained.png" %}}
\
{{% figure src="/blog_img/2019/2019-11-15_c3-explained.png" %}}
\
\

What does this mean from a business perspective? Well, that you should focus your marketing on cluster C1 and offer discounted internet packages. Marketing to C3 would be essentially useless. This is how Orange can help you identify business opportunities and understand you customer base better.
