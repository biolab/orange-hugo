+++
title= "Hiding Protected Attribute"
images =  ["/workflows/images/fairness-hiding-protected-attribute.png"]
type = "workflows"
blog_link =  "/blog/2023/2023-08-31-fairness-hiding-protected-attribute/"
video = ""
download = "fairness-hiding-protected-attribute.ows"
workflows = ["Fairness"]
weight = 1005
+++

Why would we use fairness algorithms instead of simply removing the protected attribute to avoid bias? This workflow illustrates why that is not such a good idea. We compare the predictions of a model using Reweighing to those of a model on data with the protected attribute removed. We use Box Plot to visualize and compare common fairness metrics.