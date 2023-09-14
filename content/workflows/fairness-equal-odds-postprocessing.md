+++
title= "Equal Odds Postprocessing"
images =  ["/workflows/images/fairness-equal-odds-postprocessing.png"]
type = "workflows"
blog_link =  "/blog/2023/2023-08-30-fairness-equal-odds-postprocessing/"
video = ""
download = "fairness-equal-odds-postprocessing.ows"
workflows = ["Fairness"]
weight = 1004
+++

Another way to mitigate bias is to use a postprocessing algorithm on the model's predictions. This workflow illustrates using the Equal Odds widget as a post-processor for the Logistic Regression model. To use the post-processor, we need to connect any model to the Equalized Odds Postprocessing widget along with any needed pre-processors. Doing so ensures our model's predictions get post-processed before we evaluate them.