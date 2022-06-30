import re

def on_page_markdown(markdown, files, **kwargs):
    file_content = markdown.split('\n')
    markdown = ''
    for line in file_content:
        if not re.search(r'%%(.*)%%', line) or not line.startswith('%%') or not line.endswith('%%'):
            markdown += line + '\n'
    markdown = re.sub(r'%%(.*)%%', '', markdown, flags=re.DOTALL)
    return markdown