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

## Metacopy
Using [metacopy](https://github.com/Mara-Li/obsidian-metacopy) you can quickly copy a link to a shared page, without using this option (so, yes, the script does not edit your source file !).   
To create a link, you need to configure :  
 1. `category` in `key`  
 2. Add your `set_url` in `base link`  
 3. Add `category` in `key link`  
  
Also, you can remove the metacopy from your file menu using a key, so you can activate metacopy only for `share: true`. Metacopy also support the [[blog customization#folder-note|folder note]].

The final configuration of metacopy for mkdocs_obsidian will be :  
![](assets/img/metacopy3.png)  
![](assets/img/metacopy2.png)  
  
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
- **No Obsidian plugin is supported**
- The plugin rely a lot on filename, without regarding the folder. Please use **unique naming** and use the `title` key if you need to.
- The plugin will not delete the `index` files (cf [[blog customization#folder-note|folder note]])
- The script can be long on big vault.
- The script will not manually move the file if you change a `category` : you need to delete it manually to prevent duplicate.
- ⚠️You must use `shortlinks` in Obsidian configuration. 


If you have more question, don't forget to read the [[Q&A]] !