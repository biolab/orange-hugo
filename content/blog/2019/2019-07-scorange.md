+++
author="Blaž Zupan"
date= '2019-07-25'
draft= false
title="Orange at ISMB/ECCB 2019"
type="blog"
# thumbImage will be displayed in the list of blogs
# the size of thumbImage should be 460 x 280
thumbImage = "/blog_img/2019/scorange-annotation-thumb.png"
# fronPageImage is displayed on the front page in the list of recent blogs
# the size of frontPageImage should be 460 x 280
frontPageImage = "/blog_img/2019/scorange-annotation-thumb.png"
categories=["education", "bioinformatics"]
shortExcerpt = "One of Orange's latest features is its add-on for single-cell data analytics."
# longExcerpt = ""
+++
Our entry to this year's largest bioinformatics conference was on the training of single-cell data analytics. We claim that with Orange and its new single-cell RNA analysis add-on, one can assemble a workshop to teach essential concepts from single-cell analytics in a single day.

{{% figure src="/blog_img/2019/scorange-martin-at-ismb.jpg" caption="" %}}
\

Single-cell genomics is driven on revolutionary technology from molecular biology that allows us to peek into inner workings of the individual cell. Single-cell datasets feature thousands of genes and cells and benefit from the analysis that integrates this data with other knowledge sources, like those on the classification of genes, lists of pathways, and sets of cell-type markers. To support such analysis, we have been developing a [single-cell add-on for Orange](https://github.com/biolab/orange3-single-cell). We are also experimenting with packing this add-on, the add-on for bioinformatics, and the rest of Orange within a stand-alone application called [scOrange](https://singlecell.biolab.si). Installation of scOrange comes with a preinstalled single-cell add-on and workflows and videos that are specific to this area of research. Our single-cell RNA analysis tool still uses Orange's widgets at the core, but additionally packs components for reading single-cell data, filtering cells and genes, preprocessing the data and handling peculiarities of single-cell analysis like batch effects and cell-type annotation. 

[ISMB/ECCB 2019](https://www.iscb.org/ismbeccb2019) is the largest and most prestigious bioinformatics conference. It joins the meetings of International and European and Society for Computational Biology. Martin Žagar, a post-doc at our Bioinformatics Lab in Ljubljana and responsible for much of developments in scOrange, presented [scOrange](https://singlecell.biolab.si) in light of its support for case-based teaching and hands-on workshops. During the talk, Martin showcased several scOrange's workflows. The one I liked best includes automatic annotation of cell-types in point-based visualizations.

{{% figure src="/blog_img/2019/scorange-automatic-annotation.png" width="80%" caption="" %}}



Martin's presentation was based on our ISMB/ECCB paper just published in Bioinformatics:

Martin Stražar,  Lan Žagar,  Jaka Kokošar,  Vesna Tanko,  Aleš Erjavec,  Pavlin G Poličar, Anže Starič,  Janez Demšar,  Gad Shaulsky,  Vilas Menon,  Andrew Lemire,  Anup Parikh, Blaž Zupan (2019) [scOrange—a tool for hands-on training of concepts from single-cell data analytics](https://academic.oup.com/bioinformatics/article/35/14/i4/5529249), Bioinformatics 35(14):i4–i12.
