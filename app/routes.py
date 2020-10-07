from app import app
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import search_cap
import os
import json

# upload image, text and json files and pass as arguments in render_template()
FILE_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = FILE_FOLDER   # flask app configure files to be uploaded

# set secret key for the session
import secrets
app.secret_key = secrets.token_urlsafe(16)


@app.route('/cap_search', methods=['GET','POST'])
def captionSearch():
    if request.method == 'POST':
        # fetch user input
        keyword = request.form.get('keyword') # required
        num_results = int(request.form.get('num_results')) # required
        YouTube_URL = session['input_url']

        # check necessary inputs to start a search
        if None not in (YouTube_URL, keyword, num_results):
            # search caption and display
            captions = search_cap(YouTube_URL, keyword, num_results)
            autoplay_link = ssession['input_url']+
            # ref: https://stackoverflow.com/questions/7281765/how-to-embed-an-autoplaying-youtube-video-in-an-iframe

            return render_template('main_page.html',input_url=session['input_url'],
                            keyword=keyword, num_results=str(num_results),
                            route='capSearch_1', captions=captions,
                            autoplay_link=)

                # return render_template('main_page.html', captions=captions,
                #         keyword=keyword, num_results=num_results)

        else:
            return render_template('main_page.html',input_url=session['input_url'],
                            keyword=keyword, num_results=str(num_results),
                            notes="either keyword or user_url is missing...",
                            route='capSearch_2')

    else:
        return render_template('main_page.html', input_url=session['input_url'], route='capSearch_3')



@app.route('/', methods=['GET','POST'])
def renderMain():
    eye_icon = os.path.join(app.config['UPLOAD_FOLDER'],'images', 'eye_icon.png' )

    # request data from user input
    if request.method == 'POST':
        input_url= request.form.get('videoURL')
        #user_url = input_url
        if input_url:
            # store user url for the current session before redirecting
            session['input_url'] = input_url
            return redirect(url_for('captionSearch', input_url=input_url))

        else:
            return render_template('home.html')
    else:
        return render_template('home.html')



@app.route('/admin/<name>')
def check_admin(name):
    if name == 'jingren':
        return 'Admin status verified.'
    else:
        return 'Please log in as guest.'
