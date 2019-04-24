+++
title = "Faq"
url = "/faq/"
listing = true
+++

## I am having trouble installing Orange.

Make sure you are downloading the latest version. You can also try to download a standalone installer or Anaconda distribution.

Still no luck? Check our [issue tracker](https://github.com/biolab/orange3/issues) for similar issues or report a new one.

## I am having trouble installing an add-on.

Make sure you are using the latest version of Orange. Encountering issues, please raise them on the relevant {{< link_new url="https://github.com/biolab?q=orange3-" name="add-on's issue tracker">}}. Alternatively, you can try with Anaconda distribution and install the add-on in the terminal. You can use pip or conda to install a package directly. E.g.:

	pip install orange3-text

	conda install orange3-timeseries

## I get an error when using Orange.

First, make sure you are using the latest version of Orange. If this doesn’t fix the issue, you should be able to see an error window pop up, prompting you to submit the issue to the developers. Please use this option as it allows us to recreate the issue and fix it. If this is not possible, please report the issue to our [issue tracker](https://github.com/biolab/orange3/issues).

## I believe there’s a bug in Orange.

First, make sure you are using the latest version of Orange. If the bug is still present, please submit an issue to our {{< link_new url="https://github.com/biolab/orange3/issues" name="issue tracker">}}. Follow the template and describe the issue as well as possible.

Before submitting a new issue, check if someone has already reported the same problem. Upvote the issue with a +1 and/or add your comment. Only consider opening a new issue if you cannot find a corresponding existing open or closed issue.

## There’s a feature I wish to see in Orange.

Please submit a pull request with the feature. We welcome all contributions! Once you've made a PR, developer(s) will leave comments and when everything is fixed and tested, the pull request will be merged into Orange. See our {{< link_new url="https://orange.biolab.si/contributing/" name="Contribute guide">}} for more information.

If you are not a developer, you can submit a feature request to our {{< link_new url="https://github.com/biolab/orange3/issues" name="issue tracker">}}. Describe what you wish to see in Orange and, if possible, provide a visual example.

Before submitting a new feature request, check if someone has already requested the same feature. Upvote the request with a +1 and/or add your comment. Only consider opening a new request if you cannot find a corresponding existing request.

## I would like to learn how to use Orange. Where can I find the resources?

Widget documentation is available on our {{< link_new url="https://orange.biolab.si/toolbox/" name="website">}}. You can also access the same documentation directly from Orange by selecting the widget and pressing F1.

We also provide an e-mail course ( {{< link_new url="https://biolab.us15.list-manage.com/subscribe?u=2cad1f1cbf3a532a77efe4354&amp;id=6f257f15ff" name="subscribe here">}}), beginner-level {{< link_new url="https://www.youtube.com/playlist?list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy" name="YouTube tutorials">}} and a regularly updated {{< link_new url="https://blog.biolab.si/" name="blog">}}.

## I have a question concerning data mining, statistics and machine learning algorithms.

Visit {{< link_new url="https://datascience.stackexchange.com/questions/tagged/orange" name="Data Science StackExchange">}} and ask the community!

## What data does Orange support?

Core Orange supports Excel, comma- and tab-delimited files (.xlsx, .csv, .tab). It also reads online data, such as Google Spreadsheets. Orange3-ImageAnalytics add-on can import images (.jpg, .tiff, .png). Orange3-Corpus add-on can import text files (.txt, .docx, .odt). SQL widget supports PostgreSQL and MSSQL databases.

## I want to use Orange on big data.

Orange provides the SQL widget, which samples data instances and enables exploratory data analysis on large datasets. You need {{< link_new url="http://initd.org/psycopg/" name="psycopg2">}} module installed to be able to see the widget. Install it directly in Python with 

	pip install psycopg2

command. You can also use {{< link_new url="https://www.2ndquadrant.com/en/resources/2uda/" name="2UDA package">}} for easier installation. Please note that Orange supports only PostgreSQL and MSSQL databases for now.

## Can I export Orange workflow as a Python script?

Unfortunately, no. We've {{< link_new url="https://github.com/biolab/orange3/issues/1341" name="debated this long and hard">}}. A (limited) functionality of this type would probably be possible, but would be a very big project to do well and would cost more than the expected benefits.

## I wish to propose a collaboration and/or a project with the Orange team.

Please submit a contact request and we will respond as soon as we can.

## I wish to develop a widget / an add-on for Orange.

We are always happy to receive contributions! Development documentation for {{< link_new url="http://orange-development.readthedocs.io/" name="widgets">}} and {{< link_new url="https://github.com/biolab/orange3-example-addon" name="add-ons">}} is available on the web. Next, submit a pull request and our team will review it. If you have specific questions, use {{< link_new url="https://gitter.im/biolab/orange3" name="Gitter">}} for direct communication with the developers.

## I wish to commission a custom module and/or an add-on for Orange.

Please submit a contact request to discuss the idea and rates.
