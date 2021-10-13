$(document).ready(function () {
  document.querySelector("#search-btn-js").addEventListener('mousedown', headerSearch);
})

function headerSearch() {
  let headerSearchInput = document.querySelector(".header-search-input");

  if (!headerSearchInput) {
    return;
  }

  if(headerSearchInput.hidden){
    document.addEventListener('keydown', hideHeaderSearchInputOnEscape);
    headerSearchInput.hidden = false;
    headerSearchInput.addEventListener('blur', hideHeaderSearchInput);

    setTimeout(focusInput, 0);
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

  function focusInput() {
    headerSearchInput.focus();
  }

  function hideHeaderSearchInputOnEscape(event) { 
    if (event && event.key !== "Escape") {
      return;
    }

    hideHeaderSearchInput(undefined, true);
  }

  function hideHeaderSearchInput(event, force) {
    if (!event && !force && headerSearchInput.value !== '') {
      return;
    }

    headerSearchInput.hidden = true;
    headerSearchInput.value = '';
    document.removeEventListener('keydown', hideHeaderSearchInputOnEscape)
    headerSearchInput.removeEventListener('blur', hideHeaderSearchInput)
  }
}

function check_key_header(e) {
	if (e.keyCode == 13) {
		headerSearch();
	}
}
