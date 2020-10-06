from app import app
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import search_cap
import os
import json

# upload image, text and json files and pass as arguments in render_template()
FILE_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = FILE_FOLDER   # flask app configure files to be uploaded

@app.route('/', methods=['GET','POST'])
def renderMain():
    eye_icon = os.path.join(app.config['UPLOAD_FOLDER'],'images', 'eye_icon.png' )

    YouTube_URL = 'https://www.youtube.com/watch?v=2itlXnURSP4'
    keyword = 'politics'
    num_results = 3

    # get a list of time-caption dictionaries from user input
    captions = search_cap(YouTube_URL, keyword, num_results)


    return render_template('main_page.html',
    icon_image=eye_icon,  captions=captions)

@app.route('/admin/<name>')
def check_admin(name):
    if name == 'jingren':
        return 'Admin status verified.'
    else:
        return 'Please log in as guest.'
