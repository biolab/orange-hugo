+++
author = "Janez Demšar"
date = "2023-04-24"
draft = false
title = "Živjo, Orange!"
type = "blog"
thumbImage = "/blog_img/2023/2023-03-31-zemljevid.png"
frontPageImage = "/blog_img/2023/2023-03-31-zemljevid.png"
blog = ["gui"]
shortExcerpt = "Orange speaks Slovenian!"
longExcerpt = "Orange speaks Slovenian!"
+++

{{< window-screenshot src="/blog_img/2023/2023-03-31-zemljevid.png" >}} 


The Slovenian language exhibits a complicated grammar, featuring three genders and four plural terms, along with a substantial amount of declensions and conjugations, (and unreasonable number of exceptions) that require all kinds of agreements between nouns, adjectives and verbs. It is mastered (unfortunatelly poorly, in too many cases) by some two million native speakers ... and a growing number of programs.

Among them, finally, Orange.

Why? Primarily because Orange is already being used in higher education, while its use in younger population is often hindered by language barrier. This became particularly prononunced in the context of [Pumice](https://pumice.si) and related projects that aim to introduce AI as a tool for data exploration within different school subjects from K4 on.

## Orange in Slovenian

It took over six months to translate Orange, starting with the development of Trubar, a general tool for translating modern Python code. Traditional translation tools, such as gettext, are not compatible with modern string interpolation and require modifications to the source code, which we wanted to avoid.

The next step was to translate the actual program. The core of Orange contains approximately 15,000 strings, each of which needed to be either translated or marked as programmatic, meaning it was internal to the program and not visible to the user. Additionally, there were several thousand more strings from other parts and selected libraries that required translation.

After using the translated version for some time, we manually tested each widget and created a test release, only to discover that it failed on the first widget we tried. This prompted us to run unittests on the Slovenian version, which proved to be challenging since over 10% of the tests failed because they expected English language terms. The test files included an additional 15,000 strings, but only a small number required translations. Many of the tests had to be modified by changing the text code or even the source code of the widgets themselves. During this process, we also discovered a bug or two in Orange.

After three days of frantic work to catch a deadline we imposed on ourselves as part of project Pumice -- and still feeling uneasy despite all manual and unit testing, we finally released a beta version of Slovenian Orange [for Windows](http://download.biolab.si/download/files/slo/Orange3-3.35.0.dev0%2B1bec1ca-Miniconda-x86_64.exe) and [for macOS](http://download.biolab.si/download/files/slo/Orange3-3.35.0.dev0%2B1bec1ca-Python3.9.12.dmg).

If you speak Slovenian, you can give it a try. 

## Is this it?

No, this is obviously not it, yet. Having a separate release for each language is not the best practice. Add-ons cannot be downloaded separately, We don't have anything for Linux. But it's a huge step forward.

## Orange for other languages?

Sure. With the initial work completed, translating Orange to other languages should be significantly easier. Although we have not yet prepared general instructions, if you are genuinely interested in translating to another language, we would be happy to assist you.

{{< window-screenshot src="/blog_img/2023/2023-03-31-orange-slo.png" >}} 
