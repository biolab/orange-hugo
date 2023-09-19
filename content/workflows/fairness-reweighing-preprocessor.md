+++
title= "Reweighing as a preprocessor"
images =  ["/workflows/images/fairness-reweighing-preprocessor.png"]
type = "workflows"
blog_link =  "/blog/2023/2023-09-19-fairness-reweighing-preprocessor/"
video = ""
download = "fairness-reweighing-preprocessor.ows"
workflows = ["Fairness"]
weight = 1002
+++

We can use the reweighing fairness algorithm for more than just adding weights to a dataset. It can also be used as a preprocessor for a specific model. This workflow illustrates how to use the Reweighing widget as a preprocessor for the Logistic Regression model. Initially, we load the dataset and input it into the Test and Score widget, which we will use to evaluate our model. Now, we need to connect a Logistic Regression model, which has the Reweighing widget as a preprocessor, to the Test and Score widget. Doing so ensures our data gets reweighed before the model learns from it. We compare these results against those derived from a Logistic Regression model without reweighing and visualize both using a Box Plot.