+++
author="BIOLAB"
date= '2011-07-29 18:56:00+00:00'
draft= false
title="NetworkX in Orange"
type="blog"
categories=["analysis" ,"network" ,"networkx" ,"visualization" ]
+++

[NetworkX](http://networkx.lanl.gov/) – a popular open-source python library for network analysis has finally found its way into Orange. It is now used as a base class for network representation in all Orange modules and widgets. By that, we offered to the widespread network community a fruitful and fun way to visualize and explore networks, using their existing NetworkX scripts. It has never been easier to combine network analysis and visualization with existing machine learning and data discovery methods.

Complete documentation is available in the [Orange network headquarters](/doc/orange25/Orange.network.html). For a brief overview, take a look at the following example. Let us suppose we would like to analyse the data about patients, having one of two types of leukemia. So, we have a [data set](http://blog.biolab.si/wp-content/uploads/2011/07/29/leukemiagsea.tab) with 72 patient, 4600+ gene expressions and a class variable. We also have a vast [network of human genes](images/2011/08/01/genes_biofuncttar.gz), connected if they share a biological function. What we would like to examine is a sub-network with only several hundred most expressed genes from the data set. To show off a bit, we will also use the [Orange Bioinformatics add-on](/addons/). Here is how we do it:



    import Orange
    import obiExpression

    # load leukemia data set
    table = Orange.data.Table("/media/Ox/Projects_Archive/res/BIO/leukemia/leukemiaGSEA.tab")

    useAttributeLabels = False
    ttest = obiExpression.ExpressionSignificance_TTest(table, useAttributeLabels)

    target = [table.domain.classVar(0), table.domain.classVar(1)]

    # test for significantly expressed genes
    score = ttest(target = target)

    # each gene is scored (t-test, p-value)
    print score[0]
    >>> (FloatVariable 'HIST1H4C', (1.8377179790830149, 0.07034778767062116))

    # sort by p-value
    from operator import itemgetter
    score.sort(key=lambda s: s[1][1])

    # select 200 genes with the lowest p-value
    important_genes = [gene_var.name for gene_var, s in score[:200]]

    # read the gene network (5000+ genes, dense network)
    G = Orange.network.readwrite.read('genes_biofunct.gpickle')

    items = G.items().filter_bool({'gene': important_genes})
    indices = [i for i, present in enumerate(items) if present]

    # build a subraph of 200 most expressed genes
    G_sub = G.subgraph(indices)




In addition to the power of scripting environment, we also get the benefits of visual data exploration with Orange widgets. However, network widgets are currently under heavy development, so expect some bugs if you dare to try them. Coding should be finished in a month or two, check the blog for progress updates. Here is how to open the network in Nx Explorer widget:




    
    import sys
    import PyQt4

    # must have OWNxExplorer in python path!
    import OWNxExplorer

    app=PyQt4.QtGui.QApplication(sys.argv)
    ow=OWNxExplorer.OWNxExplorer()
    ow.show()

    # set the network
    ow.set_graph(G_sub)
    app.exec_()



