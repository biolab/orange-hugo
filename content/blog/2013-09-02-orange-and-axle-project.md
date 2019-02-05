+++
author="BIOLAB"
date= '2013-09-02 21:27:00+00:00'
draft= false
title="Orange and AXLE project"
type="blog"
categories=["dataloading" ,"features" ,"future" ,"orange3" ,"sql" ]
tags=["2ndquadrant" ,"axle" ,"bigdata" ,"portavita" ,"sql" ]

+++

Our group at University of Ljubljana is a partner in the EU 7FP project [Advanced Analytics for Extremely Large European Databases (AXLE)](http://axleproject.eu/). The project is particularly interesting because of the diverse partners that cover the entire vertical, from studying hardware architectures that would better support extremely large databases (University of Manchester, Barcelona Supercomputing Center) to making the necessary adjustments related to speed and security of databases (2ndQuadrant) to data analytics (our group) to handling and analyzing real data and decision making (Portavita).

As a result of the project, Orange will be better connected with databases. Currently, all data is stored in working memory, while the forthcoming Orange 3.0 will be able to handle data that is stored in the database. We are working on a parallel computation architecture. Visualization of large data also presents a big challenge: we cannot transfer large amounts of data from the database to the desktop, and on the other hand it is difficult to provide a rich interactive experience if visualizations are created on the server-side. Also, most visualizations are intrinsically unsuitable for large data sets. For instance, the scatter plot represents each data instance with a symbol. Even when the datum is represented with a single pixel, only a few million data points fits on the computer screen. So in the context of big data, we will have to replace scatterplots with heatmaps.

What have we got so far? Orange 3, which is in early stage of development, features a new architecture, which allows the data to be stored either in memory or on a database. In the latter case, selecting a subset of features or filtering the data does not copy the data but only modifies the queries that are used to access the data when needed. Computation of, for instance, distributions or contingency matrices is performed on the server, so only the minimal amount of data is transferred to the client.

We also already have a small suite of widgets that work with this new architecture. Just to wet your appetite, here is the new box plot widget.

![](/images/2013/09/02/boxplot-orange30.png__620x311_q95_crop_upscale.png)

