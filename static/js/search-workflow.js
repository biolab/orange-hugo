var lunrIndex, pagesIndex;
// var lunr = require('lunr');

function endsWith(str, suffix) {
    return str.indexOf(suffix, str.length - suffix.length) !== -1;
}

// Initialize lunrjs using our generated index file
function initLunr() {
    if (!endsWith(baseurl,"/")){
        baseurl = baseurl+'/'
    };

    // First retrieve the index file
    $.getJSON(baseurl +"workflow.json")
        .done(function(index) {
            pagesIndex =   index;
            // Set up lunrjs by declaring the fields we use
            // Also provide their boost level for the ranking

            lunrIndex = lunr(function () {
            this.ref("uri");
            this.field('title', {
                boost: 50
            });
            this.field('tags', {
                boost: 30
            });
            this.field('content', {
                boost: 1
            });
              pagesIndex.forEach(function (doc) {
                this.add(doc)
              }, this)
            })
            

            // Feed lunr with each file and let lunr actually index them
            // pagesIndex.forEach(function(page) {
            //     lunrIndex.add(page);
            // });
            // lunrIndex.pipeline.remove(lunrIndex.stemmer)
        })
        .fail(function(jqxhr, textStatus, error) {
            var err = textStatus + ", " + error;
            console.error("Error getting Hugo index file:", err);
        });
}

/**
 * Trigger a search in lunr and transform the result
 *
 * @param  {String} query
 * @return {Array}  results
 */
function search_tag(tag, search_param) {

    var res = lunrIndex.search('tags:'+ tag)

    var res2 = lunrIndex.search(search_param)
    var inter= res.filter(a => res2.some(b => a.ref === b.ref));  

    return inter.map(function(result) {
            return pagesIndex.filter(function(page) {
                return page.uri === result.ref;
            })[0];
            });
    

}
function search(query_s){
    return lunrIndex.search(query_s).map(function(result) {
            return pagesIndex.filter(function(page) {
                return page.uri === result.ref;
            })[0];
        });
}


// Let's get started
initLunr();
