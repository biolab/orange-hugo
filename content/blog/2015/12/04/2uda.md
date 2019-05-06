+++
author="LAN"
date= '2015-12-04 07:20:12+00:00'
draft= false
title="2UDA"
type="blog"
categories=["sql" ]
tags=["2uda" ,"postgresql" ,"psycopg2" ]

+++

In one of the [previous blog posts](/blog/2015/10/19/sql-for-orange/) we mentioned that installing the optional dependency _psycopg2_ allows Orange to connect to [PostgreSQL](http://www.postgresql.org/) databases and work directly on the data stored there.
It is also possible to transfer a whole table to the client machine, keep it in the local memory, and continue working with it as with any other Orange data set loaded from a file. But the true power of this feature lies in the ability of Orange to leave the bulk of the data on the server, delegate some of the computations to the database, and transfer only the needed results. This helps especially when the connection is too slow to transfer all the data and when the data is too big to fit in the memory of the local machine, since SQL databases are much better equipped to work with large quantities of data residing on the disk.

If you want to test this feature it is now even easier to do so! A third party distribution called [**2UDA**](http://2ndquadrant.com/2uda) provides a single installer for all major OS platforms that combines Orange and a PostgreSQL 9.5 server along with LibreOffice (optional) and installs all the needed dependencies. The database even comes with some sample data sets that can be used to start testing and using Orange out of the box. 2UDA is also a great way to get the very latest version of PostgreSQL, which is important for Orange as it relies heavily on its new [TABLESAMPLE](http://blog.2ndquadrant.com/tablesample-in-postgresql-9-5-2/) clause. It enables time-based sampling of tables, which is used in Orange to get approximate results quickly and allow responsive and interactive work with big data.

We hope this will help us reach an even wider audience and introduce Orange to a whole new group of people managing and storing their data in SQL databases. We believe that having lots of data is a great starting point, but the benefits truly kick in with the ability to easily extract useful information from it.

![](/images/2015/12/2uda-final-logo_thumbnail.jpg)
