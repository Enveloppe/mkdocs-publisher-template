The script relies on the front matter** of the notes you want to publish. 
1. `share: true` allow publishing the file[^1]
2. `category` to choose where the file will be after conversion ; allowing categorization for the blog.[^2]
    - `category: false` will **hide** the file from navigation.
    - `category: hidden` will do the same.
    - `category: folder1/folder2/` will move the file in `folder2`, under `folder1`
    - `category: folder1/folder2/filename` will rename the file `index` and allow support of [section's index page](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#section-index-pages)  
3. `update: false` prevent to update the file after the first publication
4. `description` : Add a description to the file (for meta-tag sharing)[^3]
5. `title` : Change the title in the navigation.
6. `image` : Add an image for meta-tags sharing.[^3] It needs to be the name of the file, as `image.png`. 

[^1]: This key can be configured 
[^2]: You can customize the folder with [Awesome Pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)
[^3]: **Meta tags** are snippets of text that describe a page’s content; the meta tags don’t appear on the page itself, but only in the page’s source code. Meta tags are essentially little content descriptors that help tell search engines what a web page is about. [Source](https://www.wordstream.com/meta-tags)