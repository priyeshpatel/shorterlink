from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from . import utils
import redis

shorterlink = Flask(__name__)

shorterlink.secret_key = utils.env('SECRET_KEY')

r = redis.from_url(utils.env('REDISTOGO_URL'), int(utils.env('REDIS_DB')))

@shorterlink.route('/', methods=['GET'])
def index():
    return view('layout.html')

@shorterlink.route('/', methods=['POST'])
def make():
    destination = request.form['url']

    if len(destination) == 0:
        flash('please enter a url')
        return redirect(url_for('index'))

    while True:
        url = utils.generate_link(config['url_length'])
        if r.setnx("link:" + url, destination): break

    return view('layout.html', { 'shorterlink': True, 'url': url })

@shorterlink.route('/<link>')
def go(link):
    destination = r.get("link:" + link)
    if destination:
        return redirect(destination)
    flash('no such shorterlink')
    return redirect(url_for('index'))

def view(t, v = {}):
    v['config'] = config
    return render_template(t, **v)
