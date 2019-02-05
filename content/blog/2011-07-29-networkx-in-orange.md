+++
author="BIOLAB"
date= '2011-07-29 18:56:00+00:00'
draft= false
title="NetworkX in Orange"
type="blog"
categories=["analysis" ,"network" ,"networkx" ,"visualization" ]
tags=["analysis" ,"network" ,"networkx" ,"visualization" ]

+++

[NetworkX](http://networkx.lanl.gov/) – a popular open-source python library for network analysis has finally found its way into Orange. It is now used as a base class for network representation in all Orange modules and widgets. By that, we offered to the widespread network community a fruitful and fun way to visualize and explore networks, using their existing NetworkX scripts. It has never been easier to combine network analysis and visualization with existing machine learning and data discovery methods.

Complete documentation is available in the [Orange network headquarters](/doc/orange25/Orange.network.html). For a brief overview, take a look at the following example. Let us suppose we would like to analyse the data about patients, having one of two types of leukemia. So, we have a [data set](http://blog.biolab.si/wp-content/uploads/2011/07/29/leukemiagsea.tab) with 72 patient, 4600+ gene expressions and a class variable. We also have a vast [network of human genes](http://blog.biolab.si/wp-content/uploads/2011/08/01/genes_biofuncttar.gz), connected if they share a biological function. What we would like to examine is a sub-network with only several hundred most expressed genes from the data set. To show off a bit, we will also use the [Orange Bioinformatics add-on](/addons/). Here is how we do it:




    
    <span class="kn">import</span> <span class="nn">Orange</span>
    <span class="kn">import</span> <span class="nn">obiExpression</span>
    
    <span class="c"># load leukemia data set</span>
    table <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">"/media/Ox/Projects_Archive/res/BIO/leukemia/leukemiaGSEA.tab"</span><span class="p">)</span>
    
    useAttributeLabels <span class="o">=</span> <span class="bp">False</span>
    ttest <span class="o">=</span> obiExpression<span class="o">.</span>ExpressionSignificance_TTest<span class="p">(</span>table<span class="p">,</span> useAttributeLabels<span class="p">)</span>
    
    target <span class="o">=</span> <span class="p">[</span>table<span class="o">.</span>domain<span class="o">.</span>classVar<span class="p">(</span><span class="mi">0</span><span class="p">),</span> table<span class="o">.</span>domain<span class="o">.</span>classVar<span class="p">(</span><span class="mi">1</span><span class="p">)]</span>
    
    <span class="c"># test for significantly expressed genes</span>
    score <span class="o">=</span> ttest<span class="p">(</span>target <span class="o">=</span> target<span class="p">)</span>
    
    <span class="c"># each gene is scored (t-test, p-value)</span>
    <span class="k">print</span> score<span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="o">>>></span> <span class="p">(</span>FloatVariable <span class="s">'HIST1H4C'</span><span class="p">,</span> <span class="p">(</span><span class="mf">1.8377179790830149</span><span class="p">,</span> <span class="mf">0.07034778767062116</span><span class="p">))</span>
    
    <span class="c"># sort by p-value</span>
    <span class="kn">from</span> <span class="nn">operator</span> <span class="kn">import</span> itemgetter
    score<span class="o">.</span>sort<span class="p">(</span>key<span class="o">=</span><span class="k">lambda</span> s<span class="p">:</span> s<span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">])</span>
    
    <span class="c"># select 200 genes with the lowest p-value</span>
    important_genes <span class="o">=</span> <span class="p">[</span>gene_var<span class="o">.</span>name <span class="k">for</span> gene_var<span class="p">,</span> s <span class="ow">in</span> score<span class="p">[:</span><span class="mi">200</span><span class="p">]]</span>
    
    <span class="c"># read the gene network (5000+ genes, dense network)</span>
    G <span class="o">=</span> Orange<span class="o">.</span>network<span class="o">.</span>readwrite<span class="o">.</span>read<span class="p">(</span><span class="s">'genes_biofunct.gpickle'</span><span class="p">)</span>
    
    items <span class="o">=</span> G<span class="o">.</span>items<span class="p">()</span><span class="o">.</span>filter_bool<span class="p">({</span><span class="s">'gene'</span><span class="p">:</span> important_genes<span class="p">})</span>
    indices <span class="o">=</span> <span class="p">[</span>i <span class="k">for</span> i<span class="p">,</span> present <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span>items<span class="p">)</span> <span class="k">if</span> present<span class="p">]</span>
    
    <span class="c"># build a subraph of 200 most expressed genes</span>
    G_sub <span class="o">=</span> G<span class="o">.</span>subgraph<span class="p">(</span>indices<span class="p">)</span>





In addition to the power of scripting environment, we also get the benefits of visual data exploration with Orange widgets. However, network widgets are currently under heavy development, so expect some bugs if you dare to try them. Coding should be finished in a month or two, check the blog for progress updates. Here is how to open the network in Nx Explorer widget:




    
    <span class="kn">import</span> <span class="nn">sys</span>
    <span class="kn">import</span> <span class="nn">PyQt4</span>
    
    <span class="c"># must have OWNxExplorer in python path!</span>
    <span class="kn">import</span> <span class="nn">OWNxExplorer</span>
    
    app<span class="o">=</span>PyQt4<span class="o">.</span>QtGui<span class="o">.</span>QApplication<span class="p">(</span>sys<span class="o">.</span>argv<span class="p">)</span>
    ow<span class="o">=</span>OWNxExplorer<span class="o">.</span>OWNxExplorer<span class="p">()</span>
    ow<span class="o">.</span>show<span class="p">()</span>
    
    <span class="c"># set the network</span>
    ow<span class="o">.</span>set_graph<span class="p">(</span>G_sub<span class="p">)</span>
    app<span class="o">.</span>exec_<span class="p">()</span>



