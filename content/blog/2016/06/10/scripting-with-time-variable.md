+++
author="AJDA"
date= '2016-06-10 12:37:50+00:00'
draft= false
title="Scripting with Time Variable"
type="blog"
categories=["data" ,"examples" ,"scripting", "orange3" ]
+++

It's always fun to play around with data. And since Orange can, as of a few months ago, read temporal data, we decided to parse some data we had and put it into Orange.

TimeVariable is an extended class of continuous variable and it works with properly formated ISO standard datetime (Y-M-D h:m:s). Oftentimes our original data is not in the right format and needs to be edited first, so Orange can read it. Python's own datetime module is of great help. You can give it any date format and tell it how to interpret it in the argument.

    import datetime
    date = "13.03.2013 13:13:31"
    new_date = str(datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S"))
    >>> '2013-03-13 13:13:31'

Do this for all your datetime attributes. This will transform them into strings that Orange's TimeVariable can read. Then create a new data table:

    import Orange
    from Orange.data import Domain, TimeVariable
    domain = Domain([TimeVariable("timestamp")])
    timestamps = ["2013-03-13 13:13:31", "2014-04-14 14:14:41", "2015-05-15 15:15:51"]
    #create a new TimeVariable object
    time_var = TimeVariable()
    #it's important to parse strings into floats with var.parse(i)
    #list(zip(data)) then transforms the list into a 2d list of lists
    time_data = Orange.data.Table(domain, list(zip(time_var.parse(i) for i in timestamps)))

Now say you have some original data you want to append your new data to.

    data = Orange.data.Table.concatenate([original_data, time_data])
    Table.save(data, "data.tab")

But what if you want to select only a few attributes from the original data? It can be arranged.

    original_data = Orange.data.Table("original_data.tab")
    new_domain = Domain(["attribute_1", "attribute_2"], source=original_data.domain)
    new_data = Orange.data.Table(new_domain, original_data)

Then concatenate again:

    data = Orange.data.Table.concatenate([new_data, time_data])
    Table.save(data, "selected_data.tab")

Remember, if your data has string variables, they will always be in meta attributes.

    domain = Domain(["some_attribute1", "other_attribute2"], metas=["some_string_variable"])

Have fun scripting!
