+++
author="BIOLAB"
date= '2012-02-02 16:21:00+00:00'
draft= false
title="'New in Orange: Partial least squares regression'"
type="blog"
categories=["multitarget" ,"pls" ,"regression" ]
tags=["multitarget" ,"pls" ,"regression" ]

+++

[Partial least squares regression](http://en.wikipedia.org/wiki/Partial_least_squares_regression) is a regression technique which supports multiple response variables. PLS regression is very popular in areas such as bioinformatics, chemometrics etc. where the number of observations is usually less than the number of measured variables and where there exists multicollinearity among the predictor variables. In such situations, standard regression techniques would usually fail. The PLS regression is now available in Orange (see [documentation](/doc/reference/Orange.regression.pls))!

You can use PLS regression model on single-target or [multi-target](/blog/2012/01/09/multi-label-classification-and-multi-target-prediction-in-orange/) data sets. Simply load the data set [multitarget-synthetic.tab](/doc/reference/_downloads/multitarget-synthetic.tab) and see that it contains three predictor variables and four responses using this code.




    
    data <span class="o">=</span> Orange<span class="o">.</span>data<span class="o">.</span>Table<span class="p">(</span><span class="s">"multitarget-synthetic.tab"</span><span class="p">)</span>
    <span class="k">print</span> <span class="s">"Input variables:"</span>
    <span class="k">print</span> data<span class="o">.</span>domain<span class="o">.</span>features
    <span class="k">print</span> <span class="s">"Response variables:"</span>
    <span class="k">print</span> data<span class="o">.</span>domain<span class="o">.</span>class_vars





Output:




    
    Input variables<span class="p">:</span>
    <span class="o"><</span>FloatVariable <span class="s">'X1'</span><span class="p">,</span> FloatVariable <span class="s">'X2'</span><span class="p">,</span> FloatVariable <span class="s">'X3'</span><span class="o">></span>
    Response variables<span class="p">:</span>
    <span class="o"><</span>FloatVariable <span class="s">'Y1'</span><span class="p">,</span> FloatVariable <span class="s">'Y2'</span><span class="p">,</span> FloatVariable <span class="s">'Y3'</span><span class="p">,</span> FloatVariable <span class="s">'Y4'</span><span class="o">></span>





As you can see, all variables in this data set are continuous. The PLS regression is intended forsuch situations although it can be used for discrete input variables as well (using 0-1 continuation). Currently, discrete response variables are not yet supported.

Let's try to fit the PLS regression model on our data set.




    
    learner <span class="o">=</span> Orange<span class="o">.</span>multitarget<span class="o">.</span>pls<span class="o">.</span>PLSRegressionLearner<span class="p">()</span>
    classifier <span class="o">=</span> learner<span class="p">(</span>data<span class="p">)</span>





The classifier can be now used to predict values of the four responses based onthree predictors. Let's see how it manages this task on the first data instance.




    
    actual <span class="o">=</span> data<span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span>get_classes<span class="p">()</span>
    predicted <span class="o">=</span> classifier<span class="p">(</span>data<span class="p">[</span><span class="mi">0</span><span class="p">])</span> 
    
    <span class="k">print</span> <span class="s">"Actual"</span><span class="p">,</span> <span class="s">"Predicted"</span>
    <span class="k">for</span> a<span class="p">,</span> p <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>actual<span class="p">,</span> predicted<span class="p">):</span>
        <span class="k">print</span> <span class="s">"</span><span class="si">%6.3f</span> <span class="si">%6.3f</span><span class="s">"</span> <span class="o">%</span> <span class="p">(</span>a<span class="p">,</span>p<span class="p">)</span>





Output:




    
    Actual Predicted
     <span class="mf">0.490</span>  <span class="mf">0.613</span>
     <span class="mf">1.237</span>  <span class="mf">0.826</span>
     <span class="mf">1.808</span>  <span class="mf">1.084</span>
     <span class="mf">0.422</span>  <span class="mf">0.534</span>





To test the usefulness of PLS as a multi-target method let's compare it to a single-target method - linear regression. We did this by comparing [Root mean squared error](http://en.wikipedia.org/wiki/Mean_squared_error) (RMSE) of predicted values for a single response variable. We constructed synthetic data sets and performed the RMSE analysis using [this script](http://blog.biolab.si/wp-content/uploads/2012/02/02/pls_vs_linear.py). The results can be seen in the following output:




    
        Training <span class="nb">set</span> sizes      <span class="mi">5</span>     <span class="mi">10</span>     <span class="mi">20</span>     <span class="mi">50</span>    <span class="mi">100</span>    <span class="mi">200</span>    <span class="mi">500</span>   <span class="mi">1000</span>
    Linear <span class="p">(</span>single<span class="o">-</span>target<span class="p">)</span> <span class="mf">0.5769</span> <span class="mf">0.3128</span> <span class="mf">0.2703</span> <span class="mf">0.2529</span> <span class="mf">0.2493</span> <span class="mf">0.2446</span> <span class="mf">0.2436</span> <span class="mf">0.2442</span>
        PLS <span class="p">(</span>multi<span class="o">-</span>target<span class="p">)</span> <span class="mf">0.3663</span> <span class="mf">0.2955</span> <span class="mf">0.2623</span> <span class="mf">0.2517</span> <span class="mf">0.2487</span> <span class="mf">0.2447</span> <span class="mf">0.2441</span> <span class="mf">0.2448</span>





We can see that PLS regression outperforms linear regression when the number of training instances is low. Such situations (low number of instances compared to high number of variables) are quite common when analyzing data sets in bioinformatics. However, with increasing number of training instances, the advantages of PLS regression diminish.
