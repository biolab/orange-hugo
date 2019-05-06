+++
author="BIOLAB"
date= '2012-04-30 12:00:00+00:00'
draft= false
title="Orange GSoC: Multi-Target Learning for Orange"
type="blog"
categories=["classification" ,"gsoc" ,"multitarget" ]
tags=["classification" ,"gsoc" ,"multitarget" ]

+++

Orange already supports multi-target classification, but the current implementation of clustering trees is written in Python. One of the five projects Orange has chosen at this year's Google Summer of Code is the implementation of clustering trees in C. The goal of my project is to speed up the building time of clustering trees and lower their spatial complexity, especially when used in random forests. Implementation will be based on Orange's SimpleTreeLearner and will be integrated with Orange 3.0.

Once the clustering trees are implemented and integrated, documentation and unit tests will be written. Additionally I intend to make an experimental study that will compare the effectiveness of clustering trees with established multi-target classifiers (like PLS and chain classifiers) on benchmark data-sets. I will also work on some additional tasks related to multi-target classification that I had not included in my original proposal but Orange's team thinks would be useful to include. Among these is a chain classifier framework that Orange is currently missing.

If any reader is interested in learning more about clustering trees or chain classifiers these articles should cover the basics:  

* [Top-Down Induction of Clustering Trees (1998), by Hendrik Blockeel, Luc De Raedt, Jan Ramong](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.50.3353)
* [Classiﬁer Chains for Multi-label Classiﬁcation (2009), by Jesse Read, Bernhard Pfahringer, Geoﬀ Holmes, Eibe Frank](http://www.cs.waikato.ac.nz/~eibe/pubs/chains.pdf)

I am a third year undergraduate student at the Faculty of Computer and Information Science in Ljubljana and my project will be mentored by prof. dr. Blaž Zupan. I thank him and the rest of the Orange team for advice and support.
