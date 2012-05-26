from shorterlink import shorterlink 
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if os.environ.get('DEVELOPMENT', None):
        shorterlink.debug = True
    shorterlink.run(host='0.0.0.0', port=port)
