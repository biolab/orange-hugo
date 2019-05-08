+++
author="MARKO"
date= '2011-08-19 14:18:00+00:00'
draft= false
title="Golden (sublime) triangles in Orange"
type="blog"
categories=["visualization" ]
+++

Hand in hand with the development of the [new visualization framework](/blog/2011/06/30/orange-gsoc-visualizations-with-qt/) and the financial crisis we are putting some gold into Orange. The arrows at the ends of the axes are, as of today, small [golden triangles](http://en.wikipedia.org/wiki/Golden_triangle_(mathematics)). See the changes in [owaxis.py](http://orange.biolab.si/trac/intertrac/source%3Atrunk/orange/OrangeWidgets/plot/owaxis.py)!




    
    -        path.moveTo(0, 3)
    -        path.lineTo(0, -3)
    -        path.lineTo(5, 0)
    +        path.moveTo(0, 3.09)
    +        path.lineTo(0, -3.09)
    +        path.lineTo(9.51, 0)



