import os, sys, random, string

choices = string.letters + string.digits

def env(var):
    try:
        return os.environ[var]
    except KeyError:
        sys.exit("No environment variable %s" % var)

def generate_link(length):
    return ''.join(random.choice(choices) for i in range(length))
