+++
"title" = "Naive Bayes"
"icon" = "icons/naive-bayes.png"
"keywords" = "[]"
"category" = "Model"
+++
Naive Bayes
===========

A fast and simple probabilistic classifier based on Bayes' theorem with the assumption of feature independence.

**Inputs**

- Data: input dataset
- Preprocessor: preprocessing method(s)

**Outputs**

- Learner: naive bayes learning algorithm
- Model: trained model

**Naive Bayes** learns a [Naive Bayesian](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) model from the data. It only works for classification tasks.

![](/images/model/NaiveBayes-stamped.png)

This widget has two options: the name under which it will appear in other widgets and producing a report. The default name is *Naive Bayes*. When you change it, you need to press *Apply*.

Examples
--------

Here, we present two uses of this widget. First, we compare the results of the
**Naive Bayes** with another model, the [Random Forest](/widget-catalog/model/randomforest). We connect *iris* data from [File](/widget-catalog/data/file) to [Test & Score](/widget-catalog/evaluation/testandscore). We also connect **Naive Bayes** and [Random Forest](/widget-catalog/model/randomforest) to **Test & Score** and observe their prediction scores.

![](/images/model/NaiveBayes-classification.png)

The second schema shows the quality of predictions made with **Naive Bayes**. We feed the [Test & Score](/widget-catalog/evaluation/testandscore) widget a Naive Bayes learner and then send the data to the [Confusion Matrix](/widget-catalog/evaluation/confusionmatrix). We also connect [Scatter Plot](/widget-catalog/visualize/scatterplot) with **File**. Then we select the misclassified instances in the **Confusion Matrix** and show feed them to [Scatter Plot](/widget-catalog/visualize/scatterplot). The bold dots in the scatterplot are the misclassified instances from **Naive Bayes**.

![](/images/model/NaiveBayes-visualize.png)
