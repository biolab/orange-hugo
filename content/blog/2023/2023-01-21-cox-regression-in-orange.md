+++
author = "Jaka Kokošar"
date = "2023-01-21"
draft = false
title = "Cox regression in Orange"
type = "blog"
thumbImage = "/blog_img/2023/2023-01-21-cox-test-and-score.png"
frontPageImage = "/blog_img/2023/2023-01-21-cox-test-and-score.png"
blog = ["survival analysis", "cox regression"]
shortExcerpt = "Orange built-in methods for testing and scoring the predictive models now support survival-related models like Cox regression."
longExcerpt = "Orange built-in methods for testing and scoring the predictive models now support survival-related models like Cox regression."
+++

In our [previous blog post]({{< ref "/blog/2022/2022-05-25-KaplanMeier.md" >}}), we discussed the basic concepts of survival analysis, the types of problems it aims to solve and briefly introduced the Kaplan-Meier method. We used the [Kaplan-Meier widget](/widget-catalog/survival-analysis/kaplan-meier-plot/) to estimate a population's survival probability over time, taking into account a specific covariate. However, we did not account for the impact of other covariates on the survival outcome.

When studying patient outcomes in clinical settings, it is essential to consider multiple factors that describe patients' conditions and may affect survival. The Cox regression model is widely used in survival analysis. It estimates the hazard ratio of an event of interest while adjusting for the effect of included covariates. For those more interested, we suggest the article by [Bradburn et al.](https://www.nature.com/articles/6601119) on the topic of analyzing survival data with multiple covariates.

{{< window-screenshot src="/blog_img/2023/2023-01-21-cox-regression.png" >}}

The illustration above demonstrates how to perform a Cox regression analysis by linking the German Breast Cancer Study Group 2 data from the **Datasets** widget to the [Cox regression widget](/widget-catalog/survival-analysis/cox-regression/) and displaying the results in a **Data table**. The documentation of [Lifelines](https://lifelines.readthedocs.io/en/latest/Survival%20Regression.html#interpretation), the python library utilized by the survival widgets in Orange, provides a clear explanation of how to interpret the presented results.

The survival analysis [add-on](https://github.com/biolab/orange3-survival-analysis/) in Orange seamlessly integrates with the rest of the widgets, enabling the construction of standard Orange workflows. For example, in the image below, we demonstrate how we can use the cross-validation strategy to test and score the Cox regression model based on the Concordance index as a measure of predictive accuracy.

{{< window-screenshot src="/blog_img/2023/2023-01-21-cox-test-and-score.png" >}}
