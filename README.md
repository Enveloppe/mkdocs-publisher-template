---
title: Configuration
share: true
---


# Configuration
## Mkdocs configuration

In your new `publish_blog` folder, you will spot a `mkdocs.yml`. This file allows you to customize your blog! The most important to edit :
1. `site_name` 
2. `site_description`
3. `site_url` (critical) : By default, it's `https://github_username.io/repo_name`[^1]

To edit the logo and the favicon, first put the chosen file in `assets/logo`, and change `logo` and `favicon` :
1. `logo: assets/meta/logo_name.png`
2. `favicon: assets/meta/favicon.png`

You can customize :
- Font
- Color scheme, palette, icons 
- Language  

[Check the documentation to get more information](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

You don't need to touch anything in `features` ; `markdown_extensions…`

### Plugins

The `mkdocs.yml` also contains the configuration for [Mkdocs Plugin](https://www.mkdocs.org/dev-guide/plugins/). If you add plugin, you **need** to add it to your `requirements.txt` because the build use it to construct the blog.

I included :
- [Ezlinks (from mkdocs-ezlinked-plugin)](https://pypi.org/project/mkdocs-ezlinked-plugin/) : to support directly wikilinks
- [Mermaid2](https://github.com/fralau/mkdocs-mermaid2-plugin)
- [Awesome pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)
- [Tooltipster-links (from mkdocs-preview-links-plugin)](https://github.com/Mara-Li/mkdocs-preview-links-plugin)
- [Embed File](https://github.com/Mara-Li/mkdocs_embed_file_plugins), to support embedding file as in Obsidian (with the `![](file)` or `![[file]]` syntax)
- [Git revision date localized](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin), to add a date listing 
- [Mkdocs Simple Hooks](https://pypi.org/project/mkdocs-simple-hooks/), to allow creating simple python script for mkdocs (including jinja template editing!). 
- [Mkdocs Encrypt Contents](https://github.com/CoinK0in/mkdocs-encryptcontent-plugin) will allow you to "hide" file in the site. [[Template/snippets and tools#Page encrypted|See here]] for more information.
- [Mkdocs Callout](https://pypi.org/project/mkdocs-callouts/)
- [Custom tags attributes](https://pypi.org/project/mkdocs-custom-tags-attributes/)

> [!info] Superfences & dataviewjs
> You will spot that I added a [`custom fences`](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) for dataviewjs. Sorry, dataviewjs is not currently supported by mkdocs nor Obsidian Publisher. This custom fences will hide every dataviewjs block. 
> It will, so, prevent display stange block in your markdown file. If you need to display it as code, change the language (like `js` for example).
---

## Local testing (*optional*)

To run locally the blog, you need to install the requirements and run `mkdocs serve`.
```
cd publish_blog
pip install -r requirements.txt
mkdocs serve
```
A little advice here : You could use a [conda](https://docs.conda.io/en/latest/) environment here (or a venv, but I don't like venv.). Just use this:
```bash
conda create -n Publisher python=3.10.4
conda activate Publisher
```
Just before the `pip install`!


---

# Deploy
## Through GitHub

The blog will be published through [GitHub Page](https://pages.github.com/) using the `gh-page` branch. 

> [!bug] I have the readme in place of my files!
> Check the `gh-pages` branch and activate it if necessary in `Settings` → `Pages`
> ![image](https://user-images.githubusercontent.com/30244939/166161220-973cee87-75eb-4b9f-b521-1c67d273def7.png)

> [!bug] The workflow doesn't run!
>  - Check the run and error in `Actions` 
>  - Check if the actions have the good write and read access in `settings → Actions → General → workflow permission` ![image](https://user-images.githubusercontent.com/30244939/166161294-0f4f70c2-fda5-4465-89b0-d6b1b5e6995d.png)
>> [!Warning] In case of worfklow problem
>> In the [issue #4](https://github.com/obsidianPublisher/obsidian-github-publisher/issues/4), we discover that sometimes, Github Actions refuse to run without reason. If this happend to you, please, contact the Github Support!

## Through Netlify

Netlify.app is a great tool to deploy your blog. It's a free service that allows you to deploy your blog on the web, and the build will be faster than GitHub Pages.

To deploy your blog, you can click here : [![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/ObsidianPublisher/obsidian-mkdocs-publisher-template)

Alternatively :
- Create an account on Netlify
- Add a new site using already existing repository.
  For configuration, use :
    - Leave blank for repository ;
    - Use `mkdocs build` for commands ;
    - Finally, use `site` as site directory.
![config_netlify](https://i.imgur.com/ESc9vLu.png)  
- Grab the `runtime.txt` or create a new environment variable with `PYTHON_VERSION` fixed at `3.8`.

To gain deploy time and bandswith, you need to desactivate the deploy preview. To do so, go in `settings` -> `build & deploy` -> `deploy preview` and uncheck the box.
![picture 1](https://i.imgur.com/DNS0DdX.png)  


> [!note]
> It can be possible that you need to remove your `gh-pages` in GitHub to remove GitHub Pages.

Afin de gagner du temps sur la build et économiser votre bande passante/temps de déploiement, vous devez désactiver la prévisualisation du blog à chaque push. 
Pour cela, rendez-vous dans le menu `settings` -> `build & deploy` -> `deploy-previews`
![picture 1](https://i.imgur.com/DNS0DdX.png)  

> [!info] Pros/cons
>> [!info] Pros
>> - Faster than GitHub Pages (1min vs 3min)
>> - No need to use a `gh-pages` branch
>> - Free
>> - No need to worry about workflow times for private repository.
>> - Better link for your blog and you can customize it!
>
>> [!info] Cons
>> - You need to have a Netlify account
>> - Limited by Bandswith for all site (100 GB)
>> - Limited to 300 minutes/builds per month. 



---
- [Main Repo](https://github.com/Mara-Li/obsidian_mkdocs_publisher)
- [Obsidian Plugin](https://github.com/Mara-Li/obsidian-mkdocs-publisher-plugin/)
- [Python package](https://github.com/Mara-Li/obsidian-mkdocs-publisher-python)
- [Template](https://github.com/Mara-Li/obsidian-mkdocs-publisher-template)
- [Documentation](https://mara-li.github.io/obsidian_mkdocs_publisher_docs/)

[^1]: You can found the link in Repository settings > Pages. 
