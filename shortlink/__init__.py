from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
import os, sys, redis, random, string

shortlink = Flask(__name__)

def env(var):
    try:
        return os.environ[var]
    except KeyError:
        sys.exit("No environment variable %s" % var)

shortlink.secret_key = env('SECRET_KEY')

r = redis.StrictRedis(host=env('REDIS_HOST'), 
        port=int(env('REDIS_PORT')),
        db=int(env('REDIS_DB')))

choices = string.letters + string.digits

@shortlink.route('/', methods=['GET'])
def index():
    return view('layout.html')

@shortlink.route('/', methods=['POST'])
def make():
    destination = request.form['url']
    while True:
        url = generate_link()
        if r.setnx(url, destination): break
    return view('layout.html', { 'shortlink': True, 'url': url })

@shortlink.route('/<link>')
def go(link):
    destination = r.get(link)
    if destination:
        return redirect(destination)
    flash('no such shortlink')
    return redirect(url_for('index'))

def view(t, v = {}):
    v['config'] = config
    return render_template(t, **v)

def generate_link():
    return ''.join(random.choice(choices) for i in range(config['url_length']))
