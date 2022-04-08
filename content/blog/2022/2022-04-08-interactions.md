+++

author = "Noah Novšak"
date = "2022-04-08"
draft = false
title = "Predictive Modelling with Attribute Interactions"
type = "blog"
thumbImage = "/blog_img/2022/image-20220408145950556.png"
frontPageImage = "/blog_img/2022/image-20220408145950556.png"
blog = []
shortExcerpt = "Interactions add-on now in Orange 3 "
longExcerpt = "Interactions add-on has been rewritten and added back to Orange 3. See how to use attribute interactions to improve predictive models."
x2images = true  # true if using retina screenshots, else false

+++

The *Interactions* widget is one of the newest additions to Orange. Previously only available in Orange 2, it has now been rewritten and is accessible as a prototype add-on. This way one needs not go through the trouble of *compiling older versions* anymore.

But what does it do?

Good question! First and foremost it calculates the mutual information that two attributes carry about a target variable as well as the *interaction* between them. This can give insight on the data at hand and help find nicer visualizations or improve prediction models.

As far as visualizations go, consider *Scatter Plot*. Connecting Interactions to the *Features* input enables the user to select the projection, similarly to the *find informative projections* button, but with a little more bells and whistles. Enabling sorting, filtering and selecting attributes desired attributes as well as giving a clearer view as to where the information is coming from, be it one single attribute or a combination of the two.

Another, possibly even more intriguing application would be, as mentioned, improving the performance of prediction models. Using for example the *MONK* dataset, we can try and see how well a Naive Bayes Classifier (NBC) can predict the target variable like so.

{{<window-screenshot src="/blog_img/2022/image-20220408145907091.png">}}

As it turns out, it performs admirably with a precision score of $0.832$. However, before we sit down and call it a day let's take a step back to consider our data. Doing this may give us some insight on what makes the model work so well and where there might still be some room for improvement. So, first let's calculate the attribute interactions.

{{<window-screenshot src="/blog_img/2022/image-20220408145950556.png">}}

Our little escapade has yielded some promising results! While neither *a* nor *b* carry much information on their own, their combination tells a great deal about our target variable. Using this knowledge we can now use the *Feature Constructor* widget to combine the two attributes, and retry the model on our newly constructed data. Our updated workflow might now look something like this.

{{<window-screenshot src="/blog_img/2022/image-20220408155015419.png">}}

Looks like all the extra trouble has paid off. We have managed to greatly improve our model's performance by taking into account the codependence of variables (something models such as NBC lack by definition). 

And that's it for a quick rundown of the capabilities and usefulnes of the new Interactions widget.

