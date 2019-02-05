+++
author="BIOLAB"
date= '2011-09-07 10:30:00+00:00'
draft= false
title="3D Visualizations in Orange"
type="blog"
categories=["opengl" ,"visualization" ]
tags=["3d" ,"opengl" ,"visualization" ]

+++

Over the summer I worked (and still do) on several new 3D visualization widgets as well as a 3D plotting library they use, which will hopefully simplify making more widgets. The library is designed to be similar in terms of API to the new [Qt plotting library](/blog/2011/09/03/gsoc-review-visualizations-with-qt/) Noughmad is working on.

The library uses OpenGL 2/3: since Khronos deprecated parts of the old OpenGL API (particularly immediate mode and fixed-function functionality) care has been taken to use only capabilities less likely to go away in the years to come. All the drawing is done using shaders; geometry data is fed to the graphics hardware using Vertex Buffers. The library is fully functional under OpenGL 2.0; when hardware supports newer versions (3+), several optimizations are possible (e.g. geometry processing is done on the GPU rather than on CPU), possibly resulting in improved user experience.

Widgets I worked on and are reasonably usable:

#### ScatterPlot3D

[![](/images/2011/09/06/scatterplot3d.png__160x160_q95_crop_subject_location-291%2C305.jpg)
](http://blog.biolab.si/wp-content/uploads/2011/09/06/scatterplot3d.png)

Its GUI has the same options as the ordinary ScatterPlot (2D),with an additional dropdown for the third attribute (Z) and some new checkboxes (e.g. 2D/3D symbols). The data can be easily rotated, translated and scaled.Supports zoom levels and selections as well. VizRank works.Thanks to hardware acceleration, ScatterPlot3D is quite responsive even with largerdatasets (30k examples).

#### LinProj3D

[![](/images/2011/09/06/linproj3d.png__160x160_q95_crop.jpg)
](http://blog.biolab.si/wp-content/uploads/2011/09/06/linproj3d.png)

LinProj3D is displayed using dark theme (themes are available in all 3D widgets).

#### Sphereviz3D

[![](/images/2011/09/06/sphereviz.png__160x160_q95_crop.jpg)
](http://blog.biolab.si/wp-content/uploads/2011/09/06/sphereviz.png)

Sphereviz3D has 2D symbols option enabled (also available in all 3D widgets). VizRank has been modified to work with three dimensions; PCA and SPCA options under FreeViz return first three most important components when used in these widgets.

### Future

Documentation for widgets and the library is still missing. Some additional widgets are being considered, such as NetExplorer3D.

I wrote few technical details [here](http://matejd.github.com/).
