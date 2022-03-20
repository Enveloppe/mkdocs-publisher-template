You could create :
1. A command to publish everything : alias `Publish` with `obs2mk --obsidian`
2. A command to publish one specific file : alias `Publish {{title}}` with `obs2mk --obsidian file {{file_path:absolute}}`
3. Event shortcuts for file menu event : `Publish {{event_file_name}}`: `obs2mk --obsidian file "{{event_file_path:absolute}}`
4. Folder Note event (folder menu event): `Publish {{event_folder_name}}`: `obs2mk --obsidian file "{{event_folder_path:relative}}\{{event_folder_name}}.md"`
 
You can create a button with :
- [Customizable Sidebar](https://github.com/phibr0/obsidian-customizable-sidebar)    
- [Obsidian Customizable Menu](https://github.com/kzhovn/obsidian-customizable-menu)