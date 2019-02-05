+++
author="BIOLAB"
date= '2011-06-30 12:55:00+00:00'
draft= false
title="'Orange GSoC: Visualizations with Qt'"
type="blog"
categories=["gsoc" ,"visualization" ]
tags=["gsoc" ,"visualization" ]

+++

Hello, my name is Miha Čančula and this summer I'm working on Orange as part of Google's Summer of Code program, mentored by Miha Štajdohar. My task is to replace the current visualization framework based on Qwt with a custom library, depending only on Qt. This library will better support Orange's very specific visualizations and will replace the unmaintained PyQwt. 

I have a lot of experience with Qt and its graphics classes, both in C++ and Python, but I'm relatively now to Orange. As a physics student, especially now that I'm selecting a computational physics program, this a great learning opportunity for me. 

I think my work is progressing very well, because many visualizations already work with the new library with only minor modifications:  * Scatterplot  * Linear projections  * Discretize  * All the visualizations in VizRank and FreeViz dialogs

The library is written partially in C++, especially the performance-sensitive parts, and partially in Python. It uses the Qt Graphics View Framework, with several reimplemented or wrapped method to preserve the old behavior and API. I have tried to keep the necessary modification to the widgets themselves to a minimum, so the large majority of changes are in the OWGraph class which server as the base class for all graphs. 

Graphs made by Qwt are not very flexible, they only support graphs with cartesian axes. On the other hand, visualization Orange often use custom axes and transformations. That's why I designed the new library with support for arbitrary axes, curves and other elements. All of these can be extendeng with classes written in Python, C++, or a combination thereof. The required changes to visualizations I already ported to the new OWGraph class were mostly simplifications, with very little new code added. 

For example, zooming and selection is implemented completely in the new OWGraph class, with the same function and attribute names as before, so visualizations themselves didn't need any changes at all. 

The new framework is also able to produce much nicer graphs. I haven't had the time to customize the looks much, but it's possible to set colors, line widths, point sizes and symbols from Python. There are still some settings that have no UI configuration, but I will focus on that after making sure that visualization widgets work with the new library.

Currently I'm trying to change as many widgets as possible to the new classes. As I said above, I only completed a few of them, but I believe the others won't require too much work.   
