"""
A simple script that help to create a category in the database. Create the folder and the `index.md` file.
Usage : 
usage: category.py [-h] [--parent PARENT] [--description DESCRIPTION] [--toc] [--nav] name
positional arguments:
  name                  Name of the category.

options:
  -h, --help                    show this help message and exit
  --parent PARENT               Parent category.
  --description DESCRIPTION     Description of the category.
  --toc                         hide toc
  --nav                         hide nav
"""

import argparse
import yaml
from pathlib import Path
import re

def create_category(path, index_contents):
    path.mkdir(parents=True, exist_ok=True)
    index_file = Path(path, 'index.md')
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_contents.lstrip())

def index_contents(name, description_yaml, hider, description):
    index_contents = f'''
        ---
        index: true{description_yaml}
        hidden: true
        category: {name}
        template: blog.html
        title: {name}{hider}
        ---
        {description}
        '''
    index_contents = re.sub('    ', '', index_contents)
    return index_contents
    
def resolving_args(args, docs_dir):
    if args.parent:
        path = Path(docs_dir, args.parent, args.name)
    else:
        path = Path(docs_dir, args.name)
    if args.description:
        description_yaml = '\ndescription: ' + args.description
        description_contents = args.description
    else:
        description_yaml = ''
        description_contents = ''
    hider = []
    if args.toc:
        hider.append('toc')
    if args.nav:
        hider.append('navigation')
    hider = '\nhide:\n- ' + '\n- '.join(hider) if hider else ''
    return path, description_yaml, hider, description_contents

def main():
    parser = argparse.ArgumentParser(description='Create a new category your mkdocs documentations from your docs (or configured directory).')
    parser.add_argument('name', help='Name of the category.')
    parser.add_argument('--parent', help='Parent category, in path. Example : "category/subcategory"')
    parser.add_argument('--description', help='Description of the category.')
    parser.add_argument('--toc', help='hide toc', action='store_true')
    parser.add_argument('--nav', help='hide nav', action='store_true')
    parser.add_argument('--dry-run', help='Dry run, do not create the category, just log', action='store_true')
    args = parser.parse_args()


    mkdocs_config = Path('mkdocs.yml').resolve()
    with open(mkdocs_config, 'r', encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.BaseLoader)
    docs_dir = config.get('docs_dir', 'docs')
    docs_dir = Path(docs_dir).resolve()
    path, description_yaml, hider, description_contents = resolving_args(args, docs_dir)
    index = index_contents(args.name, description_yaml, hider, description_contents)
    if not args.dry_run:
        print('📤 Creating category 📤...')
        print(f'\nArguments used :\n- Name: {args.name}\n- Parents: {args.parent}\n- Description: {args.description}\n- Toc: {args.toc}\n- Nav: {args.nav}\n')
        print(f'📌 Creating with path : {path}')
        create_category(path, index)
        print('Category created ! 🎉')
    else:
        print('🐍 Dry Run 🐍')
        print(f'\nArguments used :\n- Name: {args.name}\n- Parents: {args.parent}\n- Description: {args.description}\n- Toc: {args.toc}\n- Nav: {args.nav}\n')
        print(f'🚃 Path : {path}')
        print(f'🗃️ Index : {index}')
    

if __name__ == "__main__":
    main()
    print("Done.")
    exit(0)