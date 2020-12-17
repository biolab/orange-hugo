+++
author="Ajda Pretnar"
date= '2019-05-18'
draft= false
title="Business Case Studies with Orange"
type="blog"
thumbImage = "/blog_img/2019/5/18/wartsila-blog.jpg"
blog=["business intelligence", "HR", "logistic regression", "nomogram", "predictive models"]
shortExcerpt = "At the latest workshop we demonstrated how to predict, which employees are most likely to resign in the future."

longExcerpt = "At the latest workshop in Italy we taught the participants how to identify relevant business use cases and how to predict, which employees are most likely to resign in the future."
+++

Previous week Blaž, Robert and I visited Wärtsilä in the lovely Dolina near Trieste, Italy. {{< link_new url="https://www.wartsila.com/" name="Wärtsilä">}} is one of the leading designers of lifecycle power solutions for the global marine and energy markets and its {{< link_new url="https://www.wartsila.com/ita/en/about" name="subsidiary in Trieste">}} is one of the largest Wärtsilä Group engine production plants. We were there to hold a one-day workshop on data mining and machine learning with the aim to identify relevant use cases in business and show how to address them.

\

{{% figure src="/blog_img/2019/5/18/business-case-1.png" %}}
\
\

Related: {{< link_new url="/blog/2017/11/17/data-mining-business-public-administration/" name="Data Mining for Business and Public Administration">}}

One such important use case is employee attrition. It is vital for any company to retain its most valuable workers, so they must learn how to identify dissatisfied employees and provide incentive from the to stay. It is easy to construct a workflow in Orange that helps us with this.

First, let us load Attrition – Train data set from the Datasets widget. This is a synthetic data set from IBM Watson that has 1470 instances (employees) and 18 features describing them. Our target variable is Attrition, where Yes means the person left the company and No means it stayed.


\


{{% figure src="/blog_img/2019/5/18/business-case-2.png" width="70%"%}}
\
\

Now our goal is to construct a predictive model that will successfully predict the likelihood of a person leaving. Let us connect a couple of classifiers and the data set to Test and Score and see which model performs best.


\

{{% figure src="/blog_img/2019/5/18/business-case-3.png" width="60%"%}}
\
\
Seems like Logistic Regression is the winner here, since its AUC score it the highest of the three.

\


{{% figure src="/blog_img/2019/5/18/business-case-4.png" width="80%" %}}
\
\
A great thing about Logistic Regression is that it is interpretable. We can connect the data from Datasets to Logistic Regression and the resulting model from LR to Nomogram. Nomogram shows the top ten features, ranked by their contribution to the final probability of a class.


\


{{% figure src="/blog_img/2019/5/18/business-case-5.png" width="60%" %}}
\
\

The length of a line corresponds to the relative importance of the attribute. Seems like recently hired employees are more likely to leave (YearsAtCompany goes towards 0). We also should consider promoting those that haven’t been promoted in a while (YearsSinceLastPromotion goes towards 15) and cut the overtime (OverTime is Yes). Model inspection helps us identify relevant attributes and interpret their values. So useful for HR departments!

\


{{% figure src="/blog_img/2019/5/18/business-case-6.png" width="50%"%}}
\
\

Finally, we can take new data and predict the likelihood for leaving. Put another Datasets on the canvas and load Attrition – Predict data. This one contains only three instances – say the data for three employees we have forgotten to consider in our training data.

\


{{% figure src="/blog_img/2019/5/18/business-case-7.png" width="80%"%}}
\
\

So who is more likely to leave? We obviously cannot afford to promote everyone, because this costs money. We need to optimize our decisions so that we both increase the satisfaction of employees while keep our costs low. This is where we can use predictive modeling. Connect Logistic Regression to Predictions widget. Then connect the second Datasets widget with the new data to Predictions as well.


\


{{% figure src="/blog_img/2019/5/18/business-case-8.png" width="50%"%}}
\
\
Seems like John is most likely to leave. He has been at the company for only a year and he works overtime.

\


{{% figure src="/blog_img/2019/5/18/business-case-9.png" width="80%"%}}
\
\

This is something HR department can work with to design proper policies and keep best talent. The same workflow can be used for churn prediction, process optimization and predicting success of a new product.

