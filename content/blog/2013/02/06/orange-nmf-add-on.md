+++
author="BIOLAB"
date= '2013-02-06 13:47:00+00:00'
draft= false
title="Orange NMF add-on"
type="blog"
categories=["addons" ,"matrixfactorization" ,"nmf" ]
+++

[Nimfa](http://nimfa.biolab.si), a Python library for non-negative matrix factorization (NMF), which was part of Orange GSoC program back in 2011 got its own [add-on](http://orange.biolab.si/addons/). 

Nimfa provides a plethora of initialization and factorization algorithms, quality measures along with examples on real-world and synthetic data sets. However, until now the analysis was possible only through Python scripting. A recent increase of interest in NMF techniques motivated Fajwel Fogel (a PhD student from INRIA, Paris, [SIERRA team](http://www.di.ens.fr/sierra/)) to design and implement several widgets that deal with missing data in target matrices, their normalizations, viewing and assessing the quality of matrix factors returned by different matrix factorization algorithms. He also provided an implementation of robust singular value decomposition (rSVD). All NMF methods call Nimfa library.

![](/images/2013/02/06/nmf-addon-demo.png__1000x1000_q95.jpg)


Above is shown a simple scenario in Orange that applies [LSNMF algorithm from Nimfa](http://nimfa.biolab.si/nimfa.methods.factorization.lsnmf.html) to decompose a non-negative target matrix and visualizes its basis matrix (W) and coefficient matrix (H) as heat maps. NMF finds a parts-based representation of the data due to the fact that only additive, not subtractive, combinations are allowed, which results in improved interpretability of matrix factors. That is possible because non-negativity constraints are imposed in the NMF model in contrast to SVD, PCA and ICA, which provide only holistic representations. The effect can be easily seen if we investigate heat maps produced by the scenario above. Below are shown the target, basis and coefficient matrices (from left to right, top down), respectively.  

![](/images/2013/02/06/lsnmf-addon-demo.png__432x826_q95_crop_upscale.jpg)

