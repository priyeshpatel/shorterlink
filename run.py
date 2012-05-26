from shortlink import shortlink 
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if os.environ.get('DEVELOPMENT', None):
        shortlink.debug = True
    shortlink.run(host='0.0.0.0', port=port)
