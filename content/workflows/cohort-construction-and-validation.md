+++
title= "Cohort Construction and Validation"
images =  ["/workflow_images/720_cohort_construction_and_validation.png"]
type = "workflows"
blog =  ""
video = ""
download = "720_cohort_construction_and_validation.ows"
workflows = ["Survival Analysis", "Time-To-Event", "Kaplan-Meier", "Cox Regression"]
weight = 720
+++

Stratification of patients into low and high-risk groups is a common task in survival analysis to identify clinical and biological factors that contribute to survival. One approach to stratification is by computing risk score values based on the Cox regression model. With the clever use of Orange widgets, we can split the data into training and validation sets and then interactively generate risk score models on training data to observe the difference in cohorts' survival rate on training and validation samples side-by-side. Read more on how [Apply domain]({{< ref "../blog/2021/2021-08-13-apply-domain.md" >}} "Apply domain") enables this kind of workflows.
