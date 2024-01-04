import argparse
from pathlib import Path
from string import Template
from typing import Literal

import requests
from pydantic import BaseModel


class TemplateModel(BaseModel):
    template_type: Literal["gh_pages", "netlify", "vercel"]
    site_name: str
    site_url: str
    site_description: str
    site_author: str
    language: str
    auto_h1: bool
    comments: bool
    generate_graph: bool = False


class Environment(BaseModel):
    env: str
    deploy: str


netlify = Environment(
    env="https://github.com/ObsidianPublisher/actions/raw/main/template/netlify/.env",
    deploy="https://raw.githubusercontent.com/ObsidianPublisher/actions/main/template/netlify/deploy.yml",
)

vercel = Environment(
    deploy="https://raw.githubusercontent.com/ObsidianPublisher/actions/main/template/vercel/deploy.yml",
    env="https://raw.githubusercontent.com/ObsidianPublisher/actions/main/template/vercel/.env",
)

gh_pages = Environment(
    deploy="https://raw.githubusercontent.com/ObsidianPublisher/actions/main/template/gh-pages/deploy.yml",
    env="https://raw.githubusercontent.com/ObsidianPublisher/actions/main/template/gh-pages/.env",
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a template for Obsidian Publisher"
    )
    parser.add_argument(
        "template",
        type=str,
        help="The template to generate",
        choices=["gh_pages", "netlify", "vercel"],
    )
    parser.add_argument("site_name", type=str, help="The name of the site")
    parser.add_argument("site_url", type=str, help="The url of the site")
    parser.add_argument(
        "site_description", type=str, help="The description of the site"
    )
    parser.add_argument("site_author", type=str, help="The author of the site")
    parser.add_argument("language", type=str, help="The language of the site")
    parser.add_argument(
        "--auto-h1", action="store_true", help="Automatically add h1 to the title"
    )
    parser.add_argument(
        "--comments", action="store_true", help="Enable comments on the site"
    )

    args = parser.parse_args()

    template = TemplateModel(
        template_type=args.template,
        site_name=args.site_name,
        site_url=args.site_url,
        site_description=args.site_description,
        site_author=args.site_author,
        language=args.language,
        auto_h1=args.auto_h1,
        comments=args.comments,
        generate_graph=True if args.template == "gh_pages" else False,
    )
    env = gh_pages
    if args.template == "netlify":
        env = netlify
    elif args.template == "vercel":
        env = vercel
    # download the files
    env_path = Path(".github/.env")
    deploy_path = Path(".github/workflows/deploy.yml")
    with env_path.open("w", encoding="UTF-8") as f:
        f.write(requests.get(env.env).text)
    with deploy_path.open("w", encoding="UTF-8") as f:
        f.write(requests.get(env.deploy).text)
    # write the template
    mkdocs_yaml = Path("mkdocs.yml")
    with mkdocs_yaml.open("r", encoding="UTF-8") as f:
        mkdocs = f.read()
    mkdocs = Template(mkdocs)
    s = mkdocs.substitute(
        site_name=template.site_name,
        site_url=template.site_url,
        site_description=template.site_description,
        site_author=template.site_author,
        language=template.language,
        auto_h1=template.auto_h1,
        comments=template.comments,
        generate_graph=template.generate_graph,
    )
    requirements = [
        "mkdocs==1.5.3",
        "mkdocs-material==9.5.3",
        "mkdocs-ezlinked-plugin==0.3.3",
        "mkdocs-awesome-pages-plugin==2.9.2",
        "mdx_breakless_lists==1.0.1",
        "mkdocs-embed-file-plugins==2.0.9",
        "mkdocs_custom_fences==0.1.2",
        "mkdocs-git-revision-date-localized-plugin==1.2.2",
        "mkdocs-encryptcontent-plugin==3.0.2",
        "mkdocs-callouts==1.10.0",
        "mkdocs-custom-tags-attributes==0.3.1",
        "mkdocs-meta-descriptions-plugin==3.0.0",
        "mkdocs-glightbox==0.3.6",
    ]
    requirements_actions_content = [
        "obsidiantools==0.10.0",
        "pyvis==0.3.2",
        "cairosvg==2.7.1",
        "pillow==10.2.0",
    ]
    requirements_actions = Path("requirements_actions.txt")
    if template.template_type in ["netlify", "vercel"]:
        # create requirements_actions.txt
        with requirements_actions.open("w", encoding="UTF-8") as f:
            f.write("\n".join(requirements_actions_content))

    if template.template_type == "netlify":
        with Path("runtime.txt").open("w", encoding="UTF-8") as f:
            f.write("3.8")

    elif template.template_type == "gh_pages":
        requirements += requirements_actions_content
        # delete requirements_actions.txt

        if requirements_actions.exists():
            requirements_actions.unlink()

    with Path("requirements.txt").open("w", encoding="UTF-8") as f:
        f.write("\n".join(requirements))
    with mkdocs_yaml.open("w", encoding="UTF-8") as f:
        f.write(s)

    print("Mkdocs template generated:")
    print(s)
    print("Requirements generated:")
    print("\n".join(requirements))
    if template.template_type in ["netlify", "vercel"]:
        print("Requirements for actions generated:")
        print("\n".join(requirements_actions_content))
    print("Done!")


if __name__ == "__main__":
    main()
