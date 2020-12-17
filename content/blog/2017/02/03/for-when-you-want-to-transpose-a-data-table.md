+++
author="AJDA"
date= '2017-02-03 13:16:37+00:00'
draft= false
title="For When You Want to Transpose a Data Table..."
type="blog"
blog=["analysis" ,"bioinformatics" ,"feature engineering" ,"features" ,"orange3"  ]
+++

Sometimes, you need something more. Something different. Something, that helps you look at the world from a different perspective. Sometimes, you simply need to transpose your data.

Since version 3.3.9, Orange has a Transpose widget that flips your data table around. Columns become rows and rows become columns. This is often useful, if you have, say, biological data.


**Related:** [Datasets in Orange Bioinformatics](/blog/2015/07/31/datasets-in-orange-bioinformatics-add-on/)


Today we will play around with _brown-selected.tab_, a data set on gene expression levels for 79 experiments. Our data table has genes in rows and experiments in columns, with gene expression levels recorded as values.

![](/images/2017/02/data-table-normal.png)

This representation focuses on exploring genes and allows them to be plotted or to construct a model to predict their functions. But what if I want to explore the experimental conditions and see how different external conditions influence the yeast cells? For this, it would be better to have experiments in rows and genes in columns. We can do this with Transpose.

![](/images/2017/02/data-table-transposed.png)

Transpose widget took our _gene_ meta attribute and used it for the new column names (YGR270W, YIL075C, etc.). It also appended class values to columns (Proteas). Former columns names (alpha 0, alpha 7, etc.) became our new meta attribute called _Feature name_.

Ok, we have a transposed data table. Now we ask ourselves: "Do similar experiment types (e.g. heat, cold, alpha, ...) behave similarly?"

Let's use PCA to transform these many-dimensional experiment vectors into a 2-D representation. We are going to use Scatter Plot to observe experiments (not genes) in a 2-D space. We expect the same experiment types to lie closer together than other experiments. A scatter plot after a 2-D transformation looks like this:

![](/images/2017/02/scatter-plot-big.png)

_Spo5 11_ lies quite far from the rest, so it could be an experiment to look out for. If we zoom in on the big cluster, we see that similar experiments indeed lie closer together.

![](/images/2017/02/scatter-plot-pca.png)

Now, if you are reproducing the result, you probably won't see these nice colors for class.

![](/images/2017/02/Screen-Shot-2017-02-03-at-12.29.20.png)

This is because we used the Create Class widget to help us create new class values. Create Class already available in [Orange3-Prototypes](https://github.com/biolab/orange3-prototypes) add-on and will be included in a future Orange release. You can learn more about it soon... :)


