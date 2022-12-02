function UrlExists(url, type_url) {
    let ref = "";
    let title = "";
    if (type_url === 0) {
        ref = url.href
        title = url.title
    }
    else if (type_url === 1) {
        ref = url.src
        title = url.alt
    }
    if (ref.match(/index$/)) {
        ref = ref.replace(/index$/, '')
    }
    if (ref.includes('%5C')) {
        ref = ref.replace(/%5C/g, '/')
    }
    if (type_url === 0) {
        url.href = ref
        url.title = title
        if (title.length === 0) {
            title = url.innerText
            url.title = title
        }
    }
    else if (type_url === 1) {
        url.src = ref
        url.alt = title
    }

    var http = new XMLHttpRequest();
    http.open('GET', ref, true);
    http.onload = function (e) {
        if (http.status == '404') {
            const newItem = document.createElement('div');
            newItem.innerHTML = title;
            newItem.classList.add('not_found');
            url.parentNode.replaceChild(newItem, url);
        }
        else {
            return true;
        }
    }
    http.send()
}


var p_search = /\.{2}\//gi
const not_found = []
var ht = document.querySelectorAll('a');
for (var i = 0; i < ht.length; i++) {
    var link = UrlExists(ht[i], 0);
}

var p_img = /\.+\\/gi
var img = document.querySelectorAll('img');
for (var i = 0; i < img.length; i++) {
    (img[i].attributes.src.nodeValue)
    if (img[i].alt.match(/\|\d+$/)) {
        img[i].width = img[i].alt.match(/\|\d+$/)[0].replace('|', '')
    }
    var link = UrlExists(img[i], 1);
}



var ht = document.querySelectorAll('article.md-content__inner.md-typeset > *:not(.highlight)');
var scr = /\^(.*)/gi;
for (var i = 0; i < ht.length; i++) {
    const fp = ht[i].innerHTML.match(scr)
    if (fp) {
        ht[i].innerHTML = ht[i].innerHTML.replace(fp, '')
    }
}
document.innerHTML = ht;

var cite = document.querySelectorAll('.citation');
if (cite) {
    for (var i = 0; i < cite.length; i++) {
        var img = cite[i].innerHTML.match(/!?(\[{2}|\[).*(\]{2}|\))/gi)
        if (img) {
            for (var j = 0; j < img.length; j++) {
                cite[i].innerHTML = cite[i].innerHTML.replace(img[j], '')
            }
            if (cite[i].innerText.trim().length < 2) {
                cite[i].style.display = 'none';
            }
        }
    }
}


//get iframe from graph.md
// check if page is graph.md

if (window.location.href.includes('graph')) {
    var iframe = document.querySelector('iframe');
    //get mkdocs theme
    theme=document.querySelector('[data-md-color-scheme]');
    //if mkdocs theme is dark, change iframe theme to dark
    if (theme.getAttribute('data-md-color-scheme') === 'default') {
        iframe.setAttribute('class', 'light')
    } else {
        iframe.setAttribute('class', 'dark')
    }
    //create mutation observer to change iframe theme when mkdocs theme changes
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            if (mutation.type === 'attributes') {
                iframe.setAttribute('class', mkDocsChirpyTranslator[theme.dataset.mdColorScheme])
                }
            })
        })
    //observe mkdocs theme
    observer.observe(theme, {
        attributes: true,
        attributeFilter: ['data-md-color-scheme'],
    })
}

window.onload = function () {
    let frameElement = document.querySelector('iframe');
    let doc = frameElement.contentDocument || frameElement.contentWindow.document;
    let css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = 'css/template/utils.css';
    css.type = 'text/css';
    doc.head.appendChild(css);
    theme = document.querySelector('[data-md-color-scheme]');
    if (theme.getAttribute('data-md-color-scheme') === 'default') {
        doc.body.setAttribute('class', 'light')
    }
    else {
        doc.body.setAttribute('class', 'dark')
    }
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            if (mutation.type === 'attributes') {
                doc.body.setAttribute('class', mkDocsChirpyTranslator[theme.dataset.mdColorScheme])
            }
        })
    }
    )
    observer.observe(theme, {
        attributes: true,
        attributeFilter: ['data-md-color-scheme'],
    })
}
