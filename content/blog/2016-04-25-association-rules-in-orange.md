+++
author="AJDA"
date= '2016-04-25 07:46:33+00:00'
draft= false
title="Association Rules in Orange"
type="blog"
categories=["addons" ,"analysis" ,"association rules" ,"business intelligence" ,"examples"  ,"orange3" ,"toolbox" ]
tags=["association" ,"basket" ,"business" ,"itemsets" ,"rules" ]

+++

Orange is welcoming back one of its more exciting add-ons: [Associate](https://pypi.python.org/pypi/Orange3-Associate)! [Association rules](https://en.wikipedia.org/wiki/Association_rule_learning) can help the user quickly and simply discover the underlying relationships and connections between data instances. Yeah!

The add-on currently has two widgets: one for Association Rules and the other for Frequent Itemsets. With Frequent Itemsets we first check frequency of items and itemsets in our transaction matrix. This tell us which items (products) and itemsets are the most frequent in our data, so it would make a lot of sense focusing on these products. Let's use this widget on real Foodmart 2000 data set.

![](/images/2016/04/blog5-1.png)

First let's check our data set. We have 62560 instances with 102 features. That's a whole lot of transactions. Now we connect Frequent Itemsets to our File widget and observe the results. We went with a quite low minimal support due to the large number of transactions.

Collapse All will display the most frequent items, so these will be our most important products ('bestsellers'). Our clients seem to be buying a whole lot of fresh vegetables and fresh fruit. Call your marketing department - you could become the ultimate place to buy fruits and veggies from.

![](/images/2016/04/blog2-1.png)

If there's a little arrow on the left side of the item, you can expand it to see all the other items connected to the selected attribute. So if a person buy fresh vegetables, it is most likely to buy fresh fruits as an accompanying product group. Now you can explore frequent itemsets to understand what really sells in your store.

![](/images/2016/04/blog3-1.png)

Ok. Now how about some transaction flows? We're mostly interested in the action-consequence relationship here. In other words, if a person buys one item, what is the most likely second item she will buy? Association Rules will help us discover that.

Our parameters will again be adjusted for our data set. We probably want low support, since it will be hard to find a few prevailing rules for 62,000+ transactions. However, you want the discovered rules to be true most of the time, so increase the confidence.

![](/images/2016/04/blog1.png)

The table on the right displays a list of rules with 6 different measures of association rule quality:


* support: how often a rule is applicable to a given data set (rule/data)
* confidence: how frequently items in Y appear in transactions with X or in other words how frequently the rule is true (support for a rule/support of antecedent)
* coverage: how often antecedent item is found in the data set (support of antecedent/data)
* strength:  (support of consequent/support of antecedent)
* lift: how frequently a rule is true per consequent item (data * confidence/support of consequent)
* leverage: the difference between two item appearing in a transaction and the two items appearing independently (support*data - antecedent support * consequent support/data2)


Orange will rank the rules automatically. Now give a quick look at the rules. How about these two rules?


<blockquote>fresh vegetables, plastic utensils, deli meats, wine --> dried fruit

fresh vegetables, plastic utensils, bologna, soda --> chocolate candy</blockquote>


These seem to picnickers, clients who don't want to spend a whole lot of time preparing their food. The first group is probably more gourmet, while the second seems to enjoy sweets. A logical step would be to place dried fruit closer to the wine section and the candy bars closer to sodas. What do you say? This already happened in your local supermarket? Coincidence? I don't think so. :)

![](/images/2016/04/blog6.png)

Association rules are a powerful way to improve your business by organizing your actual or online store, adjusting marketing strategies to target suitable groups, providing product recommendations and generally understanding your client base better. Just another way Orange can be used as a business intelligence tool!
