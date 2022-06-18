from datetime import datetime
from dateutil import parser
import locale



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

def on_env(env, config, files, **kwargs):
    locale.setlocale(locale.LC_ALL, '')
    print('get locale', locale.getlocale())
    env.filters['convert_time'] = time_time
    env.filters['iso_time'] = time_to_iso
    env.filters['time_todatetime'] = time_todatetime
    return env