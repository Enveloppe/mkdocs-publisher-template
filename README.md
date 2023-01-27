---
title: Configuration
---

- [Obsidian Plugin](https://github.com/ObsidianPublisher/obsidian-github-publisher)
- Template :
  - To use with [Github Pages](https://github.com/ObsidianPublisher/publisher-template-gh-pages)
  - With [Netlify](https://github.com/ObsidianPublisher/publisher-template-netlify)
- [Documentation](https://obsidian-publisher.netlify.app/)
- [Github Discussion](https://github.com/ObsidianPublisher/obsidian-github-publisher/discussions)

## Mkdocs configuration

You need to configure the plugin and the `mkdocs` configuration for it to work properly.

You can find more information about creating the site using the [Material Mkdocs Documentation](https://squidfunk.github.io/mkdocs-material/creating-your-site/#advanced-configuration).

In the repository that you cloned, you will find a `mkdocs.yml` file. This file allows you to customize your blog. The most important settings to edit are:

1. `site_name`
2. `site_description`
3. `site_url` (critical): By default, it's `https://github_username.io/repo_name`[^1]

To edit the logo and favicon, first put the chosen files in the `assets/logo` directory, and then change `logo` and `favicon`:

1. `logo: assets/meta/logo_name.png`
2. `favicon: assets/meta/favicon.png`
3. To properly work with SEO, also edit the `extra` with `SEO: 'assets/meta/LOGO_SEO.png'`

You can also customize:

- Font
- Color scheme, palette, and icons
- Language

[Check the documentation for more information](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

You don't need to touch anything in `features` or `markdown_extensions`.

### Extra configuration

The last part of the `mkdocs.yml` is a configuration for the `hooks` and the template Jinja displaying the list of articles (`blog_list.html`).

There are also :

- `SEO` (_`string`_): Link to your default image displayed by the SEO.
- `comments` (_`boolean`_) : Allow the comments block at the end of the page
- `generate_graph` (_`boolean`_): Generate the [[customization#Graph view|graph view]]
- `attachments` (_`boolean`_): For [[configuration#Blog list (article listing)]] and image in SEO. Change it according to your Obsidian Plugin settings.

#### Blog list (article listing)

The list of articles is configured by the key `blog_list` and can take the following parameters :

- `pagination` (_`boolean, default: True`_): Display a pagination if the list is too long.
- `pagination_message` (_`boolean, default: True`_): Display a message with the number of posts (article/file) in the folder.
- `pagination_translation` (`string, default: 'posts in'`): Translation of the pagination's message.
- `no_page_found` (`string, default: "No pages found!"`): The text to display if no pages were found.

#### Hooks

This part contains the configuration of `hooks`, short python scripts that allow to patch some Obsidian parts incompatible with Mkdocs.

You can configure :

- The suppression of the Obsidian's comments (`%% comments %%`): `strip_comments: true`
- A fix for headings, which adds a `#` to all headings (except the 6th one) because the Mkdocs TOC considers that the H1 is the main heading/title of the file: `fix_heading: true`

## Local testing

To run the blog locally, you need to install the requirements and run `mkdocs serve`.

`cd publish_blog pip install -r requirements.txt mkdocs serve`

A tip: You can use a [conda](https://docs.conda.io/en/latest/) environment here (or a venv, but I prefer conda). Just use this command:

```bash
conda create -n Publisher python=3.11
conda activate Publisher
```

Run this command just before running `pip install`.
