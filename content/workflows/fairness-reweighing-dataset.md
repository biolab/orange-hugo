+++
title= "Reweighing a Dataset"
images =  ["/workflows/images/fairness-reweighing-dataset.png"]
type = "workflows"
blog_link =  "/blog/2023/2023-08-24-fairness-reweighing-dataset/"
video = ""
download = "fairness-reweighing-dataset.ows"
workflows = ["Fairness"]
weight = 1001
+++

Detecting bias is only the first step in ensuring fair machine learning. The next step is to mitigate the bias. This workflow illustrates removing bias at the dataset level using the Reweighing widget. Initially, split the data into training and validation subsets. We then check for bias in the validation set before reweighing. Using the training set, we train the reweighing algorithm and apply it to the validation set. Finally, we check for bias in the reweighed validation set. We can also visualize the effect of the reweighing using a Box Plot.