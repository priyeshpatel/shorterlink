from flask import Flask, request, redirect, url_for, flash
from . import utils, config 

shorterlink = Flask(__name__)

shorterlink.secret_key = config.env('SECRET_KEY')

@shorterlink.route('/', methods=['GET'])
def index():
    return utils.view('layout.html')

@shorterlink.route('/', methods=['POST'])
def make():
    destination = request.form['url']

    if len(destination) == 0:
        flash('please enter a url')
        return redirect(url_for('index'))

    url = utils.create(destination)

    return utils.view('layout.html', { 'shorterlink': True, 'url': url })

@shorterlink.route('/<link>')
def go(link):
    destination = utils.get(link)

    if destination:
        return redirect(destination)

    flash('no such shorterlink')
    return redirect(url_for('index'))
