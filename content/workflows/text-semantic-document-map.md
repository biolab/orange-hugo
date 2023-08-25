+++
title= "Semantic Document Map"
images =  ["/workflows/images/text-semantic-document-map.png"]
type = "workflows"
blog_link =  ""
video = ""
download = "text-semantic-word-map.ows"
workflows = ["Text Mining"]
weight = 652
+++

Document maps may reveal clusters of documents with semantically similar content. Here we show a workflow that loads the corpus, performs some text preprocessing and embeds the documents in the vector space using the fastText deep model. The t-SNE widget reveals the document map, where we can select a set of documents and then explore them in Corpus Viewer or characterize them in the display of the most frequent words in the Word Cloud.
