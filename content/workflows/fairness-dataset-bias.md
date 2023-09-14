+++
title= "Dataset Bias Examination"
images =  ["/workflows/images/fairness-dataset-bias.png"]
type = "workflows"
blog_link =  "/blog/2023/2023-08-23-fairness-dataset-bias/"
video = ""
download = "fairness-dataset-bias.ows"
workflows = ["Fairness"]
weight = 1000
+++

Understanding the potential biases within datasets is crucial for fair machine-learning outcomes. This workflow detects dataset bias using a straightforward algorithm. After loading the dataset, we add specific fairness attributes to it, which are essential for our calculations. We then compute the fairness metrics via the Dataset Bias widget and explain the results in a Box Plot.