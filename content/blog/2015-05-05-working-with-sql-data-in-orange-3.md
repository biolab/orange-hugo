+++
author="LAN"
date= '2015-05-05 07:20:47+00:00'
draft= false
title="Working with SQL data in Orange 3"
type="blog"
categories=["orange3" ]
tags=["axle" ,"orange3" ,"sql" ,"visualization" ]

+++

[Orange 3](http://orange.biolab.si/orange3/) is slowly, but steadily, gaining support for working with data stored in a SQL database. The main focus is to allow huge data sets that do not fit into RAM to be analyzed and visualized efficiently. Many widgets already recognize the type of input data and perform the necessary computations intelligently. This means that data is not downloaded from the database and analyzed locally, but is retained on the remote server, with the computation tasks translated into SQL queries and offloaded to the database engine. This approach takes advantage of the state-of-the-art optimizations relational databases have for working with data that does not fit into working memory, as well as minimizes the transfer of required information to the client.

We demonstrate how to explore and visualize data stored in a SQL table on a remote server in the following short video. It shows how to connect to the server and load the data with the SqlTable widget, manipulate the data (Select Columns, Select Rows), obtain the summary statistics (Box plot, Distributions), and visualize the data (Heat map, Mosaic Display).



https://youtu.be/MhC2ckTnEgU



_The research leading to these results has received funding from the European Union’s Seventh Framework Programme (FP7/2007-2013) under grant agreement no 318633_


