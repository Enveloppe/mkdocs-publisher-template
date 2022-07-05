import re

def strip_comments(markdown):
    file_content = markdown.split('\n')
    markdown = ''
    for line in file_content:
        if not re.search(r'%%(.*)%%', line) or not line.startswith('%%') or not line.endswith('%%'):
            markdown += line + '\n'
    markdown = re.sub(r'%%(.*)%%', '', markdown, flags=re.DOTALL)
    return markdown

def fix_tags(metadata):
    tags = metadata.get('tags', None) or metadata.get('tag', None)
    if tags and isinstance(tags, str):
        tags = tags.split('/')
        tags = [tag.strip() for tag in tags]
        metadata['tags'] = tags
    return metadata

def on_page_markdown(markdown, files, page, **kwargs):
    markdown = strip_comments(markdown)
    metadata = fix_tags(page.meta)
    page.meta = metadata
    return markdown