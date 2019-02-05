+++
author="MARKO"
date= '2011-05-20 15:08:00+00:00'
draft= false
title="Orange 2.5 progress"
type="blog"
categories=["orange25" ]
tags=["orange25" ]

+++

We decided that we should reorganize Orange to provide more intuitive interface to the scripting interface. The next release, Orange 2.5 is getting better every day. But fear not, dear reader, we are working hard to ensure that your scripts will still work.

In the last morning of the camp in Bohinj we decided to use undercase_separated names instead of CamelCase. We have been steadily converting them and the [deprecation utilities](/doc/orange25/Orange.misc.html#deprecation-utility-functions) by Aleš help a lot. We just list the name changes for class attributes or arguments and their renaming is handled gracefully; they also remain accessible with the old names. Therefore, the code does not need to be duplicated to ensure backwards compatibility.

A simple example from the documentation of bagging and boosting. The old version first:




    
    <span class="kn">import</span> <span class="nn">orange</span><span class="o">,</span> <span class="nn">orngEnsemble</span><span class="o">,</span> <span class="nn">orngTree</span>
    <span class="kn">import</span> <span class="nn">orngTest</span><span class="o">,</span> <span class="nn">orngStat</span>
    
    tree <span class="o">=</span> orngTree<span class="o">.</span>TreeLearner<span class="p">(</span>mForPruning<span class="o">=</span><span class="mi">2</span><span class="p">,</span> name<span class="o">=</span><span class="s">"tree"</span><span class="p">)</span>
    bs <span class="o">=</span> orngEnsemble<span class="o">.</span>BoostedLearner<span class="p">(</span>tree<span class="p">,</span> name<span class="o">=</span><span class="s">"boosted tree"</span><span class="p">)</span>
    bg <span class="o">=</span> orngEnsemble<span class="o">.</span>BaggedLearner<span class="p">(</span>tree<span class="p">,</span> name<span class="o">=</span><span class="s">"bagged tree"</span><span class="p">)</span>
    
    data <span class="o">=</span> orange<span class="o">.</span>ExampleTable<span class="p">(</span><span class="s">"lymphography.tab"</span><span class="p">)</span>
    
    learners <span class="o">=</span> <span class="p">[</span>tree<span class="p">,</span> bs<span class="p">,</span> bg<span class="p">]</span>
    results <span class="o">=</span> orngTest<span class="o">.</span>crossValidation<span class="p">(</span>learners<span class="p">,</span> data<span class="p">,</span> folds<span class="o">=</span><span class="mi">3</span><span class="p">)</span>
    <span class="k">print</span> <span class="s">"Classification Accuracy:"</span>
    <span class="k">for</span> i <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span>learners<span class="p">)):</span>
        <span class="k">print</span> <span class="p">(</span><span class="s">"</span><span class="si">%15s</span><span class="s">: </span><span class="si">%5.3f</span><span class="s">"</span><span class="p">)</span> <span class="o">%</span> <span class="p">(</span>learners<span class="p">[</span>i<span class="p">]</span><span class="o">.</span>name<span class="p">,</span> orngStat<span class="o">.</span>CA<span class="p">(</span>results<span class="p">)[</span>i<span class="p">])</span>





Orange 2.5 version:




    
    <span class="kn">import</span> <span class="nn">Orange</span>
    
    tree <span class="o">=</span> Orange<span class="o">.</span>classification<span class="o">.</span>tree<span class="o">.</span>TreeLearner<span class="p">(</span>m_pruning<span class="o">=</span><span class="mi">2</span><span class="p">,</span> name<span class="o">=</span><span class="s">"tree"</span><span class="p">)</span>
    bs <span class="o">=</span> Orange<span class="o">.</span>ensemble<span class="o">.</span>boosting<span class="o">.</span>BoostedLearner<span class="p">(</span>tree<span class="p">,</span> name<span class="o">=</span><span class="s">"boosted tree"</span><span class="p">)</span>
    bg <span class="o">=</span> Orange<span class="o">.</span>ensemble<span class="o">.</span>bagging<span class="o">.</span>BaggedLearner<span class="p">(</span>tree<span class="p">,</span> name<span class="o">=</span><span class="s">"bagged tree"</span><span class="p">)</span>
    
    table <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">"lymphography.tab"</span><span class="p">)</span>
    
    learners <span class="o">=</span> <span class="p">[</span>tree<span class="p">,</span> bs<span class="p">,</span> bg<span class="p">]</span>
    results <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>testing<span class="o">.</span>cross_validation<span class="p">(</span>learners<span class="p">,</span> table<span class="p">,</span> folds<span class="o">=</span><span class="mi">3</span><span class="p">)</span>
    <span class="k">print</span> <span class="s">"Classification Accuracy:"</span>
    <span class="k">for</span> i <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span>learners<span class="p">)):</span>
        <span class="k">print</span> <span class="p">(</span><span class="s">"</span><span class="si">%15s</span><span class="s">: </span><span class="si">%5.3f</span><span class="s">"</span><span class="p">)</span> <span class="o">%</span> <span class="p">(</span>learners<span class="p">[</span>i<span class="p">]</span><span class="o">.</span>name<span class="p">,</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>scoring<span class="o">.</span>CA<span class="p">(</span>results<span class="p">)[</span>i<span class="p">])</span>





In new Orange we only need to import a single module, Orange, the root of the new hierarchy.
