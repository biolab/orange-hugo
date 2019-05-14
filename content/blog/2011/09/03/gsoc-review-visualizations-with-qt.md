+++
author="BIOLAB"
date= '2011-09-03 08:28:00+00:00'
draft= false
title="GSoC Review: Visualizations with Qt"
type="blog"
categories=["gsoc" ,"plot" ,"qt" ,"visualization" ]
tags=["gsoc" ,"plot" ,"qt" ,"visualization" ]

+++

During the course of this summer, I created a new plotting library for Orange plot, replacing the use of PyQwt. I can say that I have succesfully completed my project, but the library (and especially the visualization widgets) could still use some more work. The new library supports a similar interface, so little change is needed to convert individual widgets, but it also has several advantages over the old implementation:  

* Animations: When using a single curve to show all data points, data changes only move the points instead of replacing them. These moves are now animated, as are color and size changes.   
* Multithreading: All position calculations are done in separate threads, so the interface remains responsive even when an long operation is running in the background.   
* Speed: I removed several occurances of needlessly clearing and repopulating the graph.   
* Simplicity: Because it was written with Orange in mind, the new library has functions that match Orange's data structures. This leads to simpler code in widgets using the library, and less operations in Python.   
* Appearance: The plot can use the system palette, or a custom color theme. In general, I think it looks much nicer that Qwt-based plots.   
* Documentation: There is an extensive API documentation (will soon be available at [Orange 2.5 documentation](/doc/orange25/OrangeWidgets.plot.html)), as well as two widget examples. 

However, there are also disadvantages to using the new library. They are not many, and I've been trying to keep them as few and as small as possible, but there still are some.   

* Line rendering: For some reason, whenever lines are rendered on the plot, the whole widget starts acting very slow. The effect is even more noticeable when zooming. As far as I can tell, this happens in Qt's drawing libraries, so there is not much I can do about it.   
* Axis labels: With a large number of long axis labels, the formatting gets rather ugly. This is a minor inconvenience, but it does make the plots look unprofessional. 

Fortunately, I have little school obligations this september, so I think I will be able to work on Orange some more, at least until school starts. I have already added gesture support and some minor improvements since the end of the program. 

Finally, I'd like to take this opportunity to thank the Orange team, especially my mentor Miha, for accepting me and helping me throughout the summer. It's been an interesting project, and I'll be happy to continue working with the same software and the same team. 
