+++
author="AJDA"
date= '2017-08-04 11:41:33+00:00'
draft= false
title="'Text Analysis: New Features'"
type="blog"
categories=["analysis" ,"dataloading" ,"examples" ,"features" ,"orange3" ,"release"  ,"text mining" ,"version" ,"widget" ,"workshop" ]
tags=["import documents" ,"import text" ,"sentiment analysis" ,"text" ,"text mining"
  ,"textual analysis" ,"topic modelling" ]

+++

As always, we've been working hard to bring you new functionalities and improvements. Recently, we've released Orange version 3.4.5 and Orange3-Text version 0.2.5. We focused on the Text add-on since we are lately holding a lot of text mining workshops. The next one will be at Digital Humanities 2017 in Montreal, QC, Canada in a couple of days and we simply could not resist introducing some sexy new features_._


**Related:** [Text Preprocessing](https://blog.biolab.si/2017/06/19/text-preprocessing/)




**Related:** [Rehaul of Text Mining Add-On](https://blog.biolab.si/2016/07/05/rehaul-of-text-mining-add-on/)


First, Orange 3.4.5 offers better support for Text add-on. What do we mean by this? Now, every core Orange widget works with Text smoothly so you can mix-and-match the widgets as you like. Before, one could not pass the output of Select Columns (data table) to Preprocess Text (corpus), but now this is no longer a problem.

[![](/images/2017/08/Screen-Shot-2017-08-04-at-13.33.28.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-13.33.28.png)

Of course, one still needs to keep in mind that Corpus is a sparse data format, which does not work with some widgets by design. For example, Manifold Learning supports only t-SNE projection.

[![](/images/2017/08/Screen-Shot-2017-08-04-at-10.37.03.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-10.37.03.png)



Second, we've introduced two new widgets, which have been long overdue. One is Sentiment Analysis, which enables basic sentiment analysis of corpora. So far it works for English and uses two nltk-supported techniques - [Liu Hu](https://www.cs.uic.edu/~liub/publications/kdd04-revSummary.pdf) and [Vader](http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf). Both techniques are lexicon-based. Liu Hu computes a single normalized score of sentiment in the text (negative score for negative sentiment, positive for positive, 0 is neutral), while Vader outputs scores for each category (positive, negative, neutral) and appends a total sentiment score called a compound.

[![](/images/2017/08/Screen-Shot-2017-08-04-at-11.00.25.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-11.00.25.png) Liu Hu score.

[![](/images/2017/08/Screen-Shot-2017-08-04-at-10.59.57.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-10.59.57.png) Vader scores.



Try it with Heat Map to visualize the scores.

[![](/images/2017/08/Screen-Shot-2017-08-04-at-11.05.23.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-11.05.23.png)

[![](/images/2017/08/Screen-Shot-2017-08-04-at-11.05.19.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-11.05.19.png) Yellow represent a high, positive score, while blue represent a low, negative score. Seems like Animal Tales are generally much more negative than Tales of Magic.



The second widget we've introduced is Import Documents. This widget enables you to import your own documents into Orange and outputs a corpus on which you can perform the analysis. The widget supports .txt, .docx, .odt, .pdf and .xml files and loads an entire folder. If the folder contains subfolders, they will be considered as class values. Here's an example.

[![](/images/2017/08/Screen-Shot-2017-08-04-at-11.11.17.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-11.11.17.png)

This is the structure of my Kennedy folder. I will load the folder with Import Documents. Observe, how Orange creates a class variable _category_ with _post-1962_ and _pre-1962_ as class values.

[![](/images/2017/08/Screen-Shot-2017-08-04-at-11.15.01.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-11.15.01.png)

[![](/images/2017/08/Screen-Shot-2017-08-04-at-11.15.14.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-11.15.14.png) Subfolders are considered as class in the category column.



Now you can perform your analysis as usual.

[![](/images/2017/08/Screen-Shot-2017-08-04-at-11.15.44.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-11.15.44.png)



Finally, some widgets have cool new updates. Topic Modelling, for example, colors words by their weights - positive weights are colored green and negative red. Coloring only works with LSI, since it's the only method that outputs both positive and negative weights.

[![](/images/2017/08/Screen-Shot-2017-08-04-at-11.31.51.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-11.31.51.png)

[![](/images/2017/08/Screen-Shot-2017-08-04-at-12.23.24.png)
](https://blog.biolab.si/wp-content/uploads/2017/08/Screen-Shot-2017-08-04-at-12.23.24.png) If there are many kings in the text and no birds, then the text belongs to Topic 2. If there are many children and no foxes, then it belongs to Topic 3.



Take some time, explore these improvements and let us know if you are happy with the changes! You can also submit new feature requests to our [issue tracker](https://github.com/biolab/orange3-text/issues).



Thank you for working with Orange! 🍊
