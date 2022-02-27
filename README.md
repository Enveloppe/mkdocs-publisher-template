<p align="center">
	<a href="https://github.com/Mara-Li/mkdocs_obsidian_publish"><img src="https://img.shields.io/github/license/Mara-Li/YAFPA-python"></img></a>
	<a href="https://www.python.org/"><img src="https://img.shields.io/pypi/pyversions/obs2mk"></img></a>
	<a href="https://pypi.org/project/obs2mk/"><img src="https://img.shields.io/pypi/v/obs2mk"></img></a>
	<a href="https://obsidian.md/"><img src="https://img.shields.io/badge/Auxiliary%20Tool-Obsidian-blueviolet"></img></a>
	<a href="https://github.com/Mara-Li/mkdocs_obsidian_template/wiki/Q&A/"><img src="https://img.shields.io/badge/-Q%26A-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMTIgMkM2LjQ4NiAyIDIgNi40ODYgMiAxMnM0LjQ4NiAxMCAxMCAxMCAxMC00LjQ4NiAxMC0xMFMxNy41MTQgMiAxMiAyem0wIDE4Yy00LjQxMSAwLTgtMy41ODktOC04czMuNTg5LTggOC04IDggMy41ODkgOCA4LTMuNTg5IDgtOCA4eiIvPjxwYXRoIGQ9Ik0xMSAxMWgydjZoLTJ6bTAtNGgydjJoLTJ6Ii8+PC9zdmc+"></img></a>
</p>

![](screenshot/script_demo.gif)

# Mkdocs Obsidian
Mkdocs Obsidian is an association between a python script and a Material mkdocs template to get a personal wiki site based on your Obsidian Vault.


<p align="center"><a href="https://mara-li.github.io/mkdocs_obsidian_template/">Mkdocs Obsidian Template </a> </p>

<p align="center"><a href="https://www.mara-li.fr">Owlly Seed (My Blog ; In French)</a></p>

<details><summary><u><b>Screenshot</u></b> </summary>

![image_1](screenshot/image_1.png)
![image_2](screenshot/image_2.png)
![image_3](screenshot/image_3.png)
![image_4](screenshot/image_4.png)

</details>

## Pre-requiries

