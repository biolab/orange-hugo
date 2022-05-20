+++
author = "Noah Novšak"
date = "2022-05-13"
draft = false
title = "Predictive Modelling with Attribute Interactions"
type = "blog"
thumbImage = "/blog_img/2022/2022-05-06-interactions.png"
frontPageImage = "/blog_img/2022/2022-05-06-interactions.png"
blog = ["orange", "interaction", "addons"]
shortExcerpt = "A quick introduction to using the new Interactions widget in Orange 3"
longExcerpt = "The Interactions widget has been added back to Orange 3. Illustrating how to use attribute interactions to improve predictive models."
x2images = true  # true if using retina screenshots, else false
+++

The *Interactions* widget is one of the newest additions to Orange. Previously only available in Orange 2, it has been rewritten and is accessible in the prototype add-on. This way, one need not go through the trouble of [compiling older versions](/blog/2022/2022-01-10-orange2/) anymore.

But what does it do?

It computes and displays the [interaction](http://stat.columbia.edu/~jakulin/Int/) between attributes by calculating the mutual information between them and a third target variable. Doing so provides insight into the data at hand and aids in the search for better visualizations and predictive models.

As far as visualizations go, consider [Scatter Plot](/widget-catalog/visualize/scatterplot/). Connecting Interactions to the *Features* input allows the user to manually select the projection, similarly to the *find informative projections* button, but with a little more oomph. Enabling sorting, filtering, attribute selection, and offering a clear view into, where the information is coming from, be it from one single feature or a specific combination.

Another, possibly even more intriguing application would be, as mentioned, improving the performance of prediction models. To illustrate, let's take a look at the *MONK* dataset, readily available directly within Orange, in the [Datasets](/widget-catalog/data/datasets/) widget. First, we can try and see how well a Naive Bayes Classifier (NBC) can predict the target variable like so.

{{<window-screenshot src="/blog_img/2022/2022-05-06-interactions-workflow.png">}}

Taking, for example, the Area Under Curve (AUC) score of `0.741` as a  baseline, we can see that, already, our model performs quite well. But we know we can do better than that! We want to see what makes the model tick, so let's take a closer look at our data by utilizing the new interactions widget in our workflow and examining the results.

{{<window-screenshot src="/blog_img/2022/2022-05-06-interactions.png">}}

While neither `a` nor `b` carries much information independently, their combination tells a great deal about our target variable. With this in mind, we can now use the [Feature Constructor](/widget-catalog/transform/featureconstructor/) widget to combine attributes `a` and `b` into a single feature and retrain our model. Applying all these steps then yields a workflow resembling this.

{{<window-screenshot src="/blog_img/2022/2022-05-06-interactions-updated-workflow.png">}}

Lo and behold! It looks like the extra trouble has paid off. We have managed to improve our model's performance and have ended up with an AUC score of `1.0` by accounting for the codependence of variables (something models such as NBC lack by definition).

I hope this short display sheds some light on all the possibilities interaction analysis provides and urge you to try it out on some real-world data.
