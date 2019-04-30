+++
author="AJDA"
date= '2017-06-19 08:04:03+00:00'
draft= false
title="Text Preprocessing"
type="blog"
categories=["orange3" ,"preprocessing" ,"text mining" ,"visualization" ]
tags=["grimms tales" ,"preprocess" ,"preprocessing" ,"text analytics" ,"text mining"
  ,"word cloud" ]

+++

In data mining, preprocessing is key. And in text mining, it is the key and the door. In other words, it's the most vital step in the analysis.


**Related:** [Text Mining add-on](/blog/2016/07/05/rehaul-of-text-mining-add-on/)


So what does preprocessing do? Let's have a look at an example. Place Corpus widget from Text add-on on the canvas. Open it and load _Grimm-tales-selected_. As always, first have a quick glance of the data in Corpus Viewer. This data set contains 44 selected [Grimms' tales](https://en.wikipedia.org/wiki/Grimms%27_Fairy_Tales).

![](/images/2017/06/Screen-Shot-2017-06-19-at-09.45.48.png)

Now, let us see the most frequent words of this corpus in a Word Cloud.

![](/images/2017/06/Screen-Shot-2017-06-19-at-09.46.29.png)

Ugh, what a mess! The most frequent words in these texts are conjunctions ('and', 'or') and prepositions ('in', 'of'), but so they are in almost every English text in the world. We need to remove these frequent and uninteresting words to get to the interesting part. We remove the punctuation by defining our tokens. [Regexp](https://en.wikipedia.org/wiki/Regular_expression) _\w+_ will keep full words and omit everything else. Next, we filter out the uninteresting words with a list of stopwords. The [list](https://gist.github.com/sebleier/554280) is pre-set by nltk package and contains frequently occurring conjunctions, prepositions, pronouns, adverbs and so on.

![](/images/2017/06/Screen-Shot-2017-06-19-at-09.48.01.png)

Ok, we did some essential preprocessing. Now let us observe the results.

![](/images/2017/06/Screen-Shot-2017-06-19-at-09.49.27.png)

This _does_ look much better than before! Still, we could be a bit more precise. How about removing the words could, would, should and perhaps even said, since it doesn't say much about the content of the tale? A custom list of stopwords would come in handy!

Open a plain text editor, such as Notepad++ or [Sublime](https://www.sublimetext.com/), and place each word you wish to filter on a separate line.

![](/images/2017/06/Screen-Shot-2017-06-19-at-09.50.30.png)

Save the file and load it next to the pre-set stopword list.

![](/images/2017/06/Screen-Shot-2017-06-19-at-09.48.11.png)

One final check in the Word Cloud should reveal we did a nice job preparing our data. We can now see the tales talk about kings, mothers, fathers, foxes and something that is little. Much more informative!

![](/images/2017/06/Screen-Shot-2017-06-19-at-09.51.40.png)


**Related:** [Workshop: Text Analysis for Social Scientists](/blog/2017/06/09/workshop-text-analysis-for-social-scientists/)
