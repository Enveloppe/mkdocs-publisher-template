const blogURL = location.origin ;
let position = ['top', 'right', 'bottom', 'left'];
try {
    const tip = tippy(`.md-content a[href^="${blogURL}"]`, {
        content:'',
        allowHTML: true,
        animation: 'scale-subtle',
        theme: 'translucent',
        followCursor: true,
        arrow: false,
        placement: position[Math.floor(Math.random() * position.length)],
        onShow(instance) {
            fetch(instance.reference.href)
                .then(response => response.text())
                .then(html => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    let firstPara = doc.querySelector('article');
                    //broken link in first para
                    const brokenImage = firstPara.querySelectorAll('img');
                    if (brokenImage) {
                        for (let i = 0; i < brokenImage.length; i++) {
                            const encodedImage = brokenImage[i];
                            encodedImage.src = decodeURI(decodeURI(encodedImage.src));
                            //replace broken image with encoded image in first para
                        }
                    }
                    const element1 = document.querySelector(`[id^="tippy"]`);
                    if (element1) {
                        element1.classList.add('tippy')
                    }
                    const partOfText = instance.reference.href.replace(/.*#/, '#');
                    if (partOfText.startsWith('#')) {
                        firstPara = doc.querySelector(`[id="${partOfText.replace('#', '')}"]`);
                        
                        if (firstPara.tagName.startsWith('H')) {
                            firstPara = firstPara.nextElementSibling;
                        }
                        else {
                            firstPara = firstPara.innerText.replaceAll('↩', '').replaceAll('¶', '');
                        }
                        instance.popper.style.height = 'auto';
                    }
                    else {
                        const height = Math.floor(firstPara.innerText.split(' ').length / 100)
                        if (height <5 && height > 3) {
                            instance.popper.style.height = `50%`;
                        } if (height < 3) {
                            instance.popper.style.height = `auto`;
                        } else if (height > 5) {
                            instance.popper.style.height = `${height - 5}%`;
                        }
                    }
                    instance.popper.placement = position[Math.floor(Math.random() * position.length)];
                    instance.setContent(firstPara);
                    
                })
                .catch(error => {
                    console.log(error);
                    instance.setContent('Error');
                });
        }
    });
} catch {
    console.log('tippy error, ignore it');
}
