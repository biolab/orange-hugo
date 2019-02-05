+++
author="BIOLAB"
date= '2011-06-24 22:10:00+00:00'
draft= false
title="'Orange GSoC: MF Techniques for Data Mining'"
type="blog"
categories=["gsoc" ,"matrixfactorization" ]
tags=["gsoc" ,"matrixfactorization" ]

+++

I am one of three students who are working on GSoC projects for Orange this year. The objective of the project Matrix Factorization Techniques for Data Mining is to provide the Orange community with a unified and efficient interface to matrix factorization algorithms and methods. 

For that purpose I have been developing a library which will include a number of published factorization algorithms and initialization methods and will facilitate combinations of these to produce new strategies. Extensive documentation with working examples that demonstrate applications, commonly used benchmark data and possibly some visualization methods will be provided to help with the interpretation and comprehension of the factorization results. 

Main factorization techniques and their variations included in the library are:   * family of nonnegative matrix factorization algorithms (NMF), including Brunet NMF, sparse NMF, non-smooth NMF, least-squares NMF, local Fisher NMF;   * probabilistic factorization (PMF) and its sparse variant (PSMF);   * Bayesian decomposition (BD);   * iterated conditional modes (ICM) algorithm. 

Different multiplicative and update algorithms for NMF will be analyzed which minimize least-squares error or generalized Kullback-Leibler divergence. 

For those interested some more information with details about algorithms is available at [project home page.](http://orange.biolab.si/trac/intertrac/wiki%3AMatrixFactorization)

There is still much work to do but I have been enjoying at it and I am looking forward to continuing with the project. 

Thanks to the Orange team and mentor prof. dr. Blaz Zupan for support and advice.
