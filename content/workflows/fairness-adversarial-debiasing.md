+++
title= "Adversarial Debiasing"
images =  ["/workflows/images/fairness-adversarial-debiasing.png"]
type = "workflows"
blog_link =  "/blog/2023/2023-08-28-fairness-adversarial-debiasing/"
video = ""
download = "fairness-adversarial-debiasing.ows"
workflows = ["Fairness"]
weight = 1003
+++

The easiest method to address bias in machine learning is to use a bias-aware model. This approach eliminates the need for fairness preprocessing or postprocessing. In this workflow, we will employ a bias-aware model named Adversarial Debasing for classification. We will train two versions of this model: one with and one without debiasing. Finally, we will compare and display the fairness metrics using a box plot widget.