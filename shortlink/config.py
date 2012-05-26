import os
from . import utils

config = {}

config['url'] = utils.env('URL')
config['port'] = utils.env('PORT')
config['full_url'] = config['url'] + ":" + config['port']
if config['port'] == 80 or not os.environ.get('DEVELOPMENT', None):
    config['full_url'] = config['url']
config['url_length'] = 6
