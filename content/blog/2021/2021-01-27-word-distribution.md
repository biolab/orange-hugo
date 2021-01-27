+++
author = "Ajda Pretnar"
date = "2021-01-27"
draft = false
title = "Observing Word Distribution"
type = "blog"
thumbImage = "/blog_img/2021/2021-01-27-word-distribution-small.png"
frontPageImage = "/blog_img/2021/2021-01-27-word-distribution-small.png"
blog = ["text mining", "word distribution", "bar plot", "word cloud"]
shortExcerpt = "How to inspect word distribution in a corpus with in Orange."
longExcerpt = "How to inspect word distribution in a corpus with a clever combination of widgets in Orange."
x2images = true  # true if using retina screenshots, else false
+++

In text mining, one of key tasks is understanding and inspecting the corpus. It makes it easier to determine the preprocessing techniques and downstream analysis (the selection of document frequency weights, topic modelling technique, lemmatization and so on).

Even though Orange sometimes doesn't have a widget for a specific task, the said task can be achieved with a combination of widgets and their outputs. Let us look at an example of word distribution. There is no such widget in Orange, but word distributions are generally available in [Word Cloud](https://orangedatamining.com/widget-catalog/text-mining/wordcloud/). Word Cloud shows a list of most frequent words and their frequencies on the left and a cloud visualization on the right.

{{% workflow-screenshot src="/blog_img/2021/2021-01-27-word-cloud.png" %}}

This is a great start, but Word Cloud only shows the 100 words and the visualization doesn't directly correspond to the word frequency (words are scaled so that very frequent words don't overwhelm less frequent ones). Yet Word Cloud has an output called **Word Counts**, which outputs a table with words and their frequencies in columns. Just what we would like to see!

{{% workflow-screenshot src="/blog_img/2021/2021-01-27-data-table.png" %}}

Can we see these frequencies as distributions? Yes, we can. A general widget showing numeric values (such as word counts) is [Bar Plot](https://orangedatamining.com/widget-catalog/visualize/barplot/). We pass the Word Counts output of Word Cloud to Bar Plot. We can also label each bar by setting Annotations to Word.

{{% workflow-screenshot src="/blog_img/2021/2021-01-27-bar-plot.png" %}}

If we zoom in, we can see that "the", "and", "of", "to", "a" are by far the most frequent words. This calls for some preprocessing, particularly stopword removal. We place [Preprocess Text](https://orangedatamining.com/widget-catalog/text-mining/preprocesstext/) between Corpus and Word Cloud and use default preprocessing. Our bar plot has changed. Now, the most frequent word is "said", so perhaps another round of stopword removal is necessary.

{{% workflow-screenshot src="/blog_img/2021/2021-01-27-word-distribution.png" %}}

{{% workflow-screenshot src="/blog_img/2021/2021-01-27-workflow.png" %}}

Orange widgets are intended to be as general as possible, which it easy to stack them into custom workflows. Don't forget to explore all the outputs different widgets offer, for example the [All Topics](https://orangedatamining.com/widget-catalog/text-mining/topicmodelling-widget/) output from Topic Modelling, [Concordances](https://orangedatamining.com/widget-catalog/text-mining/concordance/) from Concordance, or [Grouped Data](https://orangedatamining.com/blog/2019/2019-08-27-pivot-table/) from Pivot Table.
