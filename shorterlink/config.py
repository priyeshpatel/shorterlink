import os, sys

config = {}

def env(var):
    try:
        return os.environ[var]
    except KeyError:
        sys.exit("No environment variable %s" % var)

config['url'] = env('URL')
config['port'] = env('PORT')
config['full_url'] = config['url'] + ":" + config['port']
if config['port'] == 80 or not os.environ.get('DEVELOPMENT', None):
    config['full_url'] = config['url']
config['url_length'] = 6
