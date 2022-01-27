


var p_search = /\.\.%5C/gi
var ht = document.querySelectorAll('a');
for (var i = 0; i < ht.length; i++) {
    var link = ht[i].href.match(p_search);
    if (link) {
        const newItem = document.createElement('div');
        newItem.innerHTML = ht[i].innerHTML;
        newItem.classList.add('not_found');
        ht[i].parentNode.replaceChild(newItem, ht[i]);
    }
}


var p_img = /\.+\\/gi
var img = document.querySelectorAll('img');
var links = document.querySelector("link[rel='icon']").href.replace('assets/logo/favicons.png', '');
for (var i = 0; i < img.length; i++) {
    (img[i].attributes.src.nodeValue)
    img[i].attributes.src.nodeValue = img[i].attributes.src.nodeValue.replace(/\.+\\/, links)
    if (img[i].alt.match(/\|?\d+$/)) {
        img[i].width = img[i].alt.match(/\|?\d+$/)[0].replace('|', '')
    }
}


var scr=/\^(.*)/gi;
for (var i = 0; i <ht.length;i++){
    const fp=ht[i].innerHTML.match(scr)
	if (fp) {
        ht[i].innerHTML=ht[i].innerHTML.replace(fp, '')
    }
}
document.innerHTML = ht;
