+++
author="AJDA"
date= '2017-11-03 12:40:06+00:00'
draft= false
title="Neural Network is Back!"
type="blog"
categories=["classification" ,"neuralnetwork" ,"orange3" ,"regression" ,"widget"  ]
+++

We know you've missed it. We've been getting many requests to bring back Neural Network widget, but we also had many reservations about it.

Neural networks are powerful and great, but to do them right is not straight-forward. And to do them right in the context of a GUI-based visual programming tool like Orange is a twisted double helix of a roller coaster.

Do we make each layer a widget and then stack them? Do we use parallel processing or try to do something server-side? Theano or Keras? Tensorflow perhaps?

We were so determined to do things properly, that after the n-th iteration we still had no clue what to actually do.

Then one day a silly novice programmer (a.k.a. me) had enough and just threw scikit-learn's [Multi-layer Perceptron model](http://scikit-learn.org/stable/modules/neural_networks_supervised.html) into a widget and called it a day. There you go. A Neural Network widget just like it was in Orange2 - a wrapper for a scikit's function that works out-of-the-box. Nothing fancy, nothing powerful, but it does its job. It models things and it predicts things.

Just like that:

![](/images/2017/10/Screen-Shot-2017-11-03-at-13.32.28.png)

Have fun with the new widget!








