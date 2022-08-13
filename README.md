---
title: Configuration
---

- [Obsidian Plugin](https://github.com/ObsidianPublisher/obsidian-github-publisher)
- [Template](https://github.com/Mara-Li/obsidian-mkdocs-publisher-template)
- [Documentation](https://obsidian-publisher.netlify.app/)

## Mkdocs configuration

You need to configure the plugin to work properly, and in parallels, the `mkdocs` configuration.

You can see more information about the site creation using [The Material Mkdocs Documentation](https://squidfunk.github.io/mkdocs-material/creating-your-site/#advanced-configuration).

In your new cloned blog, you will spot a `mkdocs.yml`. This file allows you to customize your blog! The most important to edit :
1. `site_name` 
2. `site_description`
3. `site_url` (critical) : By default, it's `https://github_username.io/repo_name`[^1]

To edit the logo and the favicon, first put the chosen file in `assets/logo`, and change `logo` and `favicon` :
1. `logo: assets/meta/logo_name.png`
2. `favicon: assets/meta/favicon.png`
3. In order to properly work with SEO, also edit the `extra` with `SEO: 'assets/meta/LOGO_SEO.png'`

You can customize :
- Font
- Color scheme, palette, icons 
- Language  

[Check the documentation to get more information](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

You don't need to touch anything in `features` ; `markdown_extensions…`

### Extra configuration

The last part of the `mkdocs.yml` is a configuration for the `hooks` and the template Jinja displaying the list of articles (`blog_list.html`).

#### Blog list (article listing)

The list of articles is configured by the key `blog_list` and can take the following parameters :
- `pagination` (*`boolean, default: True`*): Display a pagination if the list is too long.
- `pagination_message` (*`boolean, default: True`*): Display a message with the number of posts (article/file) in the folder.
- `pagination_translation` (`string, default: 'posts in'`): Translation of the pagination's message.

Default configuration: 
```yml
extra:
    blog_list:
        pagination: true
        pagination_message: true
        pagination_translation: 'posts in'
```

#### Hooks

This part contains the configuration of `hooks`, short python scripts that allow to patch some Obsidian part incompatible with Mkdocs.

You can configure :
- The suppression of the Obsidian's comments (`%% comments %%`): `strip_comments: true`
- A fix for headings, which adds a `#` to all headings (except the 6th one) because the Mkdocs TOC considers that the H1 is the main heading/title of the file: `fix_heading: true`

Default configuration: 
```yml
extra:
  hooks:
    strip_comments: true
    fix_heading: false
```

## Local testing
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
