+++
author="BIOLAB"
date= '2013-02-14 14:37:00+00:00'
draft= false
title="New canvas"
type="blog"
categories=["canvas" ,"features" ]
tags=["bundles" ,"canvas" ,"install" ,"orange2" ]

+++

Orange Canvas, a visual programming environment for Orange, has been around for a while. Integrating new and new features degraded the quality of code to a point where further development proved to be a daunting task. With ever increasing number of widgets, the existing widget toolbar is becoming harder and harder to use, but improving it is really hard. For that reason, we decided Orange needs a new Canvas, a rewrite, that would keep all of the feature of the existing one, but introduce the needed structure and modularity to the source code.

The project started about a year ago, and more than 20 thousand lines of code later, we have something to show you. As of yesterday, the new canvas was merged to the main Orange repository, where it lives alongside the old one. At the moment, it still lacks a lot of testing, some features are not completely implemented, but the main functionality, i.e. visual programming with widgets and links, should work.

![](/images/2013/02/14/screen_shot_2013-02-14_at_144527.png__616x616_q95_upscale.png)


If you are feeling adventurous, you can try it out yourself. Download the latest version from our website and run:

Windows:

    
    C:\Python27\python.exe -m Orange.OrangeCanvas.main


Mac OS X bundle:

    
    /Applications/Orange.app/Contents/MacOS/python -m Orange.OrangeCanvas.main


or, regardless of your operating system,

    
    python -m Orange.OrangeCanvas.main


with the python that has Orange installed.

What to expect?

Nothing will explode, but short of that, anything might happen. If you stumble upon issues or have helpful suggestions, please post them on our [issue tracker](http://orange.biolab.si/trac/newticket?component=new-canvas). There are some known [problems we are aware of](http://orange.biolab.si/trac/query?status=accepted&status=assigned&status=new&status=reopened&component=new-canvas&col=id&col=summary&col=component&col=type&col=status&col=milestone&order=priority); you do not need to report those :).
