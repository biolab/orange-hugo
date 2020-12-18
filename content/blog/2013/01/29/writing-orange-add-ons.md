+++
author="BIOLAB"
date= '2013-01-29 09:00:00+00:00'
draft= false
title="Writing Orange Add-ons"
type="blog"
blog=["addons" ,"pypi" ]
+++

We officially supported add-ons in Orange 2.6. You should start by checking the [list of available add-ons](http://orange.biolab.si/addons/). We pull those automatically from the [PyPi](http://pypi.python.org/pypi), which is our preferred distribution channel. Try to install an add-on by either:



* writing "pip install <add-on name>" in the terminal or
* from the Orange Canvas GUI. Select "Options / Add-ons..." in the menu.

Everything should just work. Writing add-ons is as easy as writing your own [Orange Widgets](http://docs.orange.biolab.si/latest/extend-widgets/rst/) or [Orange Scripts](http://docs.orange.biolab.si/latest/tutorial/rst/). Just follow [this tutorial](http://orange.biolab.si/trac/wiki/AddOns) and you will have your brand-new Orange add-on on PyPi in no time (an hour at most).

![](/images/2013/01/29/orange-add-ons.png__400x382_q95_crop_upscale.png)

