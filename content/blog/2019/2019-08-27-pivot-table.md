+++
author="Ajda Pretnar"
date= '2019-08-27'
draft= false
title="Aggregate, Group By and Pivot with... Pivot Table!"
type="blog"
thumbImage = "/blog_img/2019/2019-08-27_pivot-preview.png"
frontPageImage = "/blog_img/2019/2019-08-27_pivot-preview.png"
blog=["pivot table", "aggregate", "data", "groupby"]
shortExcerpt = "Orange's brand new Pivot Table widget with many aggregation and grouping functionalities."
longExcerpt = "Orange has a brand new Pivot Table widget with many aggregation and grouping functionalities. It can be used to transform the data on-the-fly and use the output for downstream analysis."
+++
Orange recently welcomed its new Pivot Table widget, which offers functionalities for data aggregation, grouping and, well, pivot tables. The widget is a one-stop-shop for pandas' aggregate, groupby and pivot_table functions.

{{% figure src="/blog_img/2019/2019-08-27_workflow.png" caption="" %}}
\

Let us see how to achieve these tasks in Orange. For all of the below examples we will be using the *heart_disease.tab* data.

## pandas.DataFrame.agg

The first task is computing a simple mean for the column *age*.

[In pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.aggregate.html):
~~~~
>>>df['age'].agg('mean')
54.43894389438944
~~~~
\

In Orange:

In **Pivot Table** we set *Values* to *age* and set aggregations to *mean*. There is no way to turn off splitting by rows in Pivot Table, but the values in Total report the mean value for the chosen attribute.

{{% figure src="/blog_img/2019/2019-08-27_pivot-aggregate.png" caption="" %}}
\

An even better way to observe simple statistics is in **Feature Statistics** widget. The widget also reports on the mean value of each attribute with handy distributions plots included.

{{% figure src="/blog_img/2019/2019-08-27_feature-statistics.png" caption="" %}}
\

Yet another way to observe a mean value is in a **Box Plot**.

{{% figure src="/blog_img/2019/2019-08-27_box-plot.png" caption="" %}}
\
\

## pandas.DataFrame.groupby

The second task is grouping the data by a discrete column. Say we want to group by gender and report the mean value for each column.

[In pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html):
~~~~
>>> df.groupby(['gender']).mean()
              age    rest SBP   ...  ST by exer.  major ves. col.  diameter narrowing
gender
female  55.721649  133.340206   ...   0.867010    0.546392          0.257732
male    53.834951  130.912621   ...   1.120874    0.732673          0.553398

[2 rows x 9 columns]
~~~~

In Orange:

In **Pivot Table** set *Rows* to *gender* and aggregation method to *mean*. The *Values* option in this example has no effect. Now, connect **Data Table** to Pivot Table. Finally, reset the connections. Pivot Table outputs three types of data - Pivot Table, Filtered Data, and Grouped Data. The output we are looking for here is *Grouped Data*.

{{% figure src="/blog_img/2019/2019-08-27_edit-links.png" caption="" %}}
\

{{% figure src="/blog_img/2019/2019-08-27_pivot-groupby.png" caption="" %}}
\

This is our data table. Exactly what we were looking for.

{{% figure src="/blog_img/2019/2019-08-27_groupby-data-table.png" caption="" %}}
\
\

## pandas.DataFrame.pivot_table

The third, final task is constructing a pivot table where rows are values of *diameter narrowing*, columns are values of *gender* and the values in cells is the mean of *age* for each subgroup. In other words, we want to see the average age of females with diameter narrowing, males with diameter narrowing, females without diameter narrowing and males without diameter narrowing.

[In pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table):
~~~~
>>> pd.pivot_table(df, values='age', index=['diameter narrowing'], columns=['gender'], aggfunc=np.mean)
gender                 female       male
diameter narrowing
0                   54.555556  51.043478
1                   59.080000  56.087719
~~~~

In Orange:

In **Pivot Table** set *Rows* to *diameter narrowing*, *Columns* to *gender*, *Values* to *age* and aggregation method to *mean*. The widget already offers a view of the final data table, but we can also output it and use it in other Orange widgets.

{{% figure src="/blog_img/2019/2019-08-27_pivot-table.png" caption="" %}}
\
\

**Pivot Table** widget really versatile - like a Swiss knife for data transformation.
