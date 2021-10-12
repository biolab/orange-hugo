function header_search() {
  let headerSearchInput = document.querySelector(".header-search-input");

  if (!headerSearchInput) {
    return;
  }

  if (window.innerWidth <= 990) {
    window.location = window.location.protocol
      + "//"
      + window.location.host
      + "/search/";
    return;
  }

  if(headerSearchInput.hidden){
    document.addEventListener('keydown', hideHeaderSearchInputOnEscape)
    headerSearchInput.hidden = false;
    headerSearchInput.focus();

    return;
  }
  
  let param = headerSearchInput.value;

  if(param === ''){
    hideHeaderSearchInput();
  } else {
    let query = "?q=" + param;
    let url = window.location.protocol + "//" + window.location.host + "/search/" + query;
    window.location = url;
  }

  function hideHeaderSearchInputOnEscape(event) { 
    if (event && event.key !== "Escape") {
      return;
    }

    hideHeaderSearchInput(undefined, true);
  }

  function hideHeaderSearchInput(event, force) {
    if (!force && headerSearchInput.value !== '') {
      return;
    }

    headerSearchInput.hidden = true;
    headerSearchInput.value = '';
    document.removeEventListener('keydown', hideHeaderSearchInputOnEscape)
  }
}

function check_key_header(e) {
	if (e.keyCode == 13) {
		header_search();
	}
}
