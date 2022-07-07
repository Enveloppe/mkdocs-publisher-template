from datetime import datetime
from dateutil import parser
from pathlib import Path
import urllib.parse

def logging(text):
    print(text)
    return ''

def time_time(time):
    time=time.replace('-', '/')
    time = parser.parse(time).isoformat()
    try:
        time = datetime.fromisoformat(time)
        return datetime.strftime(time,'%d %B %Y')
    except AttributeError:
        return datetime.strftime(str(time),'%d %B %Y')
    except ValueError:
        print('value error!')
        return time

def time_todatetime(time):
    return parser.parse(time)

def time_to_iso(time):
    time=time.replace('-', '/')
    
    try:
        return parser.parse(time).isoformat()
    except AttributeError:
        return time

def page_exists(page):
    return Path(page).exists()

def url_decode(url):
    return urllib.parse.unquote(url)

def on_env(env, config, files, **kwargs):
    env.filters['convert_time'] = time_time
    env.filters['iso_time'] = time_to_iso
    env.filters['time_todatetime'] = time_todatetime
    env.filters['page_exists'] = page_exists
    env.filters['url_decode'] = url_decode
    env.filters['logging'] = logging
    return env