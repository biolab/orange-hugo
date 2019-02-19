+++
author="PRIMOZGODEC"
date= '2016-08-16 17:32:20+00:00'
draft= false
title="Visualization of Classification Probabilities"
type="blog"
categories=["addons" ,"classification" ,"gsoc" ,"gsoc2016" ,"orange3" ,"widget"  ]
tags=["classification" ,"educational" ,"gsoc" ,"gsoc2016" ,"orange3" ,"polynomial"
  ,"widget" ]

+++

_This is a guest blog from the Google Summer of Code project._



[Polynomial Classification](http://orange3-educational.readthedocs.io/en/latest/widgets/polynomialclassification.html) widget is implemented as a part of my [Google Summer of Code](https://developers.google.com/open-source/gsoc/) project along with other widgets in educational add-on (see my [previous blog](/blog/2016/08/12/interactive-k-means/)). It visualizes probabilities for two-class classification (target vs. rest) using color gradient and contour lines, and it can do so for any Orange learner.

Here is an example workflow. The data comes from the [File](http://orange3.readthedocs.io/en/latest/widgets/data/file.html) widget. With no learner on input, the default is [Logistic Regression](http://orange3.readthedocs.io/en/latest/widgets/classify/logisticregression.html). Widget outputs learners _Coefficients,_ _Classifier (model)_ and _Learner._

![](/images/2016/08/poly-classification-flow.png)

Polynomial Classification widget works on two continuous features only, all other features are ignored. The screenshot shows plot of classification for an [Iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) .

![](/images/2016/08/polynomial-classification-1-stamped.png)

1. Set name of the learner. This is the name of learner on output.
2. Set features that logistic regression is performed on.
3. Set class that is classified separately from other classes.
4. Set the degree of a polynom that is used to transform an input data (1 means attributes are not transformed).
5. Select whether see or not contour lines in chart. The density of contours is regulated by _Contour step._



The classification for our case fails in separating Iris-versicolor from the other two classes. This is because logistic regression is a linear classifier, and because there is no linear combination of the chosen two attributes that would make for a good decision boundary. We can change that. Polynomial expansion adds features that are polynomial combinations of original ones. For example, if an input data contains features [a, b], polynomial expansion of degree two generates feature space [1, a, b, a2, a b, b2]. With this expansion, the classification boundary looks great.

![](/images/2016/08/polynomial-classification-2.png)



Polynomial Classification also works well with other learners. Below we have given it a [Classification Tree](http://orange3.readthedocs.io/en/latest/widgets/classify/classificationtree.html). This time we have painted the input data using [Paint Data](http://orange3.readthedocs.io/en/latest/widgets/data/paintdata.html), a great data generator used while learning about Orange and data science. The decision boundaries for the tree are all square, a well-known limitation for tree-based learners.

![](/images/2016/08/poly-classification-4e.png)



Polynomial expansion if high degrees may be dangerous. Following example shows overfitting when degree is five. See the two outliers, a blue one on the top and the red one at the lower right of the plot? The classifier was unnecessary able to separate the outliers from the pack, something that will become problematic when classifier will be used on the new data.

![](/images/2016/08/poly-classification-owerfit.png)

Overfitting is one of the central problems in machine learning. You are welcome to read our [previous blog on this problem and possible solutions](/blog/2016/03/12/overfitting-and-regularization/).
