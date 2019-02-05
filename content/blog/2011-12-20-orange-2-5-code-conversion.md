+++
author="MARKO"
date= '2011-12-20 12:21:00+00:00'
draft= false
title="'Orange 2.5: code conversion'"
type="blog"
categories=["orange25" ]
tags=["orange25" ]

+++

Orange 2.5 unifies Orange's C++ core and Python modules into a single module hierarchy. To use the new module hierarchy, import Orange instead of orange and accompanying orng* modules. While we will maintain backward compatibility in 2.* releases, we nevertheless suggest programmers to use the new interface. The provided [conversion tool](http://orange.biolab.si/trac/intertrac/wiki%3AOrange25/RefactoringTool) can help refactor your code to use the new interface.

The conversion script, orange2to25.py, resides in Orange's main directory. To refactor accuracy8.py from the "Orange for beginners" tutorial runpython orange2to25.py -w -o accuracy8_25.py doc/ofb-rst/code/accuracy8.py.

The old code




    
    <span class="kn">import</span> <span class="nn">orange</span>
    <span class="kn">import</span> <span class="nn">orngTest</span><span class="o">,</span> <span class="nn">orngStat</span><span class="o">,</span> <span class="nn">orngTree</span>
    
    <span class="c"># set up the learners</span>
    bayes <span class="o">=</span> orange<span class="o">.</span>BayesLearner<span class="p">()</span>
    tree <span class="o">=</span> orngTree<span class="o">.</span>TreeLearner<span class="p">(</span>mForPruning<span class="o">=</span><span class="mi">2</span><span class="p">)</span>
    bayes<span class="o">.</span>name <span class="o">=</span> <span class="s">"bayes"</span>
    tree<span class="o">.</span>name <span class="o">=</span> <span class="s">"tree"</span>
    learners <span class="o">=</span> <span class="p">[</span>bayes<span class="p">,</span> tree<span class="p">]</span>
    
    <span class="c"># compute accuracies on data</span>
    data <span class="o">=</span> orange<span class="o">.</span>ExampleTable<span class="p">(</span><span class="s">"voting"</span><span class="p">)</span>
    res <span class="o">=</span> orngTest<span class="o">.</span>crossValidation<span class="p">(</span>learners<span class="p">,</span> data<span class="p">,</span> folds<span class="o">=</span><span class="mi">10</span><span class="p">)</span>
    cm <span class="o">=</span> orngStat<span class="o">.</span>computeConfusionMatrices<span class="p">(</span>res<span class="p">,</span>
            classIndex<span class="o">=</span>data<span class="o">.</span>domain<span class="o">.</span>classVar<span class="o">.</span>values<span class="o">.</span>index<span class="p">(</span><span class="s">'democrat'</span><span class="p">))</span>





is refactored to




    
    <span class="kn">import</span> <span class="nn">Orange</span>
    
    <span class="c"># set up the learners</span>
    bayes <span class="o">=</span> Orange<span class="o">.</span>classification<span class="o">.</span>bayes<span class="o">.</span>NaiveLearner<span class="p">()</span>
    tree <span class="o">=</span> Orange<span class="o">.</span>classification<span class="o">.</span>tree<span class="o">.</span>TreeLearner<span class="p">(</span>mForPruning<span class="o">=</span><span class="mi">2</span><span class="p">)</span>
    bayes<span class="o">.</span>name <span class="o">=</span> <span class="s">"bayes"</span>
    tree<span class="o">.</span>name <span class="o">=</span> <span class="s">"tree"</span>
    learners <span class="o">=</span> <span class="p">[</span>bayes<span class="p">,</span> tree<span class="p">]</span>
    
    <span class="c"># compute accuracies on data</span>
    data <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">"voting"</span><span class="p">)</span>
    res <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>testing<span class="o">.</span>cross_validation<span class="p">(</span>learners<span class="p">,</span> data<span class="p">,</span> folds<span class="o">=</span><span class="mi">10</span><span class="p">)</span>
    cm <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>scoring<span class="o">.</span>compute_confusion_matrices<span class="p">(</span>res<span class="p">,</span>
            classIndex<span class="o">=</span>data<span class="o">.</span>domain<span class="o">.</span>classVar<span class="o">.</span>values<span class="o">.</span>index<span class="p">(</span><span class="s">'democrat'</span><span class="p">))</span>





Read more about [the refactoring tool on the wiki](http://orange.biolab.si/trac/intertrac/wiki%3AOrange25/RefactoringTool) and on the help page (python orange2to25.py --help).
