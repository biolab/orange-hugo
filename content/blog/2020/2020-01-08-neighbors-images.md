
+++
author = "Blaž Zupan"
date = "2020-01-08"
draft = false
title = "Look-alike Images"
type = "blog"
thumbImage = "/blog_img/2020/2020-01-08-neighbors-images-small.png"
frontPageImage = "/blog_img/2020/2020-01-08-neighbors-images-small.png"
blog = ["neighbors", "images"]
shortExcerpt = "We show how to use Neighbors widget on image embedding space to find image look-alikes."
longExcerpt = "We show how to use Neighbors widget on image embedding space to find image look-alikes."
+++

There is a cool and perhaps not often used widget in Orange called Neighbors. The widget accepts the data and a reference data item and outputs the nearest neighbors of that item.

Related: {{< link_new url="/blog/2018/02/02/image-analytics-workshop-at-aiucd-2018/" name="Image Analytics Workshop at AIUCD 2018">}}

Here I will show how to use it to display a set of images most similar to a selected reference image. I will use the following workflow:

{{< figure src="/blog_img/2020/2020-01-08-neighbors-images-workflow.png" >}}
\

We may use any collection of images, and for this blog, I have decided to pull out some image sets available from Datasets widget. To use your own collection of images, check out our [YouTube video on image clustering](https://www.youtube.com/watch?v=Iu8g2Twjn9U) to see how to prepare it. In the Dataset widget, filter the data sets to list only those that include images:

{{< figure src="/blog_img/2020/2020-01-08-neighbors-images-datasets.png" >}}
\
\

I will use Bone Healing image set from our recent [Nature Communications paper](https://www.nature.com/articles/s41467-019-12397-x). In the workflow, we first embed the images in the vector space. We send all the embedded images to the Neighbors widget through its input data channel and display them in Image Viewer. In the viewer, we can select an image. Image Viewer sends its output -- the selected image -- to the reference channel of the Neighbors widget. I have instructed this widget to send out three data items that are the most similar to the item in the reference, and on the output excluded the reference item:

{{< figure src="/blog_img/2020/2020-01-08-neighbors-images-neighbors.png" >}}
\
\

Image Viewer (1) at the end of the pipeline displays three images that are most like the chosen image:

{{< figure src="/blog_img/2020/2020-01-08-neighbors-images-result.png" >}}
\
\

Any other set of images works as well. Here is our image look-alike for traffic signs:

{{< figure src="/blog_img/2020/2020-01-08-neighbors-images-bicycles.png" >}}
\
\

We skipped any details on image embedding, measuring distances and so on. For more on these, check out our recent [paper in Nature Communications](https://www.nature.com/articles/s41467-019-12397-x) or see our [set of image analytics videos on YouTube](https://www.youtube.com/watch?v=Iu8g2Twjn9U).
