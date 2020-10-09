from app import app
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import search_cap
import os
import json


###########
# jQuery w Flask, tutorial:
    # https://pythonprogramming.net/jquery-flask-tutorial/
    # http://jqfundamentals.com/chapter/jquery-basics

#########

# upload image, text and json files and pass as arguments in render_template()
FILE_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = FILE_FOLDER   # flask app configure files to be uploaded

# set secret key for the session
import secrets
app.secret_key = secrets.token_urlsafe(16)


@app.route('/cap_search/', methods=['GET','POST'])

def captionSearch():

    # first, fetch and process input URL
    input_url = session['input_url']
    # prossess the link string to embed in HTML & autoplay
    embeded_url = input_url.replace('https://www.youtube.com/watch?v=',
            'http://www.youtube.com/embed/');
    user_url = embeded_url+'?autoplay=1?control=0'
    # store user url for the current session before search
    session['user_url'] = user_url

    if request.method == 'POST':
        # fetch user input
        keyword = request.form.get('keyword') # required
        num_results = int(request.form.get('num_results')) # required

        # save in cookie
        session['keyword'] = keyword
        session['num_results'] = num_results

        original_URL = session['input_url']


        # check necessary inputs to start a search
        if None not in (original_URL, keyword, num_results):
            # search caption and display
            captions = search_cap(original_URL, keyword, num_results)
            session['search_results'] = captions # save those search results

            # convert caption results into icon positions on html
            frame_width = 776 # set as 800px
            icon_pos = []
            time_stamp = []

            for cap in captions:
                pos = str(frame_width * cap['progress']+12) #left-shift 12px
                icon_pos.append(pos)
                time_stamp.append(cap['time'])

            session['input_url'] = original_URL # save the original url again

            #*NEW IDEA: don't render template, but return a json file
                # sending searched results to jquery for sectional display
                # tutorial: https://stackoverflow.com/questions/52290310/receive-data-with-flask-and-send-data-with-jquery
            return render_template('main_page.html',user_url=session['user_url'],
                            keyword=keyword, num_results=str(num_results),
                            route='capSearch_1', captions=captions,
                            icon_pos=icon_pos,time_stamp=time_stamp,
                            len=len(icon_pos))

                # return render_template('main_page.html', captions=captions,
                #         keyword=keyword, num_results=num_results)

        else:
            return render_template('main_page.html', user_url=session['user_url'],
                            keyword=keyword, num_results=str(num_results),
                            notes="either keyword or user_url is missing...",  len=0,
                            route='capSearch_2')
    else: # GET
        # >>> should be the first route right after submission of input link
        return render_template('main_page.html', user_url=session['user_url'],
        route='capSearch_3_no_search_yet', len=0, time_stamp=[])



@app.route('/', methods=['GET','POST'])
def renderMain():
    eye_icon = os.path.join(app.config['UPLOAD_FOLDER'],'images', 'eye_icon.png' )

    # request data from user input
    if request.method == 'POST':
        input_url= request.form.get('videoURL')

        if input_url: # if there is some input
            # *TO DO*: check if the input link is a proper YouTube link

            # store the input URL in a cookie session
            session['input_url'] = input_url
            return redirect(url_for('captionSearch'))

        else:
            return render_template('home.html',route='home_1_no_link_input')

    else:
        return render_template('home.html',route='home_2')



@app.route('/admin/<name>')
def check_admin(name):
    if name == 'jingren':
        return 'Admin status verified.'
    else:
        return 'Please log in as guest.'
