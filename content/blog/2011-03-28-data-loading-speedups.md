+++
author="MARKO"
date= '2011-03-28 13:04:00+00:00'
draft= false
title="Data loading speedups"
type="blog"
categories=["dataloading" ,"performance" ]
tags=["dataloading" ,"performance" ]

+++

Orange has been loading data faster since the end of February, especially if there are many attributes in the file.

Quick comparisons between the old new versions, measured on my computer:  * adult.tab (32561 examples, 15 attributes): old version = 1.41s, new version = 0.86s.  * DLBCL.tab (77 examples, 7071 attributes): old version = 2.72s, new version = 0.93s.  * GDS1962.tab (104 examples, 31837 attributes): old version = 33.5s, new version = 6.6s.

The speedups were obtained with:  * reuse of a buffer for parsing,  * skipping type detection for attributes with known types, and  * by keeping attributes in a different data structure internally.
