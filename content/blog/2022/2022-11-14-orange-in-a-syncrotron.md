+++
author = "Marko Toplak"
date = "2022-11-14"
draft = false
title = "Orange in a synchrotron"
type = "blog"
thumbImage = "/blog_img/2022/20221101_inside.jpg"
frontPageImage = "/blog_img/2022/20221101_inside_s.jpg"
blog = ["workshop", "addons"]
shortExcerpt = "Workshop about spectral data analysis in a synchrotron."
longExcerpt = "We taught a three-day workshop on Orange for spectral data in UK’s national synchrotron, Diamond Light Source."
+++

Orange has a cousin. His name is [Quasar](https://quasar.codes/). Quasar extends Orange with methods for the analysis of spectral data and allows researchers to use a single interactive workflow-based tool for acquisition method-specific data processing, machine learning, and visualization. Quasar was born from a collaboration between the University of Ljubljana and two synchrotrons, Soleil (France) and Elettra (Italy). Users from synchrotrons form an important group of Quasar users.

A [synchrotron light source](https://en.wikipedia.org/wiki/Synchrotron_light_source) is a particle accelerator where the beam travels in a closed loop, and wherever it bends, it generates electromagnetic radiation (or light). This light is captured on the beamlines, which can, for example, use infrared light to learn about the chemical composition of the samples or x-rays to learn about the samples' internal structure. The synchrotron light has a very tight beam and is very strong, which makes synchrotrons a very flexible light source. I sometimes imagine them as very big but high-quality light bulbs. A small section of the Diamond synchrotron's storage ring, where the beam travels around a 560-meter-long loop, is shown below.

{{% figure src="/blog_img/2022/20221101_diamond-storage.jpg" %}}

We led [a three-day workshop](https://www.diamond.ac.uk/Home/Events/2022/Infrared-microspectroscopy-analysis-training---QUASAR-software0.html) on using Orange (or Quasar) for the analysis of spectral data from infrared beamlines. The workshop took place in the UK’s national synchrotron, Diamond Light Source. We taught a class of around 40 participants with my colleague, Ferenc Borondics from the Soleil synchrotron.

{{% figure src="/blog_img/2022/20221101_lectures.jpg" %}}

The workshop spanned both spectroscopy-specific topics like baseline correction, normalization, EMSC, or differentiation, and more general topics such as multivariate statistical and machine learning methods, and visualization. We concluded with my favourite topic: common errors in supervised machine learning. My favourite workflow was the following. 

{{% figure src="/blog_img/2022/20220103_different-classes-hair.png" %}}

The above workflow demonstrates that even a (very) slight bias added to random classes introduces enough signal into the data so that the classes become perfectly separable. The added bias was very small, similar in size to mixing solutions of slightly different concentrations when preparing samples for measurement. We hope that we managed to show our students how easy it is to make an error that can invalidate our analysis.

I also learned two important facts about England on this trip: (1) pubs are the places to go for dinner, and, (2) English food tastes good.

{{% figure src="/blog_img/2022/20221103_pub.jpg" %}}
