function UrlExists(url, type_url) {
  let ref = "";
  let title = "";
  if (type_url === 0) {
    ref = url.href;
    title = url.title;
  } else if (type_url === 1) {
    ref = url.src;
    title = url.alt;
  }
  if (ref.match(/index$/)) {
    ref = ref.replace(/index$/, "");
  }
  if (ref.includes("%5C")) {
    ref = ref.replace(/%5C/g, "/");
  }
  ref = decodeURI(ref);
  if (type_url === 0) {
    url.href = ref;
    url.title = title;
    if (title.length === 0) {
      title = url.innerText;
      url.title = title;
    }
  } else if (type_url === 1) {
    url.src = ref;
    url.alt = title;
  }

  var http = new XMLHttpRequest();
  http.open("GET", ref, true);
  http.onload = function (e) {
    if (http.status == "404") {
      const newItem = document.createElement("div");
      newItem.innerHTML = title;
      newItem.classList.add("not_found");
      newItem.setAttribute("href", ref);
      try {
        url.parentNode.replaceChild(newItem, url);
      } catch (error) {
        // console.log(error)
      }
    } else {
      return true;
    }
  };
  http.send();
}

var p_search = /\.{2}\//gi;
const not_found = [];
var ht = document.querySelectorAll("a:not(img)");
for (var i = 0; i < ht.length; i++) {
  if (
    !ht[i].getElementsByTagName("img").length > 0 &&
    !ht[i].getElementsByTagName("svg").length > 0
  ) {
    var link = UrlExists(ht[i], 0);
  }
}

var p_img = /\.+\\/gi;
var img = document.querySelectorAll("img");
for (var i = 0; i < img.length; i++) {
  var link = UrlExists(img[i], 1);
}
