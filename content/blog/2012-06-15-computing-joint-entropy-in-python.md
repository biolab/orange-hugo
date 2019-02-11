+++
author="BIOLAB"
date= '2012-06-15 13:21:00+00:00'
draft= false
title="Computing joint entropy (in Python)"
type="blog"
categories=["orange3" ,"python" ]
tags=["entropy" ,"python" ]

+++

How I wrote a beautiful, general, and super fast joint entropy method (in Python).




    
    <span class="k">def</span> <span class="nf">entropy</span><span class="p">(</span><span class="o">*</span>X<span class="p">):</span>
        <span class="k">return</span> <span class="o">=</span> np<span class="o">.</span>sum<span class="p">(</span><span class="o">-</span>p <span class="o">*</span> np<span class="o">.</span>log2<span class="p">(</span>p<span class="p">)</span> <span class="k">if</span> p <span class="o">></span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">0</span> <span class="k">for</span> p <span class="ow">in</span>
            <span class="p">(</span>np<span class="o">.</span>mean<span class="p">(</span><span class="nb">reduce</span><span class="p">(</span>np<span class="o">.</span>logical_and<span class="p">,</span> <span class="p">(</span>predictions <span class="o">==</span> c <span class="k">for</span> predictions<span class="p">,</span> c <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>X<span class="p">,</span> classes<span class="p">))))</span>
                <span class="k">for</span> classes <span class="ow">in</span> itertools<span class="o">.</span>product<span class="p">(</span><span class="o">*</span><span class="p">[</span><span class="nb">set</span><span class="p">(</span>x<span class="p">)</span> <span class="k">for</span> x <span class="ow">in</span> X<span class="p">])))</span>





I started with the method to compute the entropy of a single variable. Input is a numpy array with discrete values (either integers or strings).




    
    <span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
    
    <span class="k">def</span> <span class="nf">entropy</span><span class="p">(</span>X<span class="p">):</span>
        probs <span class="o">=</span> <span class="p">[</span>np<span class="o">.</span>mean<span class="p">(</span>X <span class="o">==</span> c<span class="p">)</span> <span class="k">for</span> c <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span>X<span class="p">)]</span>
        <span class="k">return</span> np<span class="o">.</span>sum<span class="p">(</span><span class="o">-</span>p <span class="o">*</span> np<span class="o">.</span>log2<span class="p">(</span>p<span class="p">)</span> <span class="k">for</span> p <span class="ow">in</span> probs<span class="p">)</span>

In my next version I extended it to compute the joint entropy of two variables:

    
    <span class="k">def</span> <span class="nf">entropy</span><span class="p">(</span>X<span class="p">,</span> Y<span class="p">):</span>
        probs <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> c1 <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span>X<span class="p">):</span>
            <span class="k">for</span> c2 <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span>Y<span class="p">):</span>
                probs<span class="o">.</span>append<span class="p">(</span>np<span class="o">.</span>mean<span class="p">(</span>np<span class="o">.</span>logical_and<span class="p">(</span>X <span class="o">==</span> c1<span class="p">,</span> Y <span class="o">==</span> c2<span class="p">)))</span>
    
        <span class="k">return</span> np<span class="o">.</span>sum<span class="p">(</span><span class="o">-</span>p <span class="o">*</span> np<span class="o">.</span>log2<span class="p">(</span>p<span class="p">)</span> <span class="k">for</span> p <span class="ow">in</span> probs<span class="p">)</span>


