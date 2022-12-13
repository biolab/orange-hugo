+++
author = "Noah Novšak"
date = "2022-12-13"
draft = false
title = "Orange you going to ask about dask"
type = "blog"
thumbImage = "/blog_img/2022/2022-12-13_dask_data.png"
frontPageImage = "/blog_img/2022/2022-12-13_dask_data.png"
blog = ["dask", "widgets"]
shortExcerpt = "Preparing Orange to handle much more data."
longExcerpt = "A note on using dask to deal with more and more data with Orange."
+++

As great as Orange is at simplifying machine learning and bringing it closer to your [everyday regular normal guy](https://www.youtube.com/watch?v=5PsnxDQvQpw), it turns out, there are some major drawbacks that stem from it's very inception. This is because Orange is meant to be run on a laptop. A device with just a handful of CPU cores, and maybe a couple of gigabytes of RAM. Due to this ideology we have so far reasoned that nobody in their right mind would want to throw a very large dataset at it. So most of Orange's components assume they can fit all the data into memory at once, process it on a single core, and expect results fairly quickly.

You might see an issue here. What happens if I give Orange more data than my poor old laptop can handle?

The solution to our problem is [dask](https://www.dask.org). Another open-source library that enables efficient scaling of python code. As such, a project is currently under way, that aims to implement dask into Orange. So here I am today, to illustrate the changes that are coming to Orange in the near future.

One particularly fun issue I've been working on recently presents itself in Orange's most commonly used widget, the [Data Table](/widget-catalog/data/datatable/). As it stands Orange keeps all the data it's processing in memory. This means it's readily available and easy to use with little to no overhead. However, the downside of this is that we assume all the data _can_ and _must_ be stored in such a way.

{{% figure src="/blog_img/2022/2022-12-13_dask_window.png" %}}

The first steps to fixing these unjust assumptions have already been implemented under the hood. We have created a new way to store data using dask. The main advantage here is that instead of forcing all the data into memory we can instead, keep it on our hard drive until actually required for processing. And even then it won't be read all at once, but in manageable chunks. While this is sounds great, tying it into Data Table directly poses more issues. Accessing data from the hard drive can of course be very slow.

One important disticntion, as we move towards storing data on a hard drive, is that more than processing the data, the bottleneck tends to be _reading_ the data in the first place. So while the simplest method to present a table stored in memory is to read each cell, one by one, and disply it, we see a marked performance increase if we instead, read the data from our hard drive in _chunks_. 

{{% figure src="/blog_img/2022/2022-12-13_dask_chunking.png" %}}

This approach does have another drawback though. Previously each element took an equal amount of time to read and display. Now we can quickly display everything from the chunk, but when we scroll past the edge of the chunk and nead to read a new one we have to wait a little while. This causes an uneven stuttering when scrolling, which is very unpleasant.

Luckily, there's a simple solution for this one too. If I want to achieve a smoother scroll I have to let the table continue scrolling past the edge of my chunk, even though I don't know what it's supposed to display yet. Instead temporarily showing some empty cells while I ask dask to read the next chunk for me in the background. Once dask is finished preparing my data I can refresh my table with the actual values.

This aproach actually ends up working surprisingly well. Now I can (in theory) use Orange to display arbitrarily large datasets without unwanted crashes or obscenely long wait times. It was also amazingly simple to implement, due to how well dask integrates with existing numpy code.
