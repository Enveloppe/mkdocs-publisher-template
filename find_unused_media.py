from pathlib import Path
import os 
import argparse
from mkdocs.config import load_config


def find_unused_media(img_path: Path=None, dry_run: bool = False):
    config = load_config(config_file='mkdocs.yml')
    docs_dir = Path(config['docs_dir'])
    assets_dir = Path(docs_dir, config["extra"]["attachments"])
    if img_path:
        assets_dir = img_path

    images = [file for file in assets_dir.rglob('*') if file.is_file() and file.suffix in ['.png', '.jpg', '.jpeg', '.gif', '.svg']]
    md_files = [file for file in docs_dir.rglob('*.md') if file.is_file()]

    # Search for images in markdown files

    used_images = []

    for md_file in md_files:
        for image in images:
            with open(md_file, 'r', encoding='utf-8') as f:
                if image.name in f.read():
                    used_images.append(image)

    # compare the two lists
    unused_images = [image for image in images if image not in used_images]

    # delete unused images

    if unused_images:
        print(f'Found {len(unused_images)} unused images in {assets_dir}. Deleting...')
        for image in unused_images:
            if not dry_run:
                print(image)
                os.remove(image)
            else:
                print(f'Would delete {image}')
    else:
        print(f'Found no unused images in {assets_dir}.')


if __name__ == '__main__':
    # use argparse to get the path to the assets folder
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='Path to the assets folder')
    parser.add_argument('--dry-run', action='store_true', help='Do not delete unused images')
    args = parser.parse_args()
    path = Path(args.path) if args.path else None
    find_unused_media(img_path=path, dry_run=args.dry_run)
