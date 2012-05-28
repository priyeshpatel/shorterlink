import os, sys, random, string
from flask import render_template
from . import config
import redis

choices = string.letters + string.digits

r = redis.from_url(config.env('REDISTOGO_URL'), int(config.env('REDIS_DB')))

def generate_unique_link(length):
    return ''.join(random.choice(choices) for i in range(length))

def create(destination):
    while True:
        url = generate_unique_link(config.config['url_length'])
        if r.setnx("link:" + url, destination): break
    return url 

def get(link):
    return r.get("link:" + link)

def count():
    return len(r.keys("link:*"))

def view(t, v = {}):
    v['config'] = config.config
    v['count'] = count()
    return render_template(t, **v)
