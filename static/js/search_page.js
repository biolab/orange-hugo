/*
	workflows screenshots
	- v smeri examples
	- slika in spodej naslov

	blog
	- naslov in spodej kratek opis



	citation, contact, license, privacy

	getting started, faq - sta posebna

	Samo navaden rezultat


	 */


let search_results = null;

let showing = 0;

function show_more() {
	showing += 10;
	show_all(showing);
	console.log(showing);

}

function check_key(e) {
	if (e.keyCode == 13) {
		search_content();
	} else if (e.keyCode == 8) {
		if (document.getElementById('search-input').value.length <= 1) {
			$("#post_nor").show();
			$("#search-results").hide();
		}
	}
}

function search_content() {
	search_results = null;

	var nav_tabs = document.getElementById("nav-tabs-results");

	nav_tabs.hidden = true;

	var param = document.getElementById('search-input').value;

	var num_results = document.querySelector(".num_results");

	initLunr();

	search_results = search(param);


	if (search_results.length == 0) {
		num_results.textContent = `No results found for “${param}”`;
		return;
	} else if (search_results.length == 1)
		num_results.textContent = `Found one result for “${param}”`;
	else
		num_results.textContent = `Found ${search_results.length} results for “${param}”`;


	nav_tabs.removeAttribute("hidden");

	show_all(0);


}



function show_all(num_show) {
	let result_box = document.querySelector(".all-results");

	let showed = 0;
	if (num_show == 0) {
		result_box.removeAttribute("hidden");

		while (result_box.firstChild)
			result_box.removeChild(result_box.firstChild);
	}

	var template_regular = document.getElementById("result-regular");
	var template_example = document.getElementById("result-example");
	var template_blog = document.getElementById("result-blog");
	var template_blog_image = document.getElementById("result-blog-image");
	console.log(search_results);
	for (var result of search_results) {
		console.log(showed);

		if (result.kind === "page" || true) {
      console.log(result.type);
			let element = null;
			if (result.type === "blog") {
				//element = render_blog(template_blog, template_blog_image, result);

			} else if(result.type === "contact" || result.type === "citation" || result.type === "license" || result.type === "privacy"  || result.type === "faq") {
        element = render_other(template_regular, result);

			}
      if(element != null){
			showed += 1;
			if (showed >= num_show && showed < num_show + 10) {
				result_box.appendChild(element);
			}
      if(showed > num_show + 10){
        return;
      }
		}
  }
	}
}


// returns HTML
function render_blog(template, template_image, content) {

	let render = template.content.cloneNode(true);
	if (content.thumbImage != null) {
		render = template_image.content.cloneNode(true);
		render.querySelector(".image").src = content.thumbImage;
		render.querySelector(".image").href = content.uri;
	}
	render.querySelector(".summary-title-link").href = content.uri;
	render.querySelector(".read-more-link").href = content.uri;
	//element.querySelector(".result-link").href = result.uri;

	render.querySelector(".result-title").textContent = content.title;
	render.querySelector(".summary").textContent = truncate(content.content, 50);

	return render;

}


// returns HTML
function render_workflow(template, content) {


}

// returns HTML
function render_widget(template, content) {


}


// returns HTML
function render_other(template, content) {

  let render = template.content.cloneNode(true);

  render.querySelector(".summary-title-link").href = content.uri;
  render.querySelector(".read-more-link").href = content.uri;
  //element.querySelector(".result-link").href = result.uri;

  render.querySelector(".result-title").textContent = content.title;
  render.querySelector(".summary").textContent = truncate(content.content, 50);

  return render;


}

function truncate(text, minWords) {
	var match;
	var result = "";
	var wordCount = 0;
	var regexp = /(\S+)(\s*)/g;
	while (match = regexp.exec(text)) {
		wordCount++;
		if (wordCount <= minWords)
			result += match[0];
		else {
			var char1 = match[1][match[1].length - 1];
			var char2 = match[2][0];
			if (/[.?!"]/.test(char1) || char2 == "\n") {
				result += match[1];
				break;
			} else
				result += match[0];
		}
	}
	return result;
}
