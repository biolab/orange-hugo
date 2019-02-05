+++
author="BIOLAB"
date= '2011-09-01 23:48:00+00:00'
draft= false
title="'GSoC Review: MF - Matrix Factorization Techniques for Data Mining'"
type="blog"
categories=["gsoc" ,"matrixfactorization" ]
tags=["gsoc" ,"matrixfactorization" ]

+++

MF - Matrix Factorization Techniques for Data Mining is a Python scripting library which includes a number of published matrix factorization algorithms, initialization methods, quality and performance measures and facilitates the combination of these to produce new strategies. The library represents a unified and efficient interface to matrix factorization algorithms and methods.

The MF works with numpy dense matrices and scipy sparse matrices (where this is possible to save on space). The library has support for multiple runs of the algorithms which can be used for some quality measures. By setting runtime specific options tracking the residuals error within one (or more) run or tracking fitted factorization model is possible. Extensive documentation with working examples which demonstrate real applications, commonly used benchmark data and visualization methods are provided to help with the interpretation and comprehension of the results.


### Content of Current Release




#### Factorization Methods





	  * BD - Bayesian nonnegative matrix factorization Gibbs sampler [Schmidt2009]
	  * BMF - Binary matrix factorization [Zhang2007]
	  * ICM - Iterated conditional modes nonnegative matrix factorization [Schmidt2009]
	  * LFNMF - Fisher nonnegative matrix factorization for learning local features [Wang2004], [Li2001]
	  * LSNMF - Alternative nonnegative least squares matrix factorization using projected gradient method for subproblems [Lin2007]
	  * NMF - Standard nonnegative matrix factorization with Euclidean / Kullback-Leibler update equations and Frobenius / divergence / connectivity cost functions [Lee2001], [Brunet2004]
	  * NSNMF - Nonsmooth nonnegative matrix factorization [Montano2006]
	  * PMF - Probabilistic nonnegative matrix factorization [Laurberg2008], [Hansen2008]
	  * PSMF - Probabilistic sparse matrix factorization [Dueck2005], [Dueck2004], [Srebro2001], [Li2007]
	  * SNMF - Sparse nonnegative matrix factorization based on alternating nonnegativity constrained least squares [Park2007]
	  * SNMNMF - Sparse network regularized multiple nonnegative matrix factorization [Zhang2011]



#### Initialization Methods





	  * Random
	  * Fixed
	  * NNDSVD [Boutsidis2007]
	  * Random C [Albright2006]
	  * Random VCol [Albright2006]



#### Quality and Performance Measures





	  * Distance
	  * Residuals
	  * Connectivity matrix
	  * Consensus matrix
	  * Entropy of the fitted NMF model [Park2007]
	  * Dominant basis components computation
	  * Explained variance
	  * Feature score computation representing its specificity to basis vectors [Park2007]
	  * Computation of most basis specific features for basis vectors [Park2007]
	  * Purity [Park2007]
	  * Residual sum of squares - can be used for rank estimate [Hutchins2008], [Frigyesi2008]
	  * Sparseness [Hoyer2004]
	  * Cophenetic correlation coefficient of consensus matrix - can be used for rank estimate [Brunet2004]
	  * Dispersion [Park2007]
	  * Factorization rank estimation
	  * Selected matrix factorization method specific



### Plans for Future


General plan for future releases of MF library is to alleviate the usage for non-technical users, increase library stability and provide comprehensive visualization methods. Specifically, in algorithm sense addition of the following could be provided.



	  * Extending Bayesian methods with variational BD and linearly constrained BD.
	  * Adaptation of the PMF model to interval-valued matrices.
	  * Nonnegative matrix approximation. Multiplicative iterative schema.



