+++
author="AJDA"
date= '2015-08-28 14:05:07+00:00'
draft= false
title="Scatter Plot Projection Rank"
type="blog"
blog=["orange3" ,"visualization" ,"widget" ]
+++

One of the nicest and surely most useful visualization widgets in Orange is **Scatter Plot**. The widget displays a 2-D plot, where x and y-axes are two attributes from the data.

![](/images/2015/08/ScatterPlot1.png)

2-dimensional scatter plot visualization



Orange 2.7 has a wonderful functionality called **VizRank**, that is now implemented also in Orange 3. **Rank Projections** functionality enables you to find interesting attribute pairs by scoring their average classification accuracy. Click ‘_Start Evaluation_’ to begin ranking. 

![](/images/2015/08/ScatterPlot2.png)

Rank Projections before ranking is performed.



The functionality will also instantly adapt the visualization to the best scored pair. Select other pairs from the list to compare visualizations.

![](/images/2015/08/ScatterPlot3.png)

Rank Projections once the attribute pairs are scored.



Rank suggested _petal length_ and _petal width_ as the best pair and indeed, the visualization below is much clearer (better separated).

![](/images/2015/08/ScatterPlot4.png)

Scatter Plot once the visualization is optimized.



Have fun trying out this and other visualization widgets!
