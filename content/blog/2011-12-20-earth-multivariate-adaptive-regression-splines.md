+++
author="BIOLAB"
date= '2011-12-20 12:22:00+00:00'
draft= false
title="Earth - Multivariate adaptive regression splines"
type="blog"
categories=["regression" ]
tags=["earth" ,"mars" ,"regression" ]

+++

There have recently been some additions to the lineup of Orange learners. One of these is Orange.regression.earth.EarthLearner. It is an Orange interface to the [Earth](http://www.milbo.users.sonic.net/earth/) library written by Stephen Milborrow implementing [Multivariate adaptive regression splines](http://en.wikipedia.org/wiki/Multivariate_adaptive_regression_splines).

So lets take it out for a spin on a simple toy dataset ([data.tab](http://blog.biolab.si/wp-content/uploads/2011/12/13/data.tab) - created using the Paint Data widget in the Orange Canvas):




    
    <span class="kn">import</span> <span class="nn">Orange</span>
    <span class="kn">from</span> <span class="nn">Orange.regression</span> <span class="kn">import</span> earth
    <span class="kn">import</span> <span class="nn">numpy</span>
    <span class="kn">from</span> <span class="nn">matplotlib</span> <span class="kn">import</span> pylab <span class="k">as</span> pl
    
    data <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">"data.tab"</span><span class="p">)</span>
    earth_predictor <span class="o">=</span> earth<span class="o">.</span>EarthLearner<span class="p">(</span>data<span class="p">)</span>
    
    X<span class="p">,</span> Y <span class="o">=</span> data<span class="o">.</span>to_numpy<span class="p">(</span><span class="s">"A/C"</span><span class="p">)</span>
    
    pl<span class="o">.</span>plot<span class="p">(</span>X<span class="p">,</span> Y<span class="p">,</span> <span class="s">".r"</span><span class="p">)</span>
    
    linspace <span class="o">=</span> numpy<span class="o">.</span>linspace<span class="p">(</span><span class="nb">min</span><span class="p">(</span>X<span class="p">),</span> <span class="nb">max</span><span class="p">(</span>X<span class="p">),</span> <span class="mi">20</span><span class="p">)</span>
    predictions <span class="o">=</span> <span class="p">[</span>earth_predictor<span class="p">([</span>s<span class="p">,</span> <span class="s">"?"</span><span class="p">])</span> <span class="k">for</span> s <span class="ow">in</span> linspace<span class="p">]</span>
    
    pl<span class="o">.</span>plot<span class="p">(</span>linspace<span class="p">,</span> predictions<span class="p">,</span> <span class="s">"-b"</span><span class="p">)</span>
    pl<span class="o">.</span>show<span class="p">()</span>





which produces the following plot:

![](/images/2011/12/13/earth_demo_2.png__600x470_q95_subject_location-407%2C297.png)


We can also print the model representation using




    
    <span class="k">print</span> earth_predictor





which outputs:

    
    Y =
       1.013
       +1.198 * max(0, X - 0.485)
       -1.803 * max(0, 0.485 - X)
       -1.321 * max(0, X - 0.283)
       -1.609 * max(0, X - 0.640)
       +1.591 * max(0, X - 0.907)


See [Orange.regression.earth reference](https://orange-multitarget.readthedocs.io/en/0.9.2/Orange.regression.earth.html) for full documentation.

(Edit: Added link to the dataset file)
