+++
title= "Text Clustering"
images =  ["/workflow_images/text-clustering.png"]
type = "workflows"
blog =  ""
video = "https://youtu.be/rH_vQxQL6oM"
download = "620-text-clustering.ows"
workflows = ["Text Mining", "Clustering", "Tokenization"]
weight = 620
+++

The workflow clusters Grimm's tales corpus. We start by preprocessing the data and constructing the bag of words matrix. Then we compute cosine distances between documents and use Hierarchical Clustering, which displays the dendrogram. We observe how well the type of the tale corresponds to the cluster in the MDS.
