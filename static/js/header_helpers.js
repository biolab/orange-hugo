
let expanded_search = false;


function header_search(){

  let donate_div = document.querySelector(".donate-button");
  let header_search_div = document.querySelector(".header-search-input");


  if(expanded_search == false){
    expanded_search = true;

      //donate_div.hidden = true;
      header_search_div.hidden = false;
      document.getElementById('search-header').focus();

    return;
  }


  	var param = document.getElementById('search-header').value;

    if(param == ""){
      expanded_search = false;
      //donate_div.hidden = false;


      header_search_div.hidden = true;
    } else {
      let query = "?q=" + param;
      let url = window.location.protocol + "//" + window.location.host + "/search/" + query;
      window.location = url;
    }

}


function check_key_header(e) {
	if (e.keyCode == 13) {
		header_search();
	}
}
