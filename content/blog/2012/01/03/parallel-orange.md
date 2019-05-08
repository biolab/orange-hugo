+++
author="BIOLAB"
date= '2012-01-03 08:59:00+00:00'
draft= false
title="Parallel Orange?"
type="blog"
categories=["parallelization" ]
+++

We attended a [NIPS 2011](http://nips.cc/) workshop on [processing and learning from large scale data](http://biglearn.org/). Various presenters showed different tools and frameworks that can be used when developing algorithms suitable for dealing with large scale data, but none of them were written in Python and as such, not useful for Orange. We have been looking for a framework that would help us run code in parallel for some time, but so far with no luck.

We would like to have a framework that is easy to use, can be used in C as well as in Python and supports multi-level map reduce (cross validation can be viewed as map reduce and random forest that is tested is another map-reduce). Prototypes we have created so far solve this problem by inspecting learners that are used in cross-validation and creating all "subtasks" at the same time. That results in really ugly code we don't want to commit ;). If you know a framework that would suit our needs, want to implement support for parallel computation by yourself (we will apply to [GSoC](https://code.google.com/soc/)) or have an idea how to solve this problem, feel free to contact us ;).
