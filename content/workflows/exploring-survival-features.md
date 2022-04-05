+++
title= "Exploring Survival Features"
images =  ["/workflow_images/710_survival_features.png"]
type = "workflows"
blog =  ""
video = ""
download = "710_survival_features.ows"
workflows = ["Survival Analysis", "Time-To-Event", "Kaplan-Meier", "Cox Regression"]
weight = 710
+++

In this workflow, we demonstrate how users can quickly explore features related to survival. We start the workflow with an initial screening of features by univariate Cox regression analysis. This step can help researchers decide which features, that is, features that impact survival might be interesting for further analysis. The Distribution widget shows the value distribution of the feature of interest. Interactively selecting patients in the distribution plot allows us to rapidly generate new groups of patients and observe the differences in the survival rate of corresponding groups in the Kaplan-Meier plot widget. 
