[![GitHub license](https://img.shields.io/github/license/Mara-Li/YAFPA-python)](https://github.com/Mara-Li/YAFPA-python)
[![PyPI](https://img.shields.io/pypi/v/YAFPA)](https://pypi.org/project/yafpa/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/YAFPA)
![PyPI - Status](https://img.shields.io/pypi/status/YAFPA)
![](https://img.shields.io/badge/Auxiliary%20Tool-Obsidian-blueviolet)

# Mkdocs Obsidian
Mkdocs Obsidian is an association between a python script and a Material mkdocs template to get a personal wiki site based on your Obsidian Vault.

## Pre-requiries
- [Python](https://www.python.org/) and Pip
- [Mkdocs](https://www.mkdocs.org/getting-started/) : `pip install mkdocs`
- [Material Mkdocs](https://squidfunk.github.io/mkdocs-material/getting-started/) using `pip install mkdocs-material`
- [Mermaid2](https://github.com/fralau/mkdocs-mermaid2-plugin) with `pip install mkdocs-mermaid2-plugin`.
- [Roamlinks](https://github.com/Jackiexiao/mkdocs-roamlinks-plugin) : `pip install mkdocs-roamlinks-plugin`
- [mkdocs-obsidian](https://pypi.org/project/obs2mk/) : `pip install obs2mk`

## Get started
First, copy the template in [Github](https://github.com/Mara-Li/mkdocs_obsidian_template). To make it your, you need to change, in `mkdocs.yml`
- `site_name`,
- `site_description` 
- `site_url`
- The logo and favicons
- If you want, the palette, use [color scheme from material](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/) and edit `scheme` and `accent`.

The material's theme includes a lot of parameters and personnalization, so don't forget to check to make the site your ! Also there is a hundred of plug-ins ("extension") for mkdocs so don't hesitate to give an eyes! [You will found a lot here](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins).

To try your site without online use `mkdocs serve`.
You can publish your website using [Github Page](https://pages.github.com/) using the `gh-page` branch. This branch is pulled by the `.workflow` file, so don't worry about it.

Now you have two choice : move the file you want in `docs` (and the subfolder you want) or you can use `Mkdocs_Obsidian`.

## Obsidian compatibility
So, with the configuration I done, the mkdocs support :
- Folder note : the file need to be named "index" (instead of the name of the folder)
- Admonition
- Wikilinks and relative links
- Highlight and tilde markdown
- Mathjax and Mermaid 
- Custom Attribute, as [CM6 Attribute (with tags)](https://github.com/nothingislost/obsidian-cm6-attributes/releases), [Markdown Attribute](https://github.com/valentine195/obsidian-markdown-attributes) and [Contextual Typography (with tags)](https://github.com/mgmeyers/obsidian-contextual-typography).

I didn't found a way to embed file with wikilinks for the moment. Because of the strange behavior of roamlinks, these embedded file will be rendered as image. The script will care of this bug. 

# Mkdocs Obsidian
## Utilities and interest
*A vast party of the script is taken from my previous project, YAFPA*

The script will care about some things you can forgot :
- Moving your image in assets ;
- Change the admonition from the plugin to material admonition (mainly for codeblocks)
- Remove Obsidian comment (`%% text %%`) 
- **Create a folder structure** based on the `category` key. Without it, the note will be created in `docs/notes`. 
It will also add, in the **original file** a link to the blog. Using [metacopy](https://github.com/Mara-Li/obsidian-metacopy) you can quick copy this link. 
⚠️If the script crash for any reason at the moment where the script update the frontmatter, you can lost some file. If you don't want to have your YAML updated, your can use the key `--meta`.

## Usage
```powershell
usage: obs2mk [-h] [--git] [--meta] [--keep] [--config] [--force | --filepath FILEPATH]

Create file in docs and relative folder, move image in assets, convert admonition code_blocks, add links and push.

optional arguments:
  -h, --help            show this help message and exit
  --git, --g, --G       No commit and no push to git
  --meta, --m, --M      Don't update the frontmatter
  --keep, --k, --K      Keep deleted file from vault and removed shared file
  --config, --c, --C    Edit the config file
  --force, --d, --D     Force conversion - only work if path not specified
  --filepath FILEPATH, --f FILEPATH
                        Filepath of the file you want to convert
```

At the first start of the script, it will ask you :
- The **absolute path** of your vault and blog in your PC.
- The key you want to use to share the file (default : `share`).
This file will be in your `site_package` folder.

You can reconfigure the option with `obs2mk --config`.

By default, the script will remove all file that doesn't exist in the vault, and file where you remove the share (`share: false`, or removed the key). You can keep all these file with ``--k``. 

### Share one file
To share **only** one file : `obs2mk --f FILEPATH`. It will :
- Update the state status in original file (`share: true`)
- Re-write the file if exist or create it in the folder you put in `category` 
This option will pull the file no matter what is the `share` state.

### Share "all" files
You can share multiple documents using the `share: true` key, in frontmatter. The script will scan your entire vault and automatically convert the file with this key.
There is two option :
- By default, the script will compare with the older version and write only if changement are detected.
- Using `--force` will force the re-writing. 

## Customization
There are some files to customize the script :
- You can create [custom admonition with material docs](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) and adding the name in `custom_admonition.yml`. 
- You can completely exclude some folder of your vault with `exclude_folder.yml`. You can exclude specific path as `folder1/subfolderA` etc.
- Using the `\docs\assets\css\custom_attributes.css` you can create specific aspect for your tags and it also add compatibility with CM6 Attribute and Contextual Typography. 

## Limitation
- **Nested admonition doesn't work for the moment.** I don't use it a lot, but if you want, you could improve the script or create a mkdocs plugin to care of that. 
- The script will not delete the file and folder if you change the `category` key. Beware of this. 
- Share "all" can be long on big vault. 
- File with same name can have some problem while scanning, because I don't keep your folder structure. Please, beware of this ! Don't forget you can use `title` if you want a specific name (and this name already exist). 
- Bloc citation doesn't work, the script will care of that. 
- Embed file (citation and # too) doesn't work, the script will also care about it !

## Support
The script can work on any plateform that support python. The script don't use Cpython, so don't worry about it for IOS.

### IOS 
Using :
- [a-shell](https://holzschu.github.io/a-Shell_iOS/) (Free)
- [Working Copy](https://workingcopyapp.com/)
You can update the docs.

First, in a-shell, run `pickFolder` and choose the folder of your vault, and rerun `pickFolder` to choose the folder where are the blog data (you need to clone with [Working Copy](https://workingcopyapp.com/))
After, do `showmarks` and copy the two path in any note app. Check if the path is not broken because of the paste!
You can also do :
```bash
cd 
showmarks > bookmark
vim bookmark
```

Here is a blank sheet to help you if you want to manually write / edit it :
```
vault=
blog_path=
blog=
share=
```
With :
- `vault`: Vault Absolute Path
- `blog_path` : Blog repository absolute path
- `blog` : Blog link (same as `site_url` from `mkdocs.yml`)
- `share` : your wanted share key ; by default : `share`

Before running the shortcuts, you need to install all requirements, aka :
```
pip install obs2mk
obs2mk --config
```

After, in a-shell, you can use the same option as on a PC.

### Obsidian
→ Please use Wikilinks with "short links" (I BEG YOU)
You can integrate the script within obsidian using the nice plugin [Obsidian ShellCommands](https://github.com/Taitava/obsidian-shellcommands).

You could create two commands :
1. `share all` : `obs2mk`
2. `share one` : `obs2mk --f {{file_path:absolute}}`

You can use :
- [Customizable Sidebar](https://github.com/phibr0/obsidian-customizable-sidebar)
- [Obsidian Customizable Menu](https://github.com/kzhovn/obsidian-customizable-menu)
To have a button to share your file directly in Obsidian !
# Frontmatter and option
## Script

The script need one key, to share the file. You can configure the key in the configuration of the script.

If you want a folder structure in `docs`, you need to use the `category` keys, with the form of `path/path`. You can also block a file to update with `update: false`.

## Mkdocs
Material give you the possibility to add SEO tags with :
- `description`  
- `title` (will change too the title in the navigation)
- `image`: Add an image (don't forget the format) / Need to be a relative link.

## Template
So, the final frontmatter template is :
```yaml
---
title:
share:
description:
category:
---
```
