+++
author="BLAZ"
date= '2013-01-06 19:30:00+00:00'
draft= false
title="New scripting tutorial"
type="blog"
categories=["documentation" ,"examples" ,"tutorial" ]
tags=["documentation" ,"examples" ,"tutorial" ]

+++

Orange just got a new, completely rewritten [scripting tutorial](http://docs.orange.biolab.si/latest/tutorial/rst). The tutorial uses Orange class hierarchy as introduced for version 2.5. The tutorial is supposed to be a gentle introduction in Orange scripting. It includes many examples, from really simple ones to those more complex. To give you a hint about the later, here is the code for learner with feature subset selection from:




    
    <span class="k">class</span> <span class="nc">SmallLearner</span><span class="p">(</span>Orange<span class="o">.</span>classification<span class="o">.</span>PyLearner<span class="p">):</span>
        <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> base_learner<span class="o">=</span>Orange<span class="o">.</span>classification<span class="o">.</span>bayes<span class="o">.</span>NaiveLearner<span class="p">,</span>
                     name<span class="o">=</span><span class="s">'small'</span><span class="p">,</span> m<span class="o">=</span><span class="mi">5</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span>name <span class="o">=</span> name
            <span class="bp">self</span><span class="o">.</span>m   <span class="o">=</span> m
            <span class="bp">self</span><span class="o">.</span>base_learner <span class="o">=</span> base_learner
    
        <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> data<span class="p">,</span> weight<span class="o">=</span><span class="bp">None</span><span class="p">):</span>
            gain <span class="o">=</span> Orange<span class="o">.</span>feature<span class="o">.</span>scoring<span class="o">.</span>InfoGain<span class="p">()</span>
            m <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span>m<span class="p">,</span> <span class="nb">len</span><span class="p">(</span>data<span class="o">.</span>domain<span class="o">.</span>features<span class="p">))</span>
            best <span class="o">=</span> <span class="p">[</span>f <span class="k">for</span> _<span class="p">,</span> f <span class="ow">in</span> <span class="nb">sorted</span><span class="p">((</span>gain<span class="p">(</span>x<span class="p">,</span> data<span class="p">),</span> x<span class="p">)</span> \
              <span class="k">for</span> x <span class="ow">in</span> data<span class="o">.</span>domain<span class="o">.</span>features<span class="p">)[</span><span class="o">-</span>m<span class="p">:]]</span>
            domain <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Domain<span class="p">(</span>best <span class="o">+</span> <span class="p">[</span>data<span class="o">.</span>domain<span class="o">.</span>class_var<span class="p">])</span>
    
            model <span class="o">=</span> <span class="bp">self</span><span class="o">.</span>base_learner<span class="p">(</span>Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span>domain<span class="p">,</span> data<span class="p">),</span> weight<span class="p">)</span>
            <span class="k">return</span> Orange<span class="o">.</span>classification<span class="o">.</span>PyClassifier<span class="p">(</span>classifier<span class="o">=</span>model<span class="p">,</span> name<span class="o">=</span><span class="bp">self</span><span class="o">.</span>name<span class="p">)</span>





The tutorial was first written for Python 2.3. Since, Python and Orange have changed a lot. And so did I. Most of the for loops have become one-liners, list and dictionary comprehension have become a must, and many new and great libraries have emerged. The (boring) tutorial code that used to read




    
    c <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span>data<span class="o">.</span>domain<span class="o">.</span>classVar<span class="o">.</span>values<span class="p">)</span>
    <span class="k">for</span> e <span class="ow">in</span> data<span class="p">:</span>
        c<span class="p">[</span><span class="nb">int</span><span class="p">(</span>e<span class="o">.</span>getclass<span class="p">())]</span> <span class="o">+=</span> <span class="mi">1</span>
    <span class="k">print</span> <span class="s">"Instances: "</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span>data<span class="p">),</span> <span class="s">"total"</span><span class="p">,</span>
    r <span class="o">=</span> <span class="p">[</span><span class="mf">0.</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span>c<span class="p">)</span>
    <span class="k">for</span> i <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span>c<span class="p">)):</span>
        r<span class="p">[</span>i<span class="p">]</span> <span class="o">=</span> c<span class="p">[</span>i<span class="p">]</span> <span class="o">*</span> <span class="mf">100.</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span>data<span class="p">)</span>
    <span class="k">for</span> i <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span>data<span class="o">.</span>domain<span class="o">.</span>classVar<span class="o">.</span>values<span class="p">)):</span>
        <span class="k">print</span> <span class="s">", </span><span class="si">%d</span><span class="s">(</span><span class="si">%4.1f%s</span><span class="s">) with class </span><span class="si">%s</span><span class="s">"</span> <span class="o">%</span> 
            <span class="p">(</span>c<span class="p">[</span>i<span class="p">],</span> r<span class="p">[</span>i<span class="p">],</span> <span class="s">'%'</span><span class="p">,</span> data<span class="o">.</span>domain<span class="o">.</span>classVar<span class="o">.</span>values<span class="p">[</span>i<span class="p">]),</span>
    <span class="k">print</span>





is now replaced with




    
    <span class="k">print</span> Counter<span class="p">(</span><span class="nb">str</span><span class="p">(</span>d<span class="o">.</span>get_class<span class="p">())</span> <span class="k">for</span> d <span class="ow">in</span> data<span class="p">)</span>





Ok. Pretty print is missing, but that, if not in the same line, could be done in another one.

For now, the tutorial focuses on data input and output, classification and regression. We plan to use other sections, but you can also give us a hint if there are any you would wish to be included.
