import json
import posixpath
import os
from pathlib import PurePosixPath
from mkdocs.structure.files import Files
from mkdocs.config.defaults import MkDocsConfig

def list_existing_pages(config: MkDocsConfig, files: Files):
    pages = []
    output_dir = config['site_dir']
    for file in files:
        if file.is_documentation_page() or file.is_media_file():
            pages.append(file)
    
    with open(posixpath.join(output_dir, 'search', 'all_files.json'), 'w') as f:
        json.dump(pages, f, default=lambda o: o.__dict__, indent=4)

def on_files(files: Files, config: MkDocsConfig):
    if not (posixpath.exists(posixpath.join(config['site_dir'], 'search'))):
        os.makedirs(posixpath.join(config['site_dir'], 'search'))
    list_existing_pages(config, files)
    return files

