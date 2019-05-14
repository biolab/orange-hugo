+++
author="BIOLAB"
date= '2012-05-15 06:00:00+00:00'
draft= false
title="Orange GSoC: Computer vision add-on for Orange"
type="blog"
categories=["computervision" ,"gsoc" ]
+++

This summer I got the chance to develop an add-on for Orange that will introduce basic computer vision functionality, as a part of [Google Summer of Code](http://www.google-melange.com/gsoc/homepage/google/gsoc2012).

The add-on will consist of a set of widgets, each with it's own dedicated purpose, which can be seamlessly connected to provide most commonly used image preprocessing functionality.

Here is a list of the widgets:
  
* Widget for viewing image files (add description)  
* Widget for resizing an image  
* Widget for rotation/flipping of the image  
* Widget for converting the color mode (RGB, HSV, Grayscale etc.)  
* Widget for changing the hue/saturation, brightness/contrast and inverting the image  
* Widget for generic transformations through convolution with a matrix

Also, if there is enough time left throughout the GSoC period, a face detection widget will be built in order to demonstrate the power of the underlying libraries.

These are all things that have been implemented in Python before. Reimplementing them is of course a rather bad idea, so I will use an library called [OpenCV](http://opencv.willowgarage.com/wiki/). It is written in C++ and has Python bindings, and is the most widely used computer vision library, by far. So the core of the widgets will be written in it, and the GUI using [PyQT](http://www.riverbankcomputing.co.uk/software/pyqt/intro), the library used for building the Orange Canvas.

Although working with images is not Oranges' main thing, the knowledge gathered while developing the add-on will be used to improve in a number of ways: finding a general structure for add-ons developed in the future, improving the way they are distributed and the way they are tested.

Finally, I want to thank the Orange core team for having faith in me and giving me the chance to spend the summer working on an idea I care about. I'm very grateful for that and I hope I'll exceed their expectations.
