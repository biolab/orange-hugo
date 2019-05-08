+++
author="MARKO"
date= '2018-04-05 08:22:20+00:00'
draft= false
title="Unfreezing Orange"
type="blog"
categories=["neuralnetwork" ,"orange3" ,"parallelization" ,"performance" ,"programming"  ,"python" ,"qt" ]
+++

Have you ever tried Orange with data big enough that some widgets ran for more than a second? Then you have seen it: Orange froze. While the widget was processing, the interface would not respond to any inputs, and there was no way to stop that widget.

Not all the widgets freeze, though! Some widgets, like Test & Score, k-Means, or Image Embedding, do not block. While they are working, we are free to build other parts of the workflow, and these widgets also show their progress. Some, like Image Embedding, which work with lots of images, even allow interruptions.

![](/images/2018/04/progressbar.png)


Why does Orange freeze? Most widgets process users' actions directly: after an event (click, pressed key, new input data) some code starts running: until it finishes, the interface can not respond to any new events. This is a reasonable approach for short tasks, such as making a selection in a Scatter Plot. But with longer tasks, such as building a Support Vector Model on big data, Orange gets unresponsive.

To make Orange responsive while it is processing, we need to start the task in a new thread. As programmers we have to consider the following:

1. Starting the task. We have to make sure that other (older) tasks are not running.
2. Showing results when the task has finished.
3. Periodic communication between the task and the interface for status reports (progress bars) and task stopping.


![](/images/2018/04/figure.png)


Starting the task and showing the results are straightforward and [well documented in a tutorial for writing widgets](http://orange-development.readthedocs.io/tutorial-responsive-gui.html). Periodic communication with stopping is harder: it is completely task-dependent and can be either trivial, hard, or even impossible. Periodic communication is, in principle, unessential for responsiveness, but if we do not implement it, we will be unable to stop the running task and progress bars would not work either.

Taking care of periodic communication was the hardest part of making the Neural Network widget responsive. It would have been easy, had we implemented neural networks ourselves. But we use the [scikit-learn implementation](http://scikit-learn.org/stable/modules/neural_networks_supervised.html), which does not expose an option to make additional function calls while fitting the network (we need to run code that communicates with the interface). We had to resort to a trick: we modified fitting so that a change to an attribute called `n_iters_` called a function ([see pull request](https://github.com/biolab/orange3/pull/2958)). Not the cleanest solution, but it seems to work.

For now, only a few widgets work so that the interface remains responsive. We are still searching for the best way to make existing widgets behave nicely, but responsiveness is now one of our priorities.
