+++
author="BIOLAB"
date= '2011-12-08 15:28:00+00:00'
draft= false
title="Random forest switches to Simple tree learner by default"
type="blog"
categories=["forestlearner" ,"simpletreelearner" ]
tags=["forestlearner" ,"simpletreelearner" ]

+++

Random forest classifiers now use Orange.classification.tree.SimpleTreeLearner by default, which considerably shortens their construction times.

Using a random forest classifier is easy.




    
    <span class="kn">import</span> <span class="nn">Orange</span>
    
    iris <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">'iris'</span><span class="p">)</span>
    forest <span class="o">=</span> Orange<span class="o">.</span>ensemble<span class="o">.</span>forest<span class="o">.</span>RandomForestLearner<span class="p">(</span>iris<span class="p">,</span> trees<span class="o">=</span><span class="mi">200</span><span class="p">)</span>
    <span class="k">for</span> instance <span class="ow">in</span> iris<span class="p">:</span>
        <span class="k">print</span> forest<span class="p">(</span>instance<span class="p">),</span> instance<span class="o">.</span>get_class<span class="p">()</span>





The example above loads the iris dataset and trains a random forest classifier with 200 trees. The classifier is then used to label all training examples, printing its prediction alongside the actual class value.

Using SimpleTreeLearner insted of TreeLearner substantially reduces the training time. The image below compares construction times of Random Forest classifiers using a SimpleTreeLearner or a TreeLearner as the base learner.

![](/images/2011/12/08/forest_construction.png__600x641_q95_crop_upscale.png)


By setting the base_learner parameter to TreeLearer it is possible to revert to the original behaviour:




    
    tree_learner <span class="o">=</span> Orange<span class="o">.</span>classification<span class="o">.</span>tree<span class="o">.</span>TreeLearner<span class="p">()</span>
    forest_orig <span class="o">=</span> Orange<span class="o">.</span>ensemble<span class="o">.</span>forest<span class="o">.</span>RandomForestLearner<span class="p">(</span>base_learner<span class="o">=</span>tree_learner<span class="p">)</span>



