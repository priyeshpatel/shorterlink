import os 

config = {}

if os.environ.get('DEVELOPMENT', None):
    config['url'] = "http://127.0.0.1:%i" % int(os.environ.get('PORT', 5000))
else:
    config['url'] = "http://blah.herokuapp.com"

config['url_length'] = 6
