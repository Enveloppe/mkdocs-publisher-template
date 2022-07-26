---
title: Configuration
share: true
---

## Configuration
## Configuration de Mkdocs

Dans votre nouveau dossier `publish_blog`, vous trouverez un `mkdocs.yml`. Ce fichier vous permet de personnaliser votre blog ! Les plus importants à éditer :
1. `site_name` 
2. `site_description`
3. `site_url` (critique) : Par défaut, c'est `https://github_username.io/repo_name` [^1]

Pour modifier le logo et le favicon, mettez d'abord le fichier choisi dans `assets/logo`, et changez `logo` et `favicon` :
1. `logo : assets/meta/logo_name.png`
2. `favicon : assets/meta/favicon.png`.

Vous pouvez personnaliser :
- Police
- Schéma de couleurs, palette, icônes 
- Langue  

[Consultez la documentation pour obtenir plus d'informations](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

Vous n'avez pas besoin de toucher à quoi que ce soit dans `features` ; `markdown_extensions...`

### Plugins

Le fichier `mkdocs.yml` contient également la configuration de [Mkdocs Plugin] (https://www.mkdocs.org/dev-guide/plugins/). Si vous ajoutez le plugin, vous **devez** l'ajouter à votre `requirements.txt` car la build l'utilise pour construire le blog.

J'ai inclus :
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
> Vous remarquerez que j'ai ajouté une [`custom fences`](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) pour dataviewjs. Désolé, dataviewjs n'est pas encore supporté par mkdocs ni Obsidian Publisher. Ce "custom fence" cachera tous les blocs dataviewjs. 
> Elle empêchera donc l'affichage de blocs étranges dans votre fichier markdown. Si vous avez besoin de l'afficher comme du code, changez le langage (comme `js` par exemple).

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

---

# Deploiement
## Par GitHub Pages

Le blog sera publié via [GitHub Page](https://pages.github.com/) en utilisant la branche `gh-page`. 

> [!bug] J'ai le README à la place de mes fichiers !
> Vérifier la branche `gh-pages` et l'activer si nécessaire dans `Settings` → `Pages`
> ![image](https://user-images.githubusercontent.com/30244939/166161220-973cee87-75eb-4b9f-b521-1c67d273def7.png)

> [!bug] Le workflow ne s'exécute pas !
> - Vérifiez l'exécution et l'erreur dans `Actions`. 
> - Vérifiez si les actions ont les bons accès en écriture et en lecture dans `Settings → Actions → General → workflow permission` ![image](https://user-images.githubusercontent.com/30244939/166161294-0f4f70c2-fda5-4465-89b0-d6b1b5e6995d.png)
>> [!Avertissement] En cas de problème de worfklow
>> Dans le [problème #4](https://github.com/obsidianPublisher/obsidian-github-publisher/issues/4), nous avons découvert que parfois, les actions Github refusent de s'exécuter sans raison. Si cela vous arrive, veuillez contacter le support Github !

## Par Netlify

Netlify est un service qui permet de publier votre blog gratuitement sur un site web, et la construction du blog (*build*) sera beaucoup plus rapide que via GitHub.

Pour déployer votre blog, vous pouvez cliquer ici : [![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/ObsidianPublisher/obsidian-mkdocs-publisher-template)

Alternativement : 
- Créer un compte sur Netlify.app
- Ajouter un nouveau site en utilisant un dépôt déjà existant. 
    Pour la configuration, vous pouvez utiliser :
    - Laisser blanc pour le `base directory`
    - <u>Build command</u> : `mkdocs build`
    - <u>Publish directory</u> : `site`
- Prendre le fichier `runtime.txt` et le rajouter à la racine de votre dépôt, ou créer une nouvelle variable d'environnement nommée `PYTHON_VERSION` fixée à `3.8`.

Afin de gagner du temps sur la build et économiser votre bande passante/temps de déploiement, vous devez désactiver la prévisualisation du blog à chaque push. 
Pour cela, rendez-vous dans le menu `settings` -> `build & deploy` -> `deploy-previews`
![picture 1](https://i.imgur.com/DNS0DdX.png)  


> [!note]
> Il peut être possible que vous ayez besoin de supprimer la branch `gh-pages` pour supprimer l'ancienne page GitHub Pages.

> [!info] Avantages/inconvénients
>> [!info] Avantages
>> - Plus rapide que GitHub Pages (1min VS 3min)
>> - Gratuit
>> - Pas besoin de s'inquiéter du temps des workflow dans les dépôt privés.
>> - Meilleur liens et customisation de ses derniers.
>
>> [!info] Inconvénients
>> - Vous avez besoin d'un compte Netlify pour déployer votre blog.
>> - Limité par la bande passante à 100GB pour tous les sites
>> - Limités à 300minutes/build par mois.

---

- [Obsidian Plugin](https://github.com/ObsidianPublisher/obsidian-github-publisher)
- [Template](https://github.com/ObsidianPublisher/obsidian-mkdocs-publisher-template)
- [Documentation](https://obsidian-publisher.netlify.app)

[^1]: Vous pouvez trouver le lien dans `Settings > Pages`
