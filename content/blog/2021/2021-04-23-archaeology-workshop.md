+++
author = "Ajda Pretnar"
date = "2021-04-23"
draft = false
title = "Data Mining for Archaeologists, part I"
type = "blog"
thumbImage = "/blog_img/2021/2021-04-23-archaeology-small.png"
frontPageImage = "/blog_img/2021/2021-04-23-archaeology-small.png"
blog = ["archaeology", "workshop", "image analytics", "amphorae"]
shortExcerpt = "The many things archaeologists can do in Orange."
longExcerpt = "A workshop about different kinds of analyses archaeologists can do in Orange."
x2images = true  # true if using retina screenshots, else false
+++

Recently, we held a workshop for a group of archaeologists. While archaeologists are quite well-versed in quantitative analysis, data science was still quite new for most of the participants. Our aim was to introduce basic data science concepts through archaeological use cases. One such case that came to our mind was predicting a type of the artefact from the image.

Related: {{< link_new url="blog/2018/11/06/data-mining-for-anthropologists/" name="Data Mining for Anthropologists">}}

We took three best-documented amphora types (types with the highest number of images) from the [Archaeology Data Service portal](https://archaeologydataservice.ac.uk/archives/view/amphora_ahrb_2005/index.cfm). We also added some metadata describing each amphora subtype.

This is how our data looks like.

{{< window-screenshot src="/blog_img/2021/2021-04-23-data-table.png" >}}

Each row represents one amphora, with type, image URL, subtype, and metadata included. Let us observe the data in an **Image Viewer** from the **Image Analytics** add-on.

{{< window-screenshot src="/blog_img/2021/2021-04-23-image-viewer.png" >}}

{{% workflow-screenshot src="/blog_img/2021/2021-04-23-workflow1.png" %}}

Images now have to be converted to numbers, so that predictive models will know how to infer patterns from them. The procedure of describing an image with a vector is called embedding and in Orange, it can be found in **Image Embedding** widget. We will use a simple, pre-trained Inception v3 model, but it is possible to train custom models specifically for archaeology.

The result of embedding is a long line of numbers.

{{< window-screenshot src="/blog_img/2021/2021-04-23-embedding.png" >}}

For the predictive model to consider only image vectors, we need to move metadata to ... well, meta attributes. We will do this with **Select Columns**.

{{< window-screenshot src="/blog_img/2021/2021-04-23-select-columns.png" >}}

{{% workflow-screenshot src="/blog_img/2021/2021-04-23-workflow2.png" %}}

Now, we can build our prediction model. Or a couple of them. We will use **Logistic Regression**, **kNN**, and **SVM**, as these are quite successful for working with images. We connect the data and the learners to **Test and Score**. Seems like all of our models are quite accurate, with logistic regression having the highest AUC score.

{{< window-screenshot src="/blog_img/2021/2021-04-23-test-and-score.png" >}}

Looking at the **Confusion Matrix**, logistic regression also best distinguishes between Dressels and Gauloises. It makes 13 mistakes, fairly equally confusing Dressels with Gauloises and vice versa. The other two classifiers more frequently confuse Gauloises for Dressels, so they are slightly biased in this sense.

{{< window-screenshot src="/blog_img/2021/2021-04-23-confusion-matrix.png" >}}

{{% workflow-screenshot src="/blog_img/2021/2021-04-23-workflow3.png" %}}

It always makes sense to check the distribution of misclassifications to determine the quality of the model. If the model just predicts the most frequent class, it is useless. Having more data would surely make this model distinguish between amphora type better.

We can use the model for predicting the type of amphora for unlabelled images. Go to the internet and find some Dressels, Gauloises, and Keays. I have three images here. I put them in a single folder and I will load them with **Import Images** widget. We have to pass the data through another **Image Embedding** widget, because this data too needs numbers. Finally, we pass the data and one of the models (say, logistic regression) to **Predictions**. Don't forget, logistic regression needs the data input to word with Predictions (you need to pass the model, not the learner).

{{< window-screenshot src="/blog_img/2021/2021-04-23-predictions.png" >}}

Seems like Dressel and Gauloise were successfully predicted, while Keay was mislabelled as a Gauloise. Not what we would have expected. Could archaeologists among you figure out, why this Keay amphora was mislabelled?

{{< window-screenshot src="/blog_img/2021/2021-04-23-workflow-final.png" >}}

In the second part of Data Mining for Archaeologists, we will have a look at geo-tagged data and how to plot them on a map.
