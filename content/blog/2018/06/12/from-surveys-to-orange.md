+++
author="AJDA"
date= '2018-06-12 07:54:17+00:00'
draft= false
title="From Surveys to Orange"
type="blog"
categories=["data" ,"dataloading" ,"orange3" ,"workshop" ]
tags=["data" ,"ministry" ,"questionnaire" ,"survey" ,"workshop" ]

+++

Today we have finished a series of workshops for the Ministry of Public Affairs. This was a year-long cooperation and we had many students asking many different questions. There was however one that we talked about a lot. If I have a survey, how do I get it into Orange?


**Related:** [Analyzing Surveys](/blog/2017/10/26/analyzing-surveys/)


![](/images/2018/06/IMG_20180611_120525.jpg)

We are using EnKlik Anketa service, which is a great Slovenian product offering a wide array of options for the creation of surveys. We have created one such simple survey to use as a test. I am now inside EnKlik Anketa online service and I can see my survey has been successfully filled out.

![](/images/2018/06/Screen-Shot-2018-06-11-at-15.44.48.png)

Now I have to create a public link to my survey in order to access the data in Orange. I have to click on an icon in the top right part and select 'Public link'.

![](/images/2018/06/Screen-Shot-2018-06-11-at-15.50.01.png)


A new window opens, where I select 'Add new public link'. This will generate a public connection to my survey results. But be careful, the type of the connection needs to be Data, not Analysis! Orange can't read already analyzed data, it needs raw data from Data pane.

![](/images/2018/06/Screen-Shot-2018-06-11-at-15.54.59.png)


Now, all I have to do is open Orange, place EnKlik Anketa widget from the Prototypes add-on onto the canvas, enter the public link into the 'Public link URL' fields and press Enter. If your data has loaded successfully, the widget will display available variables and information in the Info pane.

![](/images/2018/06/Screen-Shot-2018-06-11-at-15.59.01.png)

From here on you can continue your analysis just like you would with any other data source!

![](/images/2018/06/Screen-Shot-2018-06-12-at-09.46.23.png)
