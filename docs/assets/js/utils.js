function heading(str) {
    var title_regex = /\[{2}(.*)\|(.*)/gi
    str_list = str.split(']]')
    for (var i = 0; i < str_list.length; i++) {
        truc = str_list[i].match(title_regex);
        if (truc) {
            title = truc.join().split('|')[1]
            title = '[[' + title
            str = str.replace(str_list[i].match(title_regex), title)

        }
    }
    return str
}

var p_search = /!?\[{2}(.*)\]{2}/gi
var ht = document.querySelectorAll('article.md-content__inner.md-typeset > *:not(.highlight)');
for (var i = 0; i < ht.length; i++) {
    const found_p = ht[i].innerHTML.match(p_search);
    if (found_p) {
        founded = heading(found_p[0])
        var not_found = founded.replace(/]]/gi, '</div>');
        not_found = not_found.replace(/\[\[/gi, '<div class="not_found">')
        not_found = not_found.replace('!', '')
        ht[i].innerHTML = ht[i].innerHTML.replace(found_p, not_found);
    }
}
document.innerHTML = ht;

var p_img = /\.+\\/gi
var img = document.querySelectorAll('img');
var links = document.querySelector("link[rel='icon']").href.replace('assets/logo/favicons.png', '');
for (var i = 0; i < img.length; i++) {
    img[i].attributes.src.nodeValue = img[i].attributes.src.nodeValue.replace(/\.+\\/, links)
    if (img[i].alt.match(/\|?\d+$/)) {
        img[i].width = img[i].alt.match(/\|?\d+$/)[0].replace('|', '')
    }
}

var wikilink = document.querySelectorAll('a')
for (var i = 0; i < wikilink.length; i++) {
    wikilink[i].href = wikilink[i].href.replace(/(.*)\/\.+\//, links)
    wikilink[i].href = wikilink[i].href.replace('.md', '')
}
