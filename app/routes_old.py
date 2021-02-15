from app import app
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, make_response
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

@app.route('/hypervideo/', methods=['POST'])
def hypervideo():
    session['user_url'] = request.form.get('user_url')
        # >>> should be the first route right after submission of input link
    return render_template('main_page.html', session=session,
        route='capSearch_3_no_search_yet', len=0, time_stamp=[])


@app.route('/caption_search/', methods=['POST'])
def caption_search():
    # # first, fetch and process input URL
    # input_url = session['input_url']
    # # prossess the link string to embed in HTML & autoplay
    # embeded_url = input_url.replace('https://www.youtube.com/watch?v=',
    #         'https://www.youtube.com/embed/');
    # user_url = embeded_url+'?autoplay=1?control=0'
    # # store user url for the current session before search
    # session['user_url'] = user_url

    user_url=session['user_url']
    # initialize session variables
    session['keyword'] = None
    session['num_results'] = None
    session['explorer_url'] = None


    if request.method == 'POST':
        # fetch user input (from all three features)
        keyword = request.form.get('keyword')
        num_results = request.form.get('num_results')

        # save in cookie
        session['keyword'] = keyword
        session['num_results'] = num_results
        original_URL = session['input_url']


        # feature 1 inputs if any check necessary inputs to start a search
        if None not in (original_URL, keyword, num_results):
            # search caption and display
            captions = search_cap(original_URL, keyword, int(num_results))
            session['search_results'] = captions # save those search results
            # convert caption results into icon positions on html
            frame_width = 776 # set as 800px
            icon_pos = []
            time_stamp = []

            for cap in captions:
                pos = str(frame_width * cap['progress']+12) #left-shift 12px
                icon_pos.append(pos)
                time_stamp.append(cap['time'])
            #
            # session['input_url'] = original_URL # save the original url again
            #
            # response = make_response(jsonify(user_url=session['user_url'],
            #             keyword=session['keyword'], num_results=str(session['num_results']),
            #             explorer_url=session['explorer_url'],
            #             captions=captions,
            #             icon_pos=icon_pos, time_stamp=time_stamp,
            #             len=len(icon_pos),
            #             route='capSearch_1', notes="successful caption search" ))
            #
            # return response

            #*NEW IDEA: don't render template, but return a json file
                # sending searched results to jquery for sectional display
                # tutorial: https://stackoverflow.com/questions/52290310/receive-data-with-flask-and-send-data-with-jquery

            return render_template('main_page.html',session=session, user_url=user_url,
                            original_URL=session['input_url'],
                            keyword=keyword, num_results=str(num_results),
                            route='capSearch_1', captions=captions,
                            icon_pos=icon_pos,time_stamp=time_stamp,
                            len=len(icon_pos), notes="successful caption search" )


@app.route('/video_hyperlink/', methods=['POST'])
def video_hyperlink():
    # feature 2 inputs if any
    user_url = session['user_url']
    explorer_query = request.form.get('explorer_query')
    session['explorer_query'] = explorer_query

    if session['explorer_query']:
        query_url = explorer_query.replace(' ','+')
        session['explorer_url']= "https://www.google.com/search?igu=1&ei=&q=" + query_url# str for the embedded explorer

        return render_template('main_page.html',session=session, user_url=user_url, original_URL=session['input_url'])



@app.route('/', methods=['GET','POST'])
def renderMain():
    eye_icon = os.path.join(app.config['UPLOAD_FOLDER'],'images', 'eye_icon.png' )

    # request data from user input
    if request.method == 'POST':
        input_url= request.form.get('videoURL')

        if input_url: # if there is some input
            session['input_url'] = input_url #store the original URL
            # prossess the link string to embed in HTML & autoplay
            embeded_url = input_url.replace('https://www.youtube.com/watch?v=',
                    'https://www.youtube.com/embed/');
            user_url = embeded_url+'?autoplay=1?control=0'
            # store user url for the current session before search
            session['user_url'] = user_url
            # initiate key vars
            session['keyword'] = None
            session['num_results'] = None
            session['explorer_query'] = None

            return render_template('main_page.html',session=session, user_url=session['user_url'], original_URL=input_url)

        else:
            return render_template('home.html',session=session, route='home_1_no_link_input')

    else:
        return render_template('home.html',route='home_2', notes="successful home rendering!")



@app.route('/admin/<name>')
def check_admin(name):
    if name == 'jingren':
        return 'Admin status verified.'
    else:
        return 'Please log in as guest.'
