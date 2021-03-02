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


document.getElementById("all_tab").addEventListener("click", function() {
	change_res("all");
}, false);

document.getElementById("blog_tab").addEventListener("click", function() {
	change_res("blog");
}, false);

document.getElementById("workflows_tab").addEventListener("click", function() {
	change_res("workflows");
}, false);

document.getElementById("widgets_tab").addEventListener("click", function() {
	change_res("widgets");
}, false);




let search_results = null;

let showing = 0;

let showing_type = "";

let inited_lunr = false;

let widget_json = null;


jQuery(document).ready(function() {
	'use strict';
	// read widget.json file
	$.getJSON("/widgets.json", function(json) {
		widget_json = json;
		console.log(json);
	})
});

function show_more() {
	if (search_results != null) {
		showing += 10;
		if (showing_type == "all") {
			show_all(showing);
		}
		if (showing_type == "blog") {
			show_blog(showing);
		}

		if (showing_type == "widgets") {
			show_widget(showing);
		}
		console.log(showing);
	}

}

function change_res(type) {
	console.log(type);
	console.log(showing_type);
	if (type != showing_type) {
		document.querySelector(".nav-tabs").querySelector(".active").classList.remove("active");

		showing_type = type;
		showing = 0;
		remove_all_results();
		if (type == "all") {
			document.getElementById("all_tab").parentNode.classList.add("active");
			show_all(showing);
		}

		if (type == "blog") {
			document.getElementById("blog_tab").parentNode.classList.add("active");
			show_blog(showing);
		}

		if (type == "workflows") {
			document.getElementById("workflows_tab").parentNode.classList.add("active");
			//show_all(showing);
		}

		if (type == "widgets") {
			document.getElementById("widgets_tab").parentNode.classList.add("active");
			show_widget(showing);
		}
	}
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
	showing_type = "";
	var nav_tabs = document.getElementById("nav-tabs-results");
	remove_all_results();
	hide_all_results();
	nav_tabs.hidden = true;

	var param = document.getElementById('search-input').value;

	var num_results = document.querySelector(".num_results");
	if (!inited_lunr) {
		initLunr();
		inited_lunr = true;

	}

	search_results = search(param);


	if (search_results.length == 0) {
		num_results.textContent = `No results found for “${param}”`;
		return;
	} else if (search_results.length == 1)
		num_results.textContent = `Found one result for “${param}”`;
	else
		num_results.textContent = `Found ${search_results.length} results for “${param}”`;


	nav_tabs.removeAttribute("hidden");
	showing = 0;
	change_res("all");

}

function hide_all_results() {
	let result_box = document.querySelector(".all-results");
	let result_box_blog = document.querySelector(".blog-results");
	let result_box_workflows = document.querySelector(".workflows-results");
	let result_box_widgets = document.querySelector(".widgets-results");

	result_box.hidden = true;
	result_box_blog.hidden = true;
	result_box_workflows.hidden = true;
	result_box_widgets.hidden = true;

}

function remove_all_results() {
	let result_box = document.querySelector(".all-results");
	let result_box_blog = document.querySelector(".blog-results");
	let result_box_workflows = document.querySelector(".workflows-results");
	let result_box_widgets = document.querySelector(".widgets-results");

	while (result_box.firstChild)
		result_box.removeChild(result_box.firstChild);

	while (result_box_blog.firstChild)
		result_box_blog.removeChild(result_box_blog.firstChild);

	while (result_box_workflows.firstChild)
		result_box_workflows.removeChild(result_box_workflows.firstChild);

	while (result_box_widgets.firstChild)
		result_box_widgets.removeChild(result_box_widgets.firstChild);
}


function show_all(num_show) {
	hide_all_results();
	let result_box = document.querySelector(".all-results");
	result_box.removeAttribute("hidden");
	let showed = 0;
	if (num_show == 0) {
		remove_all_results();
	}




	console.log(search_results);
	for (var result of search_results) {
		console.log(showed);

		if ((result.kind === "page" || true) && result.kind != "term") {
			console.log(result.type);
			let element = null;
			if (result.type === "blog") {
				element = render_blog(result);

			} else if (result.type === "workflows") {
				element = render_widget(result);
			} else if (result.type === "widget-catalog") {
				element = render_widget(result);
			} else if (result.type === "contact" || result.type === "citation" || result.type === "widget-catalog" || result.type === "license" || result.type === "privacy" || result.type === "faq") {
				element = render_other(result);
				console.log(result);

			}
			if (element != null) {
				showed += 1;
				if (showed >= num_show && showed < num_show + 10) {
					result_box.appendChild(element);
				}
				if (showed > num_show + 10) {
					return;
				}
			}
		}
	}
}



function show_blog(num_show) {
	hide_all_results()
	let result_box = document.querySelector(".blog-results");
	result_box.removeAttribute("hidden");
	let showed = 0;
	if (num_show == 0) {
		remove_all_results();
	}

	for (var result of search_results) {


		if (result.kind === "page") {

			let element = null;
			if (result.type === "blog") {
				element = render_blog(result);

				showed += 1;
				if (showed >= num_show && showed < num_show + 10) {
					console.log(result.kind);
					result_box.appendChild(element);
				}
			}

			if (showed > num_show + 10) {
				return;
			}
		}
	}
}

function show_widget(num_show) {
	hide_all_results()
	let result_box = document.querySelector(".widgets-results");
	result_box.removeAttribute("hidden");
	let showed = 0;
	if (num_show == 0) {
		remove_all_results();
	}

	for (var result of search_results) {


		if (result.kind === "page") {

			let element = null;
			if (result.type === "widget-catalog") {
				element = render_widget(result);

				showed += 1;
				if (showed >= num_show && showed < num_show + 10) {
					console.log(result.kind);
					result_box.appendChild(element);
				}
			}

			if (showed > num_show + 10) {
				return;
			}
		}
	}
}





// returns HTML
function render_blog(content) {
	let template = document.getElementById("result-blog");
	let template_image = document.getElementById("result-blog-image");

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
function render_workflow(content) {
	let template = document.getElementById("result-example");
	let render = template.content.cloneNode(true);

	render.querySelector(".summary-title-link").href = content.uri;
	render.querySelector(".read-more-link").href = content.uri;
	//element.querySelector(".result-link").href = result.uri;

	render.querySelector(".result-title").textContent = content.title;
	render.querySelector(".summary").textContent = truncate(content.content, 50);

	return render;

}

// returns HTML
function render_widget(content) {

	let template = document.getElementById("result-widget");
	let render = template.content.cloneNode(true);

  let json_data = null;
	if(widget_json != null){
		for(let cat of widget_json){
    	for(let wid of cat[1]){
      	//console.log(wid);
      	if(wid.title === content.title){
        	console.log("FOKJEA");
					console.log(wid);
        	render.querySelector(".image").src = "/"+wid.icon;
      	}
    	}
  	}
	}

	render.querySelector(".summary-title-link").href = content.uri;
	render.querySelector(".read-more-link").href = content.uri;
	//element.querySelector(".result-link").href = result.uri;

	render.querySelector(".result-title").textContent = content.title;
	render.querySelector(".summary").textContent = truncate(content.content, 50);

	return render;

}


// returns HTML
function render_other(content) {
		let template_regular = document.getElementById("result-regular");
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
