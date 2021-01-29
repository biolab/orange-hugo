var lunrIndex, searchIndex;

function endsWith(str, suffix) {
	return str.indexOf(suffix, str.length - suffix.length) !== -1;
}

// Initialize lunrjs using our generated index file
function initLunr() {


	// First retrieve the index file
	$.getJSON("/search.json")
		.done(function (searchindex) {
			searchIndex = searchindex;
			console.log(searchIndex);
			// Set up lunrjs by declaring the fields we use
			// Also provide their boost level for the ranking
			lunrIndex = lunr(function () {
				this.ref("uri");
				this.field('title', {
					boost: 50
				});
				this.field('categories', {
					boost: 30
				});
				this.field('longExcerpt', {
					boost: 10
				});
				this.field('type', {
					boost: 70
				});
				this.field('author', {
					boost: 10
				});
				this.field('content', {
					boost: 1
				});

				searchIndex.forEach(function (doc) {
					this.add(doc)
				}, this)


			})


		})
		// Feed lunr with each file and let lunr actually index them
		// pagesIndex.forEach(function(page) {
		//     lunrIndex.add(page);
		// });
		// lunrIndex.pipeline.remove(lunrIndex.stemmer)

		.fail(function (jqxhr, textStatus, error) {
			var err = textStatus + ", " + error;
			console.error("Error getting Hugo index file:", err);
		});
}


function search_categories(category, search_param) {
	var search_by_categories = lunrIndex.search('categories:' + category)

	var search_by_params = lunrIndex.search(search_param)
	var intersection_of_results = search_by_categories.filter(a => search_by_params.some(b => a.ref === b.ref));

	return intersection_of_results.map(function (result) {
		return pagesIndex.filter(function (page) {
			return page.uri === result.ref;
		})[0];
	});


}


/**
 * Trigger a search in lunr and transform the result
 *
 * @param  {String} query
 * @return {Array}  results
 */
function search(query) {
	// Find the item in our index corresponding to the lunr one to have more info
	let res = [];
	lunrIndex.search(query).map(function (result) {

		console.log(result);
		searchIndex.forEach(function (entry) {
			if (entry.uri === result.ref) {
				console.log(entry);
				res.push(entry);
			}
		});
	});
	console.log(res);
	return res;
}

// function search_content(){
//     console.log($("#search-by").get(0).value);
//     var param = $("#search-by").get(0).value;
//     var results  = search(param);
//     console.log(results);
//     // document.getElementById('search-by').value;
// }

// Let's get started
initLunr();
