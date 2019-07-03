+++
author="Ajda Pretnar"
date= '2019-06-03'
draft= false
title="Gene Expression Profiles with Line Plot"
type="blog"
thumbImage = "/blog_img/2019/6/3/gene-blog.png"
frontPageImage = "/blog_img/2019/6/3/gene-blog.png"
categories=["bioinformatics", "gene expression", "line plot"]
shortExcerpt = "We show how to explore gene expression profiles with the new Line Plot widget."

longExcerpt = "Line Plot shows profiles of data instances – each instance is a line in the plot and its profile are values across all variables in the data. We show how to explore gene expression profiles."
+++

Line Plot is one of our recent additions to the visualization widgets. It shows data profiles, meaning it plots values for all features in the data set. Each data instance in a line plot is a line or a 'profile'.

The widget can show four types of information – individual data profiles (lines), data range, mean profile and error bars. It has the same cool features of other Orange visualizations – it is interactive, meaning you can select a subset of data instances from the plot, it allows grouping by a discrete variable, and it highlights an incoming data subset.

Related: {{< link_new url="/blog/2018/12/21/scatter-plots-the-tour/" name="Scatter Plot: The Tour">}}


Let us check a simple example. We will use brown-selected data, which is a data on gene expression of baker's yeast. To observe gene expression profiles, we will use Line Plot.

\
\

{{% figure src="/blog_img/2019/6/3/gene-expression-1.png" width="80%" %}}
\
\


Since the data has class, which represents a function of the gene, Line Plot will automatically group by class variable. It seems like protease, respiratory and ribosome genes have quite distinctive profiles! Let us select the most interesting region in the plot by selecting the zoom tool and dragging across the area of interest.
\
\


{{% figure src="/blog_img/2019/6/3/gene-expression-2.png" width="80%" %}}
\
\

We see that spo-mid feature distinguishes really well between protease and two other gene types and that values of protease are normally high for spo-mid.

Another thing we can do is select a subset from the plot. If we press the ‘rectangle’ icon on the left, our plot will be automatically resized to the original size. Then we press the ‘arrow’ icon, which will put us back to the selecting mode. Now let us select Lines instead of Range and Mean for display. This will show individual expression profiles.
\
\


{{% figure src="/blog_img/2019/6/3/gene-expression-3.png" width="80%" %}}
\
\

If we click and drag across an area of interest, instances under the thick black line will be selected. We can connect, say a Box Plot to the Line Plot and observe the distribution of the selected subset. Unsurprisingly, the genes we have selected are mostly protease.
\
\

{{% figure src="/blog_img/2019/6/3/gene-expression-4.png" width="80%" %}}
\
\

{{% figure src="/blog_img/2019/6/3/gene-expression-5.png" width="50%" %}}
\
\

This is it. Line Plot is really simple to use and can reveal many interesting things not only for biologists, but for any kind of data analyst. Next week we will talk about how to work with timeseries data in combination with the Line Plot.

