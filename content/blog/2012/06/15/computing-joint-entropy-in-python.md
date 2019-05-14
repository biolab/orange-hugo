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

    
    def entropy(*X):
    return = np.sum(-p * np.log2(p) if p > 0 else 0 for p in
        (np.mean(reduce(np.logical_and, (predictions == c for predictions, c in zip(X, classes))))
            for classes in itertools.product(*[set(x) for x in X])))





I started with the method to compute the entropy of a single variable. Input is a numpy array with discrete values (either integers or strings).




    
    import numpy as np

    def entropy(X):
        probs = [np.mean(X == c) for c in set(X)]
        return np.sum(-p * np.log2(p) for p in probs)

In my next version I extended it to compute the joint entropy of two variables:

    
    def entropy(X, Y):
    probs = []
    for c1 in set(X):
        for c2 in set(Y):
            probs.append(np.mean(np.logical_and(X == c1, Y == c2)))

    return np.sum(-p * np.log2(p) for p in probs)


Now wait a minute, it looks like we have a recursion here. I couldn't stop myself of writing en extended general function to compute the joint entropy of n variables.
  
    def entropy(*X, **kwargs):
        predictions = parse_arg(X[0])
        H = kwargs["H"] if "H" in kwargs else 0
        v = kwargs["v"] if "v" in kwargs else np.array([True] * len(predictions))

        for c in set(predictions):
            if len(X) > 1:
                H = entropy(*X[1:], v=np.logical_and(v, predictions == c), H=H)
            else:
                p = np.mean(np.logical_and(v, predictions == c))
                H += -p * np.log2(p) if p > 0 else 0
        return H


It was the ugliest recursive function I've ever written. I couldn't stop coding, I was hooked. Besides, this method was slow as hell and I need a faster version for my reasearch. I need my data tommorow, not next month. I googled if Python has something that would help me deal with the recursive part. I fould this great method: itertools.product, I's just what we need. It takes lists and returns a cartesian product of their values. It's the "nested for loops" in one function.

   
    def entropy(*X):
        n_insctances = len(X[0])
        H = 0
        for classes in itertools.product(*[set(x) for x in X]):
            v = np.array([True] * n_insctances)
            for predictions, c in zip(X, classes):
                v = np.logical_and(v, predictions == c)
            p = np.mean(v)
            H += -p * np.log2(p) if p > 0 else 0
        return H

No resursion, but still slow. It's time to rewrite loops to the Python-like style. As a sharp eye has already noticed, the second for loop with the np.logical_and inside is perfect for the reduce method.
    
    def entropy(*X):
        n_insctances = len(X[0])
        H = 0
        for classes in itertools.product(*[set(x) for x in X]):
            v = reduce(np.logical_and, (predictions, c for predictions, c in zip(X, classes)))
            p = np.mean(v)
            H += -p * np.log2(p) if p > 0 else 0
        return H

Now, we have to remove just one more list comprehension and we have a beautiful, general, and super fast joint etropy method.

   
    def entropy(*X):
        return = np.sum(-p * np.log2(p) if p > 0 else 0 for p in
            (np.mean(reduce(np.logical_and, (predictions == c for predictions, c in zip(X, classes))))
                for classes in itertools.product(*[set(x) for x in X])))
