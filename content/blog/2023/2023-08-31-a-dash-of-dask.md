+++
author = "Noah Novšak"
date = "2023-08-31"
draft = false
title = "A dash of Dask"
type = "blog"
thumbImage = "/blog_img/2023/2023-08-31-dask-logistic-regression.png"
frontPageImage = "/blog_img/2023/2023-08-31-dask-logistic-regression.png"
blog = ["dask", "development"]
shortExcerpt = "Updates in the dask project, integrating machine learning methods and enhancing efficiency in a data preprocessor."
longExcerpt = "Updates in the dask project, integrating machine learning methods and enhancing efficiency in a data preprocessor."
+++

It's been a while since our last progress update on [Dask](/blog/2022/2022-12-13-dask-table), and quite a bit has happened since. Most noticeably, we've got some more visualization widgets working, but I leave that for another blog post. Today, I want to focus on our updated machine-learning methods. K-Means, PCA, Naive Bayes, Linear, and Logistic Regression are now running. Well, maybe not flawlessly, but hey, they work.

Currently, most of Orange's learners wrap existing scikit-learn methods. Extending them to support Dask was as simple as making a helper function that switches between the `sklearn` and `dask_ml` implementations depending on the data received (with a couple of caveats).

Ideally, this kind of data handling should be separate from the canvas and widgets. Both to facilitate development and to not obtrude the end user. Also, we need the learners to maintain backward compatibility because Orange is quite a large project. These requirements mean some *magic* has to be done behind the scenes to account for the subtle differences between scikit-learn and dask-ml. So, to anyone trying to use one of the learners mentioned above in unpredicted ways, you have been warned.

Additionally some decisions had to be made about when to compute certain operations and what we can and should store in memory. Consider, for example, the experience I went through when implementing some of the described changes in logistic regression.

I was running some tests to ensure everything worked fine, but they took quite a while to finish. It was not all that surprising as I was processing a large amount of data, but I still wondered if I wasn't waiting a little _too_ long.  So I thought, 'Maybe I've made a mistake'. I decided to go through every computation phase painstakingly and ensure nothing took an unreasonable amount of time. After a while, I happened upon a preprocessor that, at first glance, was doing little computing but was taking inordinately long to finish! The preprocessor in question is called `RemoveNaNColumns`, and its job is to eliminate columns with too many missing values like so:

```python
nans = np.sum(np.isnan(data.X), axis=0)
att = [a for a, n in zip(data.domain.attributes, nans) if n < threshold]
```

This specific bit of code has yet to be touched up to work with Dask, but interestingly, it still works. Typically, it would sum up the number of unknown values along the 0-th axis, then loop through them, removing attributes with too many. The catch with Dask is that we only compute the first part of this process when necessary. Since the first part is vectorized and the second isn't, the entire calculation (summing up the `NaN` values for all columns) is performed repeatedly in each iteration slowing the process down substantially.

The ideal solution would be to vectorize the second part, but sadly, that is not something I know how to do with Python lists. So we are left with option one, doing the first part in a loop, or option two, computing the first part ahead of time and storing the results in memory. Here's an example of how each of these approaches might look.

```python
# option 1
att = [a for i, a in enumerate(data.domain.attributes)
       if np.sum(np.isnan(data.X[:, i])) < threshold]

# option 2
nans = np.asarray(np.sum(np.isnan(data.X), axis=0))
att = [a for a, n in zip(data.domain.attributes, nans) if n < threshold]
```

In theory, option one should have a more minor memory impact, and one may prefer a version of it under certain circumstances. However, accessing data from the hard drive is slow, even more so when only reading small pieces at a time. Option two has an advantage because it can access all the data it requires more smartly while using vectorization. The only downside is that we must store a temporary array in memory. Regardless, this is the approach we've opted to use going forward, prioritizing computation speed under the assumption that these temporary arrays are manageable.

This decision is a good illustration of what we aim to achieve with Dask and how. While you may consider committing an intermediate array to memory unappealing and contradictory to using dask to help orange scale, you should also look at the bigger picture. The main goal of this project is not to handle *big data* but *bigger* data. Essentially, we would like to transition from assuming all the data fits comfortably into memory to storing just a single column or row at a time. Going beyond that would require fundamental architectural changes and significant hardware upgrades to your laptop.
