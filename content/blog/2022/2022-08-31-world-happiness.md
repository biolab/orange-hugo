+++
author = "Ajda Pretnar Žagar"
date = "2022-08-31"
draft = false
title = "Socio-economic data at your fingertips"
type = "blog"
thumbImage = "/blog_img/2022/2022-08-31_happy.png"
frontPageImage = "/blog_img/2022/2022-08-31_happy.png"
blog = ["data", "add-on", "widgets", "economy"]
shortExcerpt = "New World Happiness add-on joins the Orange family"
longExcerpt = "New World Happiness add-on for retrieving socio-economic data from the OECD database joins the Orange family"
+++

A new add-on has joined the Orange family! It is called World Happiness and it is intended for retrieving socio-econimic data from global databases. Go to Options --> Add-ons and select World Happiness from the list to install it.

{{< window-screenshot src="/blog_img/2022/2022-08-31_add-on.png" >}}

Currently, it contains a single wigdet - Socioeconomic Indices. But fret not! This one widget can do many things.

{{< window-screenshot src="/blog_img/2022/2022-08-31_widget.png" >}}

Say I wish to retrieve data for Europe and Central Asia, which I can select from the Countries list. I can go even further and filter by a specific country, but for now, let us go with the general region.

{{< window-screenshot src="/blog_img/2022/2022-08-31_country.png" >}}

Next, I can set which period I wish to retrieve the data for. Say the past five years, from 2017 to 2021. On the left side, you will see some parameters. They define how many missing values we permit in the data. The first is the percentage of missing values for the indicator, say forest area in square kilometers. If more than 60% of the indicator values are missing, the indicator will not appear on the output. Similarly for the country - if more than 90% of the values are missing, the country will not appear on the output. Finally, the values will be aggregated by mean, meaning each year for each country will display an average indicator value.

{{< window-screenshot src="/blog_img/2022/2022-08-31_period.png" >}}

Finally, I will select the indicator I wish on the output. Say I am interested in forestry. I type "forest" in the filter. Only the indicators containing the word "forest" will be displayed below. Now, I select the desired indicator to send to the output. I will select all of them.

{{< window-screenshot src="/blog_img/2022/2022-08-31_filter.png" >}}

To actually send the indicators to the output, I have to move them to the selected indicators section, which is the final box in the lower right corner. If the retrieval was successful, you will see a number in the status bar at the bottom of the widget. I have retrieved 47 rows of data.

{{< window-screenshot src="/blog_img/2022/2022-08-31_indicators.png" >}}

I can observe the data in the Data Table. Each row represents a country and each column an indicator. Now I can sort the data in the Data Table, observe means and medians in Box Plot, cluster countries based on given indicators and so on.

{{< window-screenshot src="/blog_img/2022/2022-08-31_data-table.png" >}}

Enjoy exploring the data and let us know if you discover something interesting!

{{< window-screenshot src="/blog_img/2022/2022-08-31_workflow.png" >}}
