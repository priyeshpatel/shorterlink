from shortlink import shortlink 
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if os.environ.get('DEVELOPMENT', None):
        shortlink.run(port=port, debug=True)
    else:
        shortlink.run(host='0.0.0.0', port=port)
