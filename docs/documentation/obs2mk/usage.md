The script can be use :
- Directly in Obsidian, using [Obsidian Shell Commands](https://github.com/Taitava/obsidian-shellcommands) (see [[obsidian shell|Obsidian shell configuration]])
- In a [terminal](#commands).

The supported system are :
- macOS, Linux and Windows
- [[ios|IOS]] (with [Pyto](https://pyto.app) and/or [a-shell](https://holzschu.github.io/a-Shell_iOS/) with [Working Copy](https://workingcopyapp.com/))

## Script's Configuration
At the first run, you will be asked to configure some key and specific path.
1. <u>Vault</u> : Use the file dialog to choose your vault folder.
2. <u>Publish repository folder : </u> As vault path, use the file dialog.
3. <u>share</u> : You can change the `share` key. By default, it's `share`
4. <u>Index key:</u> Support for citation of [[blog customization#folder-note|pagination index pages]]. By default, it uses `(i)`
5. <u>Default blog folder:</u> By default, the notes will be in `docs/notes` but you can change that, or use `/` for root. 

## Commands

Global options :
- `--git` : No commit and push to git ; 
- `--mobile` : Use mobile shortcuts instead of `--git`
- `--meta` : Update frontmatter of source files
- `--keep` : Don't delete files in blog folder
- `--shell` : Remove Rich printing

Commands and specific options :
- **config** : (*it will ignore `--use configuration_name`*)
    - `--new configuration_name` : Create a specific configuration for some files
- **all** : Share all vault
    - `--force` : Force updating (ignore the difference between the source and blog file)
    - `--vault` : Share all vault file, ignoring the share state.
- **`file [file*]`** : Share only one file

```bash
usage: __main__.py [-h] [--mobile | --git] [--meta] [--keep] [--use configuration_name] {config,all,file} ...

positional arguments:
  {config,all,file}
    config              Configure the script : Add or edit your vault and blog absolute path, change some keys.
    all                 Publish multiple files
    file                Publish only one file

options:
  -h, --help            show this help message and exit
  --mobile, --shortcuts
                        Use mobile shortcuts, without push
  --git, --g, --G       No commit and no push to git
  --meta, --m, --M      Update the frontmatter of the source file, adding the note blog's link
  --keep, --k, --K      Keep deleted file from vault and removed shared file
  --use configuration_name, --config configuration_name
                        Use a different config from default
```
The commands order is :
`obs2mk (global_options) [all|config|file FILEPATH] (specific_options)`
Where :
- Global and specific options are optional
- `all`, `config` and `file`[^1] are required
You can use the command without argument with `obs2mk` to share every `share: true` file in your vault.

## Share one file : `obs2mk file FILEPATH`
It will :
- Update the `share` state in original file
- Convert one file, regardless of what is the `share` state.

## Share all file : `obs2mk all` or `obs2mk`
You can share multiple documents at once with scanning your Vault, looking for the `share: true`. It will convert automatically these files.  
Only file with modification since the last sharing will be updated.

You can :
- Share entirely your vault (that's ignore the `share` state) with : `obs2mk all --vault`
- Ignore the difference between the source file and the blog's file with :  `obs2mk all --force`
Also, you can combine the two options. 

## Multiple configurations
You can use and create multiple configuration files. This allows to have multiple site based on one vault, or different vault accross one site... 
1. To create a new configuration file : `obs2mk config --new configuration_name`
2. To use a configuration use : `--use configuration_name` 
    For example : `obs2mk --use configuration_name` 

[^1]: For `file` you need to add the filepath of the file you want to share : `obs2mk (global_option) file "filepath" (specific_options)`