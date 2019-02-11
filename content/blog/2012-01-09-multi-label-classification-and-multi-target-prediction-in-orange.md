+++
author="BIOLAB"
date= '2012-01-09 12:41:00+00:00'
draft= false
title="Multi-label classification (and Multi-target prediction) in Orange"
type="blog"
categories=["classification" ,"gsoc" ,"mlc" ,"multilabel" ]
tags=["classification" ,"gsoc" ,"mlc" ,"multilabel" ]

+++

The last summer, student Wencan Luo participated in [Google Summer of Code](https://code.google.com/soc/) to implement [Multi-label Classification in Orange](/blog/2011/09/02/gsoc-review-multi-label-classification-implementation/). He provided a framework, implemented a few algorithms and some prototype widgets. His work has been "hidden" in our repositories for too long; finally, we have merged part of his code into Orange (widgets are not there yet ...) and added a more general support for multi-target prediction.

You can load multi-label tab-delimited data (e.g. [emotions.tab](http://orange.biolab.si/trac/intertrac/export%3Atrunk/orange/doc/datasets/emotions.tab)) just like any other [tab-delimited data](/doc/reference/Orange.data.formats/#tab-delimited-format):

    
    <span class="o">>>></span> zoo <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">'zoo'</span><span class="p">)</span>            <span class="c"># single-target</span>
    <span class="o">>>></span> emotions <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">'emotions'</span><span class="p">)</span>  <span class="c"># multi-label</span>



The difference is that now zoo's domain has a non-empty class_var field, while a list of emotions' labels can be obtained through it's domain's class_vars:

    
    <span class="o">>>></span> zoo<span class="o">.</span>domain<span class="o">.</span>class_var
    EnumVariable <span class="s">'type'</span>
    <span class="o">>>></span> emotions<span class="o">.</span>domain<span class="o">.</span>class_vars
    <span class="o"><</span>EnumVariable <span class="s">'amazed-suprised'</span><span class="p">,</span>
     EnumVariable <span class="s">'happy-pleased'</span><span class="p">,</span>
     EnumVariable <span class="s">'relaxing-calm'</span><span class="p">,</span>
     EnumVariable <span class="s">'quiet-still'</span><span class="p">,</span>
     EnumVariable <span class="s">'sad-lonely'</span><span class="p">,</span>
     EnumVariable <span class="s">'angry-aggresive'</span><span class="o">></span>


A simple example of a [multi-label classification](/doc/reference/Orange.multilabel/) learner is a "binary relevance" learner. Let's try it out.

    
    <span class="o">>>></span> learner <span class="o">=</span> Orange<span class="o">.</span>multilabel<span class="o">.</span>BinaryRelevanceLearner<span class="p">()</span>
    <span class="o">>>></span> classifier <span class="o">=</span> learner<span class="p">(</span>emotions<span class="p">)</span>
    <span class="o">>>></span> classifier<span class="p">(</span>emotions<span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="p">[</span><span class="o"><</span>orange<span class="o">.</span>Value <span class="s">'amazed-suprised'</span><span class="o">=</span><span class="s">'0'</span><span class="o">></span><span class="p">,</span>
     <span class="o"><</span>orange<span class="o">.</span>Value <span class="s">'happy-pleased'</span><span class="o">=</span><span class="s">'0'</span><span class="o">></span><span class="p">,</span>
     <span class="o"><</span>orange<span class="o">.</span>Value <span class="s">'relaxing-calm'</span><span class="o">=</span><span class="s">'1'</span><span class="o">></span><span class="p">,</span>
     <span class="o"><</span>orange<span class="o">.</span>Value <span class="s">'quiet-still'</span><span class="o">=</span><span class="s">'1'</span><span class="o">></span><span class="p">,</span>
     <span class="o"><</span>orange<span class="o">.</span>Value <span class="s">'sad-lonely'</span><span class="o">=</span><span class="s">'1'</span><span class="o">></span><span class="p">,</span>
     <span class="o"><</span>orange<span class="o">.</span>Value <span class="s">'angry-aggresive'</span><span class="o">=</span><span class="s">'0'</span><span class="o">></span><span class="p">]</span>
    <span class="o">>>></span> classifier<span class="p">(</span>emotions<span class="p">[</span><span class="mi">0</span><span class="p">],</span> Orange<span class="o">.</span>classification<span class="o">.</span>Classifier<span class="o">.</span>GetProbabilities<span class="p">)</span>
    <span class="p">[</span><span class="o"><</span><span class="mf">1.000</span><span class="p">,</span> <span class="mf">0.000</span><span class="o">></span><span class="p">,</span> <span class="o"><</span><span class="mf">0.881</span><span class="p">,</span> <span class="mf">0.119</span><span class="o">></span><span class="p">,</span> <span class="o"><</span><span class="mf">0.000</span><span class="p">,</span> <span class="mf">1.000</span><span class="o">></span><span class="p">,</span>
     <span class="o"><</span><span class="mf">0.046</span><span class="p">,</span> <span class="mf">0.954</span><span class="o">></span><span class="p">,</span> <span class="o"><</span><span class="mf">0.000</span><span class="p">,</span> <span class="mf">1.000</span><span class="o">></span><span class="p">,</span> <span class="o"><</span><span class="mf">1.000</span><span class="p">,</span> <span class="mf">0.000</span><span class="o">></span><span class="p">]</span>



Real values of label variables of emotions[0] instance can be obtained by calling emotions[0].get_classes(), which is analogous to the get_class method in the single-target case.

For multi-label classification, we can also perform testing like usual, however, [specialised evaluation measures](/doc/reference/Orange.evaluation.scoring/#scoring-for-multilabel-classification) have to be used:


    
    <span class="o">>>></span> test <span class="o">=</span> Orange<span class="o">.</span>evaluation<span class="o">.</span>testing<span class="o">.</span>cross_validation<span class="p">([</span>learner<span class="p">],</span> emotions<span class="p">)</span>
    <span class="o">>>></span> Orange<span class="o">.</span>evaluation<span class="o">.</span>scoring<span class="o">.</span>mlc_hamming_loss<span class="p">(</span>test<span class="p">)</span>
    <span class="p">[</span><span class="mf">0.2228780213603148</span><span class="p">]</span>



In one of the following blog posts, a multi-target regression method PLS that is in the process of implementation will be described.
