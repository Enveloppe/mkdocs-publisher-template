import logging
import shutil
import os
import re
import urllib.parse
import datetime
from pathlib import Path

from babel.dates import format_date
from dateutil import parser


def obsidian_graph():
    """Generates a graph of the Obsidian vault."""
    # pylint: disable=import-outside-toplevel
    import obsidiantools.api as otools

    # pylint: disable=import-outside-toplevel``
    from pyvis.network import Network

    log = logging.getLogger("mkdocs.plugins." + __name__)
    log.info("[OBSIDIAN GRAPH] Generating graph...")
    vault_path = Path(Path.cwd(), "docs")
    vault = otools.Vault(vault_path).connect().gather()
    graph = vault.graph
    net = Network(
        height="750px", width="750px", font_color="#7c7c7c", bgcolor="transparent"
    )
    net.from_nx(graph)
    try:
        net.save_graph(str(Path.cwd() / "docs" / "assets" / "graph.html"))
    except OSError:
        pass
    shutil.rmtree(Path.cwd() / "lib")
    log.info("[OBSIDIAN GRAPH] Graph generated!")
    return ""


def get_last_part_URL(url):
    """Get the last part of an URL.

    Args:
        url (str): the URL

    Returns:
        str: the last part of the URL
    """
    if not url.endswith("/"):
        url = url + "/"
    head, tail = os.path.split(url)
    return "/" + tail if tail != "" else ""


def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    return re.sub(find, replace, s)


def log(text):
    """Prints text to the console, in case you need to debug something.

    Using mainly in the template files.
    Parameters:
        text (str): The text to print.
    Returns:
        str: An empty string.
    """
    print(text)
    return ""


def time_time(time):
    """Converts a time string to a human-readable format.

    Parameters:
        time (any): The time string to convert.
    Returns:
        str|datetime:  The converted time.
    """
    time = time.replace("-", "/")
    time = parser.parse(time).isoformat()
    try:
        time = datetime.datetime.fromisoformat(time)
        return datetime.datetime.strftime(time, "%d %B %Y")
    except AttributeError:
        return datetime.datetime.strftime(str(time), "%d %B %Y")
    except ValueError:
        print("value error!")
        return time


def to_local_time(time, locale):
    """Convert to local time.

    Args:
        time (any): the time to convert
        locale (any): the locale to use

    Returns:
        str: the converted time
    """
    if isinstance(time, datetime.time) or isinstance(time, datetime.date):
        time = time.isoformat()
    date = time.replace("-", "/")
    date = parser.parse(date)
    return format_date(date, locale=locale)


def time_todatetime(time):
    """convert time to datetime.

    Args:
        time (any): time to convert

    Returns:
        datetime: the converted time
    """
    return parser.parse(time)


def time_to_iso(time):
    """Convert time to ISO format.

    Args:
        time (any): Time to convert

    Returns:
        any|str: convert time or the original time if error
    """
    if isinstance(time, datetime.time) or isinstance(time, datetime.date):
        time = time.isoformat()
    time = time.replace("-", "/")
    try:
        return parser.parse(time).isoformat()
    except AttributeError:
        return time


def page_exists(page):
    """Check if a page exists.

    Args:
        page (any): The page to check

    Returns:
        bool: true if exists
    """
    return Path(page).exists()


def url_decode(url):
    """decode an url in a template.

    Args:
        url (any): THE URL

    Returns:
        str : the decoded url
    """
    return urllib.parse.unquote(url)


def value_in_frontmatter(key, metadata):
    """Check if a key exists in a dictionnary.

    Args:
        key (any): the key to check
        metadata (any): the dictionnary to check

    Returns:
        bool: true if exists
    """
    if key in metadata:
        return metadata[key]
    else:
        return None


def on_env(env, config, files, **kwargs):
    if config["extra"].get("generate_graph", True):
        obsidian_graph()
    env.filters["convert_time"] = time_time
    env.filters["iso_time"] = time_to_iso
    env.filters["time_todatetime"] = time_todatetime
    env.filters["page_exists"] = page_exists
    env.filters["url_decode"] = url_decode
    env.filters["log"] = log
    env.filters["to_local_time"] = to_local_time
    env.filters["value_in_frontmatter"] = value_in_frontmatter
    env.filters["regex_replace"] = regex_replace
    env.filters["get_last_part_URL"] = get_last_part_URL
    return env