Now wait a minute, it looks like we have a recursion here. I couldn't stop myself of writing en extended general function to compute the joint entropy of n variables.
  
    <span class="k">def</span> <span class="nf">entropy</span><span class="p">(</span><span class="o">*</span>X<span class="p">,</span> <span class="o">**</span>kwargs<span class="p">):</span>
        predictions <span class="o">=</span> parse_arg<span class="p">(</span>X<span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        H <span class="o">=</span> kwargs<span class="p">[</span><span class="s">"H"</span><span class="p">]</span> <span class="k">if</span> <span class="s">"H"</span> <span class="ow">in</span> kwargs <span class="k">else</span> <span class="mi">0</span>
        v <span class="o">=</span> kwargs<span class="p">[</span><span class="s">"v"</span><span class="p">]</span> <span class="k">if</span> <span class="s">"v"</span> <span class="ow">in</span> kwargs <span class="k">else</span> np<span class="o">.</span>array<span class="p">([</span><span class="bp">True</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span>predictions<span class="p">))</span>
    
        <span class="k">for</span> c <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span>predictions<span class="p">):</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span>X<span class="p">)</span> <span class="o">></span> <span class="mi">1</span><span class="p">:</span>
                H <span class="o">=</span> entropy<span class="p">(</span><span class="o">*</span>X<span class="p">[</span><span class="mi">1</span><span class="p">:],</span> v<span class="o">=</span>np<span class="o">.</span>logical_and<span class="p">(</span>v<span class="p">,</span> predictions <span class="o">==</span> c<span class="p">),</span> H<span class="o">=</span>H<span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                p <span class="o">=</span> np<span class="o">.</span>mean<span class="p">(</span>np<span class="o">.</span>logical_and<span class="p">(</span>v<span class="p">,</span> predictions <span class="o">==</span> c<span class="p">))</span>
                H <span class="o">+=</span> <span class="o">-</span>p <span class="o">*</span> np<span class="o">.</span>log2<span class="p">(</span>p<span class="p">)</span> <span class="k">if</span> p <span class="o">></span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">0</span>
        <span class="k">return</span> H


It was the ugliest recursive function I've ever written. I couldn't stop coding, I was hooked. Besides, this method was slow as hell and I need a faster version for my reasearch. I need my data tommorow, not next month. I googled if Python has something that would help me deal with the recursive part. I fould this great method: itertools.product, I's just what we need. It takes lists and returns a cartesian product of their values. It's the "nested for loops" in one function.

   
    <span class="k">def</span> <span class="nf">entropy</span><span class="p">(</span><span class="o">*</span>X<span class="p">):</span>
        n_insctances <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>X<span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        H <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> classes <span class="ow">in</span> itertools<span class="o">.</span>product<span class="p">(</span><span class="o">*</span><span class="p">[</span><span class="nb">set</span><span class="p">(</span>x<span class="p">)</span> <span class="k">for</span> x <span class="ow">in</span> X<span class="p">]):</span>
            v <span class="o">=</span> np<span class="o">.</span>array<span class="p">([</span><span class="bp">True</span><span class="p">]</span> <span class="o">*</span> n_insctances<span class="p">)</span>
            <span class="k">for</span> predictions<span class="p">,</span> c <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>X<span class="p">,</span> classes<span class="p">):</span>
                v <span class="o">=</span> np<span class="o">.</span>logical_and<span class="p">(</span>v<span class="p">,</span> predictions <span class="o">==</span> c<span class="p">)</span>
            p <span class="o">=</span> np<span class="o">.</span>mean<span class="p">(</span>v<span class="p">)</span>
            H <span class="o">+=</span> <span class="o">-</span>p <span class="o">*</span> np<span class="o">.</span>log2<span class="p">(</span>p<span class="p">)</span> <span class="k">if</span> p <span class="o">></span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">0</span>
        <span class="k">return</span> H

No resursion, but still slow. It's time to rewrite loops to the Python-like style. As a sharp eye has already noticed, the second for loop with the np.logical_and inside is perfect for the reduce method.
    
    <span class="k">def</span> <span class="nf">entropy</span><span class="p">(</span><span class="o">*</span>X<span class="p">):</span>
        n_insctances <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>X<span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        H <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> classes <span class="ow">in</span> itertools<span class="o">.</span>product<span class="p">(</span><span class="o">*</span><span class="p">[</span><span class="nb">set</span><span class="p">(</span>x<span class="p">)</span> <span class="k">for</span> x <span class="ow">in</span> X<span class="p">]):</span>
            v <span class="o">=</span> <span class="nb">reduce</span><span class="p">(</span>np<span class="o">.</span>logical_and<span class="p">,</span> <span class="p">(</span>predictions<span class="p">,</span> c <span class="k">for</span> predictions<span class="p">,</span> c <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>X<span class="p">,</span> classes<span class="p">)))</span>
            p <span class="o">=</span> np<span class="o">.</span>mean<span class="p">(</span>v<span class="p">)</span>
            H <span class="o">+=</span> <span class="o">-</span>p <span class="o">*</span> np<span class="o">.</span>log2<span class="p">(</span>p<span class="p">)</span> <span class="k">if</span> p <span class="o">></span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">0</span>
        <span class="k">return</span> H

Now, we have to remove just one more list comprehension and we have a beautiful, general, and super fast joint etropy method.

   
    <span class="k">def</span> <span class="nf">entropy</span><span class="p">(</span><span class="o">*</span>X<span class="p">):</span>
        <span class="k">return</span> <span class="o">=</span> np<span class="o">.</span>sum<span class="p">(</span><span class="o">-</span>p <span class="o">*</span> np<span class="o">.</span>log2<span class="p">(</span>p<span class="p">)</span> <span class="k">if</span> p <span class="o">></span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">0</span> <span class="k">for</span> p <span class="ow">in</span>
            <span class="p">(</span>np<span class="o">.</span>mean<span class="p">(</span><span class="nb">reduce</span><span class="p">(</span>np<span class="o">.</span>logical_and<span class="p">,</span> <span class="p">(</span>predictions <span class="o">==</span> c <span class="k">for</span> predictions<span class="p">,</span> c <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>X<span class="p">,</span> classes<span class="p">))))</span>
                <span class="k">for</span> classes <span class="ow">in</span> itertools<span class="o">.</span>product<span class="p">(</span><span class="o">*</span><span class="p">[</span><span class="nb">set</span><span class="p">(</span>x<span class="p">)</span> <span class="k">for</span> x <span class="ow">in</span> X<span class="p">])))</span>
