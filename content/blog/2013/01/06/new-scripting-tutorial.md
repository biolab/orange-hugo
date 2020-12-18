+++
author="BLAZ"
date= '2013-01-06 19:30:00+00:00'
draft= false
title="New scripting tutorial"
type="blog"
blog=["documentation" ,"examples" ,"tutorial" ]
+++

Orange just got a new, completely rewritten [scripting tutorial](http://docs.orange.biolab.si/latest/tutorial/rst). The tutorial uses Orange class hierarchy as introduced for version 2.5. The tutorial is supposed to be a gentle introduction in Orange scripting. It includes many examples, from really simple ones to those more complex. To give you a hint about the later, here is the code for learner with feature subset selection from:

    
    class SmallLearner(Orange.classification.PyLearner):
        def __init__(self, base_learner=Orange.classification.bayes.NaiveLearner,
                     name='small', m=5):
            self.name = name
            self.m   = m
            self.base_learner = base_learner

        def __call__(self, data, weight=None):
            gain = Orange.feature.scoring.InfoGain()
            m = min(self.m, len(data.domain.features))
            best = [f for _, f in sorted((gain(x, data), x) \
              for x in data.domain.features)[-m:]]
            domain = Orange.data.Domain(best + [data.domain.class_var])

            model = self.base_learner(Orange.data.Table(domain, data), weight)
            return Orange.classification.PyClassifier(classifier=model, name=self.name)





The tutorial was first written for Python 2.3. Since, Python and Orange have changed a lot. And so did I. Most of the for loops have become one-liners, list and dictionary comprehension have become a must, and many new and great libraries have emerged. The (boring) tutorial code that used to read


    
        c = [0] * len(data.domain.classVar.values)
        for e in data:
            c[int(e.getclass())] += 1
        print "Instances: ", len(data), "total",
        r = [0.] * len(c)
        for i in range(len(c)):
            r[i] = c[i] * 100. / len(data)
        for i in range(len(data.domain.classVar.values)):
            print ", %d(%4.1f%s) with class %s" % 
                (c[i], r[i], '%', data.domain.classVar.values[i]),
        print



is now replaced with

    
    print Counter(str(d.get_class()) for d in data)



Ok. Pretty print is missing, but that, if not in the same line, could be done in another one.

For now, the tutorial focuses on data input and output, classification and regression. We plan to use other sections, but you can also give us a hint if there are any you would wish to be included.