<
# Prerequisites
You need : 
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- Optional *(Windows)*: [Windows Terminal](https://docs.microsoft.com/fr-fr/windows/terminal/)

## Quick installation tutorial
1. Click on [use this template](https://github.com/Mara-Li/mkdocs_obsidian_template/generate) ; Use the name of your choice.
2. Click on [code](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories) → SSH ; Copy the link
3. Run : 
```bash
git clone [[PASTE THE LINK HERE]] publish_blog
cd publish_blog
pip install obs2mk --upgrade
pip install -r requirements.txt
```

# Creating the blog
## Customization
In your new `publish_blog` folder, you will spot a `mkdocs.yml`. This file allows you to customize your blog! The most important to edit :
1. `site_name` 
2. `site_description`
3. `site_url` (critical) : By default, it's `https://github_username.io/repo_name`

To edit the logo and the favicon, first put the chosen file in `assets/logo`, and change `logo` and `favicon` :
1. `logo: assets/logo/logo_name.png`
2. `favicon: assets/logo/favicon.png`

You can customize :
- font
- Color scheme, palette, icons 
- Language
[Check the documentation to get more information](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

You don't need to touch everything in `features ; markdown_extensions…`

## Local testing
To locally build template, you need to run `pip install -r requirements.txt` after cloning : 
```bash
git clone git@github.com:your_username/your_blog_name.git
cd your_blog_name
pip install -r requirements.txt
```
To run locally the blog : `mkdocs serve`

The blog will be published through [GitHub Page](https://pages.github.com/) using the `gh-page` branch. Everything is already configured by the template for that.

# Obs2mk : Obsidian to Mkdocs
The script's goal is to move an authorized file (or multiple authorized file) from your Obsidian's vault to your blog's repository. It will :
- Move linked image in `docs/assets/img`
- Convert the **code block** [Admonition](https://github.com/valentine195/obsidian-admonition) to [material Admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)[^1]
- Remove Obsidian's comments as `%% comments %%`
- Copy the file in `docs` or a specific folder structure. 
- Add custom CSS based on markdown attribute or tags ([CM6 Live Preview](https://github.com/nothingislost/obsidian-cm6-attributes) ; [Markdown Attribute](https://github.com/valentine195/obsidian-markdown-attributes) and [Contextual Typography](https://github.com/mgmeyers/obsidian-contextual-typography)). 

Furthermore, it will also carry :
- Of the support of [Folder Note — Pagination Indexes](#folder-note)
- Copy a link to the blog converted file

## File's front matter
The script relies on the front matter** of the notes you want to publish. 
1. `share: true` allow publishing the file[^2]
2. `category` to choose where the file will be after conversion ; allowing categorization for the blog. 
    - `category: false` will **hide** the file from navigation.
    - `category: hidden` will do the same.
    - `category: folder1/folder2/` will move the file in `folder2`, under `folder1`
    - `category: folder1/folder2/filename` will rename the file `index` and allow support of [section's index page](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#section-index-pages)
    You can customize the folder with [Awesome Pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)
3. `update: false` prevent to update the file after the first publishing
4. `description` : Add a description to the file (for meta-tag sharing)[^3]
5. `title` : Change the title in the navigation.
6. `image` : Add an image for meta-tags sharing.[^4] It needs to be the name of the file, as `image.png`. 

## Usage
The script can be use :
- Directly in Obsidian, using [Obsidian Shell Commands](https://github.com/Taitava/obsidian-shellcommands) (see [Obsidian Shell's configuration](#obsidian-shell-configuration))
- In [Terminal](#terminal).
The platform supported are :
- macOS, Linux and Windows (referred as 'Computer')
- [IOS](#ios) (with [Pyto](https://pyto.app) and/or [a-shell](https://holzschu.github.io/a-Shell_iOS/) with [Working Copy](https://workingcopyapp.com/))

### Configuration
At the first run, you will be asked to configure some key and specific path.
1. <u>Vault</u> : Use the file dialog to choose your vault folder.
2. <u>Publish repository folder : </u> As vault path, use the file dialog.
3. <u>share</u> : You can change the `share` key. By default, it's `share`
4. <u>Index key:</u> Support for citation of [pagination index pages](#folder-note). By default, it uses `(i)`
5. <u>Default blog folder:</u> By default, the notes will be in `docs/notes` but you can change that, or use `/` for root. 

### Terminal 
```bash
usage: obs2mk [-h] [--git | --mobile] [--meta] [--keep] [--config] [--force] [--filepath FILEPATH | --ignore]

Create file in docs and relative folder, move image in assets, convert admonition code_blocks, add links and push.

options:
  -h, --help            show this help message and exit
  --git, --g, --G       No commit and no push to git
  --mobile, --shortcuts, --s, --S
                        Use mobile shortcuts fonction without push.
  --meta, --m, --M      Update the frontmatter with link
  --keep, --k, --K      Keep deleted file from vault and removed shared file
  --config, --c, --C    Edit the config file
  --force, --d, --D     Force conversion - only work if path not specified
  --filepath FILEPATH, --f FILEPATH
                        Filepath of the file you want to convert
  --ignore, --ignore-share, --no-share, --i, --vault
                        Convert the entire vault without relying on share state.
```

#### Share one file : `obs2mk --f FILEPATH`
It will :
- Update the `share` state in original file
- Convert one file, regardless of what is the `share` state.

#### Share all file : `obs2mk`
You can share multiple documents at once with scanning your Vault, looking for the `share: true`. It will convert automatically these files.
Only file with modification since the last sharing will be updated.

#### Options
1. `--vault` : This option allows sharing the entire vault, regardless of the `share` key.
2. `--mobile` : See [iOS](#ios) for more information.
3. `--git` : Forbid push ;
4. `--keep` : Keep deleted file from vault and removed shared file.
5. `--force` : Force conversion (in case the vault's file and blog's file are the same)
6. `--config` : Reconfigure the environment (path and key)

### Obsidian Shell Configuration
You could create :
1. A command to publish everything : alias `Publish` with `obs2mk --obsidian`
2. A command to publish one specific file : alias `Publish {{title}}` with `obs2mk --obsidian --f {{file_path:absolute}}`
3. Event shortcuts for file menu event : `Publish {{event_file_name}}`: `obs2mk --obsidian --f "{{event_file_path:absolute}}
4. Folder Note event (folder menu event): `Publish {{event_folder_name}}`: `obs2mk --obsidian --f "{{event_folder_path:relative}}\{{event_folder_name}}.md"`
You can create a button with :
- [Customizable Sidebar](https://github.com/phibr0/obsidian-customizable-sidebar)    
- [Obsidian Customizable Menu](https://github.com/kzhovn/obsidian-customizable-menu)

The file will be in `site-packages/mkdocs_obsidian`  

### IOS
The script support IOS using :
- [a-shell](https://holzschu.github.io/a-Shell_iOS/) (Free)  
- [Pyto](https://pyto.app) ($3 lite version / $10 complete version) [^5]
- [Working Copy](https://workingcopyapp.com/) (Free for student / $19)

>The option `mobile` will **never** push. You need to use Working Copy to push the converted file.

You can :
1. Share the entire vault : `obs2mk --mobile`
2. Share a specific file, using its name : `obs2mk --mobile --f "filename"`.[^6] This option can be used especially with [Shortcuts](https://support.apple.com/guide/shortcuts/welcome/ios)

Mobile supports all previous option, including `--ignore`.

### Customization
- You can prevent the script to share file in specific folder, with editing `folder` list in `exclude.yml`
- You can prevent the script to **delete** some file with editing `file` list in the same file.
- You can, also, create some CSS customization with hashtag, with editing `docs/assets/css/custom_attributes.css`. See [Custom Attribute](#custom-attribute-example) for some example.


# Blog : Customization
## Custom attribute example
You can create [Inline Markdown Attribute](https://python-markdown.github.io/extensions/attr_list/) using hashtags in Obsidian. For example, to align some text to right :
1. Add 
```css
#right {
 display: inline-block;
 width: 100%;
 text-align: right;
 font-weight: normal;
}
```
2. Add `#right` on the last part of a line : 
```md
Lorem ipsum dolor sit amet, consectetur adipiscing elit. In mollis, libero porttitor gravida accumsan, justo metus pulvinar nulla, vitae dictum odio ligula non nisl. Vivamus id venenatis nulla. Nullam sed euismod ligula. Pellentesque tempor elit felis, lobortis vulputate risus gravida et. Curabitur auctor sed libero nec consectetur. Nam placerat rhoncus risus, euismod sagittis eros bibendum ac. Maecenas tellus libero, porttitor ac purus sit amet, viverra suscipit dolor. Proin id nisl velit. Ut at tincidunt libero, ac pharetra mi. Integer non luctus nisi. #right
```
It will appear as: 
![](screenshot/custom_attribute.png)

## Folder note
You can create a folder note if you use a `category` front matter key that have the last folder with the same name as the file. For example : 
`category: folder1/folder2/filename`. The file `filename` will be renamed `index` and the folder will be named `filename`.

To support the citation and link to these page, you need to use an index key (cf [configuration](#configuration)).

Some examples of citation and their transformation : 
| In Obsidian               | In Publish            |
| ------------------------- | --------------------- |
| `[[Real File|(i) Alias]]` | `[[index|Alias]]`     |
| `[[Real File|(i)]]`       | `[[index|Real File]]` |
| `[(i) Alias](Real file) ` | `[Alias](index)`      |
| `[(i)](real file)`        | `[real file](index)`  | 

# Obsidian
**Some useful plugin to support the script** : 
- [Metacopy](https://github.com/Mara-Li/obsidian-metacopy)
- [Obsidian Shell](https://github.com/Taitava/obsidian-shellcommands) (cf [Obsidian Shell](#obsidian-shell-configuration))
- [Customizable Sidebar](https://github.com/phibr0/obsidian-customizable-sidebar)    
- [Obsidian Customizable Menu](https://github.com/kzhovn/obsidian-customizable-menu)
- [Alx Folder Note](https://github.com/aidenlx/alx-folder-note)
- Custom Attribute :
	- [CM6 Live Preview](https://github.com/nothingislost/obsidian-cm6-attributes) ; 
	- [Markdown Attribute](https://github.com/valentine195/obsidian-markdown-attributes)
	- [Contextual Typography](https://github.com/mgmeyers/obsidian-contextual-typography) 

### Metacopy
Using [metacopy](https://github.com/Mara-Li/obsidian-metacopy) you can quickly copy a link to a shared page, without using this option (so, yes, the script does not edit your source file !).   
To create a link, you need to configure :  
 1. `category` in `key`  
 2. Add your `set_url` in `base link`  
 3. Add `category` in `key link`  
  
Also, you can remove the metacopy from your file menu using a key, so you can activate metacopy only for `share: true`. Metacopy also support the [folder note](#folder-note).   
  
The final configuration of metacopy for mkdocs_obsidian will be :  
![](screenshot/metacopy3.png)  
![](screenshot/metacopy2.png)  
  
So, in the end, a menu will appear on file with `share: true` and a `category` configured. This menu is on the left click and the file-menu. You can quickly copy a link from there, like a Google or notion sharing link!  
  
[Here is a demo](https://www.loom.com/share/88c64da2ba194e219578d5911fb8e08d) :   
  
[![click to get a video !](screenshot/demo.gif)](https://www.loom.com/share/88c64da2ba194e219578d5911fb8e08d)

## Front matter template
```yml
title:  
share: 
description:  
category:
```

# Limitation
- The plugin rely a lot on filename, without regarding the folder. Please use **unique naming** and use the `title` key if you need to.
- The plugin will not delete the `index` files (cf [Folder Note](#folder-note))
- The script can be long on big vault.
- The script will not manually move the file if you change a `category` : you need to delete it manually to prevent duplicate.
- ⚠️You must use `shortlinks` in Obsidian configuration. 

# TLDR
1. Install / update with `pip install obs2mk --upgrade`
2. Add `share: true` in front matter
3. Customize the `category` key in front matter
4. Run the script `obs2mk`

If you have more question, don't forget to read the [Q&A](https://github.com/Mara-Li/mkdocs_obsidian_template/wiki/Q&A/) !



[^1]: No support for nested admonition and [Microsoft Document Syntax](https://github.com/valentine195/obsidian-admonition#microsoft-document-syntax)
[^2]: This key can be configured 
[^3]: **Meta tags** are snippets of text that describe a page’s content; the meta tags don’t appear on the page itself, but only in the page’s source code. Meta tags are essentially little content descriptors that help tell search engines what a web page is about. [Source](https://www.wordstream.com/meta-tags)
[^4]: Using Pyto you need to add the writing authorization for your vault and blog repository. You can access it in parameters > Runtime. Also, the configuration file will be in `site_package` directly.
[^5]: Beware, if it exists a file with the same name, it will take the first found. 