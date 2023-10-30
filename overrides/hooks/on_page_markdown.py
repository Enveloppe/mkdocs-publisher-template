import re


def non_breaking_space(markdown):
    return re.sub(
        "[\u00A0\u1680\u180E\u2000-\u200B\u202F\u205F\u3000\uFEFF]", "&emsp;", markdown
    )


def update_heading(markdown):
    file_content = markdown.split("\n")
    markdown = ""
    code = False
    for line in file_content:
        if not code:
            if line.startswith("```"):
                code = True
            elif line.startswith("#") and line.count("#") <= 5:
                heading_number = line.count("#") + 1
                line = "#" * heading_number + " " + line.replace("#", "")
        elif line.startswith("```") and code:
            code = True
        markdown += line + "\n"
    return markdown


def strip_comments(markdown):
    return re.sub(r"%%.*?%%", "", markdown, flags=re.DOTALL)


def fix_tags(metadata):
    tags = metadata.get("tags", None) or metadata.get("tag", None)
    if tags and isinstance(tags, str):
        tags = tags.split("/")
        tags = [tag.strip() for tag in tags]
        metadata["tags"] = tags
    return metadata


def on_page_markdown(markdown, files, page, config, **kwargs):
    config_hooks = config.get(
        "extra", {"hooks": {"strip_comments": True, "fix_heading": False}}
    ).get("hooks", {"strip_comments": True, "fix_heading": False})
    if config_hooks.get("strip_comments", True):
        markdown = strip_comments(markdown)
    if config_hooks.get("fix_heading", False):
        markdown = update_heading(markdown)
    metadata = fix_tags(page.meta)
    page.meta = metadata
    markdown = non_breaking_space(markdown)
    return markdown
