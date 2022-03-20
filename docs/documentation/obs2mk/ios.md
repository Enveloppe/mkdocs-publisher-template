The script support IOS using :
- [a-shell](https://holzschu.github.io/a-Shell_iOS/) (Free)  
- [Pyto](https://pyto.app) ($3 lite version / $10 complete version) [^1]
- [Working Copy](https://workingcopyapp.com/) (Free for student / $19)

> The option `mobile` will **never** push. You need to use Working Copy to push the converted file.

You can :
1. Share the entire vault : `obs2mk --mobile all --vault`
2. Share a specific file, using its name : `obs2mk --mobile file "filename"`.[^2] This option can be used especially with [Shortcuts](https://support.apple.com/guide/shortcuts/welcome/ios)

[^1]: Using Pyto you need to add the writing authorization for your vault and blog repository. You can access it in parameters > Runtime. 
[^2]: Beware, if it exists a file with the same name, it will take the first found. 