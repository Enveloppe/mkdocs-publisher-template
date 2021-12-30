var p_search = /\[{2}(.*)\]{2}/gi
var ht = document.querySelectorAll('p');
for (var i = 0; i<ht.length;i++) {
  const found_p = ht[i].innerHTML.match(p_search);
	if (found_p && !found_p[0].includes('code')) {
		var not_found= "<div class='not_found'>" + found_p + '</div>';
		ht[i].innerHTML=ht[i].innerHTML.replace(found_p, not_found);
	}
}
document.innerHTML = ht;

var p_img = /\.+\\/gi
var img = document.querySelectorAll('img');
var links = document.querySelector("link[rel='icon']").href.replace('assets/logo/favicons.png', '');
for (var i = 0; i < img.length; i++){
  img[i].attributes.src.nodeValue=img[i].attributes.src.nodeValue.replace(/\.+\\/, links)
}