### Usage






    
    <span class="c"># Import MF library entry point for factorization</span>
    <span class="kn">import</span> <span class="nn">mf</span>
    
    <span class="kn">from</span> <span class="nn">scipy.sparse</span> <span class="kn">import</span> csr_matrix
    <span class="kn">from</span> <span class="nn">scipy</span> <span class="kn">import</span> array
    <span class="kn">from</span> <span class="nn">numpy</span> <span class="kn">import</span> dot
    <span class="c"># We will try to factorize sparse matrix. Construct sparse matrix in CSR format.</span>
    V <span class="o">=</span> csr_matrix<span class="p">((</span>array<span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">]),</span>array<span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">]),</span>array<span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">6</span><span class="p">])),</span>shape<span class="o">=</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
    
    <span class="c"># Run Standard NMF rank 4 algorithm</span>
    <span class="c"># Returned object is fitted factorization model. </span>
    <span class="c"># Through it user can access quality and performance measures.</span>
    fit <span class="o">=</span> mf<span class="o">.</span>mf<span class="p">(</span>V<span class="p">,</span>method <span class="o">=</span> <span class="s">"nmf"</span><span class="p">,</span>max_iter <span class="o">=</span> <span class="mi">30</span><span class="p">,</span>rank <span class="o">=</span> <span class="mi">4</span><span class="p">,</span>update <span class="o">=</span> <span class="s">'divergence'</span><span class="p">,</span>objective <span class="o">=</span> <span class="s">'div'</span><span class="p">)</span>
    
    <span class="c"># Basis matrix. It is sparse, as input V was sparse as well.</span>
    W <span class="o">=</span> fit<span class="o">.</span>basis<span class="p">()</span>
    <span class="k">print</span> <span class="s">"Basis matrix</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> W<span class="o">.</span>todense<span class="p">()</span>
    
    <span class="c"># Mixture matrix. We print this tiny matrix in dense format.</span>
    H <span class="o">=</span> fit<span class="o">.</span>coef<span class="p">()</span>
    <span class="k">print</span> <span class="s">"Coef</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> H<span class="o">.</span>todense<span class="p">()</span>
    
    <span class="c"># Return the loss function according to Kullback-Leibler divergence. </span>
    <span class="k">print</span> <span class="s">"Distance Kullback-Leibler"</span><span class="p">,</span> fit<span class="o">.</span>distance<span class="p">(</span>metric <span class="o">=</span> <span class="s">"kl"</span><span class="p">)</span>
    
    <span class="c"># Compute generic set of measures to evaluate the quality of the factorization</span>
    sm <span class="o">=</span> fit<span class="o">.</span>summary<span class="p">()</span>
    <span class="c"># Print sparseness (Hoyer, 2004) of basis and mixture matrix</span>
    <span class="k">print</span> <span class="s">"Sparseness W: </span><span class="si">%5.3f</span><span class="s">  H: </span><span class="si">%5.3f</span><span class="s">"</span> <span class="o">%</span> <span class="p">(</span>sm<span class="p">[</span><span class="s">'sparseness'</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> sm<span class="p">[</span><span class="s">'sparseness'</span><span class="p">][</span><span class="mi">1</span><span class="p">])</span>
    <span class="c"># Print actual number of iterations performed</span>
    <span class="k">print</span> <span class="s">"Iterations"</span><span class="p">,</span> sm<span class="p">[</span><span class="s">'n_iter'</span><span class="p">]</span>
    
    <span class="c"># Print estimate of target matrix V</span>
    <span class="k">print</span> <span class="s">"Estimate</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> dot<span class="p">(</span>W<span class="o">.</span>todense<span class="p">(),</span> H<span class="o">.</span>todense<span class="p">())</span>







### Examples


Examples with visualized results in bioinformatics, image processing, text analysis, recommendation systems are provided in [Examples section of Documentation.](http://helikoid.si/mf/)

Figure 1: Reordered consensus matrix generated for rank = 2 on Leukemia data set.

[![](/images/2011/09/04/all_aml_consensus2.png__160x160_q95_crop.png)
](http://blog.biolab.si/wp-content/uploads/2011/09/04/all_aml_consensus2.png)

Figure 2: Interpretation of NMF - Divergence basis vectors on Medlars data set. By considering the highest weighted terms in this vector, we can assign a label or topic to basis vector W1, a user might attach the label liver to basis vector W1.

[![](/images/2011/09/04/documents_basisw1.png__160x160_q95_crop.png)
](http://blog.biolab.si/wp-content/uploads/2011/09/04/documents_basisw1.png)

Figure 3: Basis images of LSNMF obtained after 500 iterations on original face images. The bases trained by LSNMF are additive but not spatially localized for representation of faces.

[![](/images/2011/09/04/orl_faces_500_iters_large_lsnmf.png__160x160_q95_crop.png)
](http://blog.biolab.si/wp-content/uploads/2011/09/04/orl_faces_500_iters_large_lsnmf.png)


### Relevant Links





	  * [Extensive published documentation with examples](http://helikoid.si/mf/)
	  * [Orange wiki MF Project page](http://orange.biolab.si/trac/wiki/MatrixFactorization)
	  * [Github repository with source code](https://github.com/marinkaz/mf)
	  * [Short presentation in pdf format of MF library](http://helikoid.si/mf/GSoC_MF.pdf)

