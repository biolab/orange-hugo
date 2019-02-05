+++
author="BIOLAB"
date= '2011-08-24 22:26:00+00:00'
draft= false
title="Faster classification and regression trees"
type="blog"
categories=["classification" ,"regression" ,"tree" ]
tags=["classification" ,"regression" ,"tree" ]

+++

SimpleTreeLearner is an implementation of classification and regression trees that sacrifices flexibility for speed. A benchmark on 42 different datasets reveals that SimpleTreeLearner is **11 times faster** than the original TreeLearner.

The motivation behind developing a new tree induction algorithm from scratch was to speed up the construction of random forests, but you can also use it as a standalone learner. SimpleTreeLearner uses gain ratio for classification and MSE for regression and can handle unknown values.


### Comparison with TreeLearner


The graph below shows SimpleTreeLearner construction times on datasets bundled with Orange normalized to TreeLearner. Smaller is better.

![](/images/2011/08/24/simpletree_speed.png__600x641_q95_crop_upscale.png)


The harmonic mean (average speedup) on all the benchmarks is 11.4.


### Usage


The user can set four parameters:



maxMajority
    Maximal proportion of majority class.
minExamples
    Minimal number of examples in leaves.
maxDepth
    Maximal depth of tree.
skipProb
    At every split an attribute will be skipped with probability skipProb. This parameter is especially useful for building random forests.
The code snippet below demonstrates the basic usage of SimpleTreeLearner. It behaves much like any other Orange learner would.




    
    <span class="kn">import</span> <span class="nn">Orange</span>
    
    data <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">"iris"</span><span class="p">)</span>
    
    <span class="c"># build classifier and classify train data</span>
    classifier <span class="o">=</span> Orange<span class="o">.</span>classification<span class="o">.</span>tree<span class="o">.</span>SimpleTreeLearner<span class="p">(</span>data<span class="p">,</span> maxMajority<span class="o">=</span><span class="mf">0.8</span><span class="p">)</span>
    <span class="k">for</span> ex <span class="ow">in</span> data<span class="p">:</span>
        <span class="k">print</span> classifier<span class="p">(</span>ex<span class="p">)</span>
    
    <span class="c"># estimate classification accuracy with cross-validation</span>
    learner <span class="o">=</span> Orange<span class="o">.</span>classification<span class="o">.</span>tree<span class="o">.</span>SimpleTreeLearner<span class="p">(</span>minExamples<span class="o">=</span><span class="mi">2</span><span class="p">)</span>
    result <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>testing<span class="o">.</span>cross_validation<span class="p">([</span>learner<span class="p">],</span> data<span class="p">)</span>
    <span class="k">print</span> <span class="s">'CA:'</span><span class="p">,</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>scoring<span class="o">.</span>CA<span class="p">(</span>result<span class="p">)[</span><span class="mi">0</span><span class="p">]</span>



