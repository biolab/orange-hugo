+++
author="AJDA"
date= '2017-10-26 11:03:10+00:00'
draft= false
title="Analyzing Surveys"
type="blog"
blog=["analysis" ,"clustering" ,"data" ,"dataloading" ,"orange3" ,"visualization"  ,"workshop" ]
+++

Our streak of workshops continues. This time we taught professionals from public administration how they can leverage data analytics and machine learning to retrieve interesting information from surveys. Thanks to the [Ministry of Public Administration](http://www.mju.gov.si/en/), this is only the first in a line of workshops on data science we are preparing for public sector employees.

![](/images/2017/10/FRI_2422.jpg)

For this purpose, we have designed EnKlik Anketa widget, which you can find in Prototypes add-on. The widget reads data from a Slovenian online survey service [OneClick Survey](http://english.1ka.si/) and imports the results directly into Orange.

We have prepared a test survey, which you can import by entering a public link to data into the widget. Here's the link: [https://www.1ka.si/podatki/141025/72F5B3CC/](https://www.1ka.si/podatki/141025/72F5B3CC/) . Copy it into the Public link URL line in the widget. Once you press Enter, the widget loads the data and displays retrieved features, just like the File widget.

![](/images/2017/10/Screen-Shot-2017-10-26-at-12.29.10.png)
EnKlik Anketa widget is similar to the File widget. It also enables changing the attribute type and role.



The survey is in Slovenian, but we can use Edit Domain to turn feature names into English equivalent.

![](/images/2017/10/Screen-Shot-2017-10-26-at-12.30.53.png)

We renamed attributes in order as they appear in the survey. If you load the survey yourself, you can rename them just like you see here.



As always, we can check the data in a Data Table. We have 41 respondents and 7 questions. Each respondent chose a nickname, which makes it easier to browse the data.

![](/images/2017/10/Screen-Shot-2017-10-26-at-12.33.25.png)

Now we can perform familiar clustering to uncover interesting groups in our data. Connect Distances to Edit Domain and Hierarchical Clustering to Distances.

![](/images/2017/10/Screen-Shot-2017-10-26-at-12.36.26.png)

Distance from Pipi and Chad to other respondents is very high, which makes them complete outliers.



![](/images/2017/10/Screen-Shot-2017-10-26-at-12.36.46.png)

We have two outliers, Pipi and Chad. One is an excessive sportsman (100 h of sport per week) and the other terminally ill (general health -1). Or perhaps they both simply didn't fill out the survey correctly. If we use the Data Table to filter out Pipi and Chad, we get a fairly good clustering.

![](/images/2017/10/Screen-Shot-2017-10-26-at-12.41.01.png)

We can use Box Plot, to observe what makes each cluster special. Connect Box Plot to Hierarchical Clustering (with the two groups selected), select grouping by_ Cluster_ and tick _Order by relevance_.

![](/images/2017/10/Screen-Shot-2017-10-26-at-12.41.50.png)
Box Plot separates distributions by Cluster and orders attributes by how well they split selected subgroups.



![](/images/2017/10/Screen-Shot-2017-10-26-at-12.45.32.png)

The final workflow.



Seems like our second cluster (C2) is the sporty one. If we are serving in the public administration, perhaps we can design initiatives targeting cluster C1 to do more sports. It is so easy to analyze the data in Orange!
