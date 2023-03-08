+++
title= "Semantic search"
images =  ["/workflow_images/text-semantic-search.png", "/workflow_images/text-semantic-search-widget.png"]
type = "workflows"
blog_link =  ""
video = ""
download = "text-semantic-search.ows"
workflows = ["Text Mining"]
weight = 655
+++

We can find relevant parts of a document by searching for exact words or parts of documents with similar meanings. The Semantic Viewer widget in this workflow searches for pertinent sentences of the documents by comparing the meaning of words from the Word List widget to the meaning of sentences in the text via SBERT text embeddings. The widget ranks documents by scores measuring their relevance, shows selected documents, and highlights the relevant parts.