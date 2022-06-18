In your new `publish_blog` folder, you will spot a `mkdocs.yml`. This file allows you to customize your blog! The most important to edit :
1. `site_name` 
2. `site_description`
3. `site_url` (critical) : By default, it's `https://github_username.io/repo_name`[^1]

To edit the logo and the favicon, first put the chosen file in `assets/logo`, and change `logo` and `favicon` :
1. `logo: assets/logo/logo_name.png`
2. `favicon: assets/logo/favicon.png`

You can customize :
- Font
- Color scheme, palette, icons 
- Language  

[Check the documentation to get more information](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

You don't need to touch anything in `features` ; `markdown_extensions…`

## Local testing (optional)

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

The blog will be published through [GitHub Page](https://pages.github.com/) using the `gh-page` branch. In case your blog is not published through mkdocs :
- Check the `gh-pages` branch and activate it if necessary in `Settings` → `Pages` : ![image](https://user-images.githubusercontent.com/30244939/166161220-973cee87-75eb-4b9f-b521-1c67d273def7.png)
- Check if workflow run normally :
  - Check the run and error in `Actions` 
  - Check if the actions have the good write and read access in `settings → Actions → General → workflow permission` ![image](https://user-images.githubusercontent.com/30244939/166161294-0f4f70c2-fda5-4465-89b0-d6b1b5e6995d.png)

> [!Warning] In case of worfklow problem
> In the [issue #4](https://github.com/obsidianMkdocs/obsidian-github-publisher/issues/4), we discover that sometimes, Github Actions refuse to run without reason. If this happend to you, please, contact the Github Support!

---

- [Obsidian Plugin](https://github.com/obsidianMkdocs/obsidian-mkdocs-publisher-plugin/)
- [Python package](https://github.com/obsidianMkdocs/obsidian-mkdocs-publisher-python)
- [Template](https://github.com/obsidianMkdocs/obsidian-mkdocs-publisher-template)
- [Documentation](https://obsidianmkdocs.github.io/obsidian_mkdocs_publisher_docs/)

[^1]: You can found the link in Repository settings > Pages. 
