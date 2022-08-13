---
title: Configuration
---

- [Obsidian Plugin](https://github.com/ObsidianPublisher/obsidian-github-publisher)
- [Template](https://github.com/ObsidianPublisher/obsidian-mkdocs-publisher-template)
- [Documentation](https://obsidian-publisher.netlify.app)

## Configuration de Mkdocs

Vous avez besoin de configurer à la fois le module Obsidian et mkdocs afin que tout fonctionne proprement.

Vous pouvez obtenir plus d'information au sujet de la création de site via Material Mkdocs [ici](https://squidfunk.github.io/mkdocs-material/creating-your-site/#advanced-configuration).

Au sein de votre template nouvellement clonée, vous trouverez un `mkdocs.yml`. Ce fichier vous permet de personnaliser votre blog ! 

Les plus importants à éditer :
1. `site_name` 
2. `site_description`
3. `site_url` (critique) : Par défaut, c'est `https://github_username.io/repo_name` [^1]

Pour modifier le logo et le favicon, mettez d'abord le fichier choisi dans `assets/logo`, et changez `logo` et `favicon` :
1. `logo : assets/meta/logo_name.png`
2. `favicon : assets/meta/favicon.png`.
3. `extra` : `SEO : 'assets/meta/LOGO_SEO.png'` afin de faire fonctionner proprement les SEO.

Vous pouvez personnaliser :
- Police
- Schéma de couleurs, palette, icônes 
- Langue  

[Consultez la documentation pour obtenir plus d'informations](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

Vous n'avez pas besoin de toucher à quoi que ce soit dans `features` ; `markdown_extensions...`

### Extra configuration

La dernière partie du fichier mkdocs est une configuration pour les `hooks` et la template Jinja affichant la liste des articles (`blog_list.html`).

#### Liste des articles

La liste des articles est configuré par la clé `blog_list` et peut prendre les paramètres suivants : 

- `pagination` (*`boolean, defaut: True`*) : Affiche une pagination si la liste est trop longue.
- `pagination_message` (*`boolean, defaut: True`*) : Affiche un message indiquant le nombre de postes (fichier) dans le dossier.
- `pagination_translation` (*`string, defaut: 'posts in'`*) : Traduction du message de pagination.

Configuration par défaut : 
```yml
extra:
    blog_list:
        pagination: true
        pagination_message: true
        pagination_translation: 'posts in'
```

#### Hooks

Cette partie contient la configuration des `hooks`, des programmes courts en python qui permettent de patch certaines parties de Obsidian incompatibles avec Mkdocs.

Vous pouvez y configurer :
- La suppression des commentaires Obsidian (`%% comments %%`) : `strip_comments: true`
- Un fix pour les titres, qui rajoute un `#` à tous les titres (sauf le 6e) car le TOC de Mkdocs considère que le H1 est le titre principal/titre du fichier : `fix_heading : true`

Configuration par défaut : 
```yml
extra:
  hooks:
    strip_comments: true
    fix_heading: false
```

## Test local (*optionnel*)

Pour faire fonctionner le blog en local, vous devez installer les pré-requis et lancer `mkdocs serve`.
```
cd publish_blog
pip install -r requirements.txt
mkdocs serve
```
Un petit conseil : Vous pouvez utiliser un environnement [conda](https://docs.conda.io/en/latest/) ici (ou un venv, mais je n'aime pas venv). Utilisez simplement ceci :
``bash
conda create -n Publisher python=3.10.4
conda activate Publisher
```
Juste avant l'installation du `pip` !
