## 1. Private repository

As I authorize this repo to be a template, it allows you to create a private repository!

_Note : Fork doesn't allow you to create a private repo, that's why you must use the template._

## 2. Update the template

Using a template (in place of fork) prevent to get the update I do sometimes. So, to keep an eye on it, you need to create a **branch** based on the template. 

In the cloned folder, (in your blog) do : 
```git
git remote add Template git@github.com:Mara-Li/mkdocs_obsidian_template.git
git fetch Template
git checkout -b template Template/main
```
After, to get the update : 
```git
git checkout template
git pull
```

You can merge the branch, or just get the updated file with the checkout command : 
```git
git checkout main
git checkout template path/file/youwant 
```
Don't forget to commit and push!

## 3. Update the script

The simplest way to update the script is using pip : `pip install obs2mk --upgrade`

## 4. The script crash with YAML error.

The YAML error is not on my side, but on yours. You need to fix the front matter of the error's file. To accomplish that, you can use a YAML validator/linter, as : https://jsonformatter.org/yaml-validator