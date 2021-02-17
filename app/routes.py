from app import app
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, make_response
from models import search_cap
import os
import json
import requests

# set secret key for the session
import secrets
app.secret_key = secrets.token_urlsafe(16)

###########
# jQuery w Flask, tutorial:
    # https://pythonprogramming.net/jquery-flask-tutorial/
    # http://jqfundamentals.com/chapter/jquery-basics

#########

# upload image, text and json files and pass as arguments in render_template()
FILE_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = FILE_FOLDER   # flask app configure files to be uploaded


######### helper function to process incoming data from client  #########
def embedYouTube(input_url):

    watch_url = input_url.split("&", 1)[0] # drop anything after video_id
    new_url  = ''     # convert link to be embedable in HTML

    if 'www.youtube.com/watch?v=' in watch_url:
        new_url = watch_url.replace('www.youtube.com/watch?v=',
                'www.youtube.com/embed/');

    elif 'www.youtube.com/watch/' in watch_url:
        new_url = watch_url.replace('https://www.youtube.com/watch/',
                'https://www.youtube.com/embed/');

    # also turn on autoplay when page loads
    ytb_configurations = '?autoplay=1&mute=1&cc_load_policy=1&fs=0&modestbranding=1&enablejsapi=1&rel=0&loop=1'
    # make embedded YouTube url
    embedded_url = new_url+ ytb_configurations+'&origin='+input_url+'&start=0'

    return embedded_url

def make_queryURL(user_query_url):
    embedded_url = ''
    # 1 - check if it's a youtube url
    if 'www.youtube.com/watch' in user_query_url:
        # make embedded YouTube url
        embedded_url = embedYouTube(user_query_url)
        return embedded_url


    # 2 - check if it's a ted talk url
    elif "www.ted.com/talks" in user_query_url: # make embedded TED talks url
        embedded_url = user_query_url.replace("www.ted", "embed.ted")
        return embedded_url
    else:
        return user_query_url  # return original url



######### define app routes with python decorator@  #########
@app.route('/explorer_query', methods=['GET','POST'])
def explorer_query():
    # return appropriate url for embedded display depending on url type
    if request.method == "POST":
        query_str = request.form['current_query']
        # query_str = data['current_query']   #retrieve the query string from user input
        print("-----1- ",query_str)
        query_url = make_queryURL(query_str) # convert to embedded explorer url for display
        print("-----2- ",query_url)
        response = jsonify({ 'user_query':  query_str,
                             'user_embedded_url':  query_url })

        print("-----3- ",response)
        return response

    if request.method == "GET":
        print('GET enabled!!!')

        return 'GET enabled!!!'


@app.route('/caption_search', methods=['GET','POST'])
def search_caption():
    # query = request.form
    # print(query)
    if request.method == "POST":
        # prepare relevant user data for caption search
        user_keyword = request.form['current_keyword'] # retrieve user keyword from input
        user_num_results  = int(request.form['current_num_results'])  # retrieve number of search Results from input
        # user_url = request.form['current_user_url']
        # # convert to original, unembedded url for YouTube cap_search
        # original_url = user_url.split('&origin=')[1]
        user_video_id = request.form['current_video_id']
        original_url = 'www.youtube.com/watch?v='+user_video_id

        print((user_keyword, user_num_results, original_url))

        # pass user data to caption search function
        caption_results = search_cap(original_url, user_keyword, user_num_results) # return a list of dictionaries

        print(caption_results)
        print(type(caption_results))
        results_data = {}
        for i in range(len(caption_results)):
            results_data[str(i)] = caption_results[i]
        print(results_data)
        response = jsonify(results_data)

        return response


    if request.method == "GET":
        print('GET enabled!!!')

        print()
        return 'GET enabled!!!'


@app.route('/app', methods=['GET','POST'])
def renderApp(): # just render the main page
    user_url = session['user_url']
    return render_template('main.html', session=session)



@app.route('/', methods=['GET','POST'])
def renderHome():
    # get video URL from user input * should be a CC-ed YouTube link, or null
    input_url= request.form.get('videoURL')

    if request.method == 'POST':
        if input_url: # if there's some input
            user_url = embedYouTube(input_url) # convert to embed url
            # store user url at current session
            session['user_url'] = user_url
            session['input_url'] = input_url
            # redirect to 'app' page
            return redirect(url_for('renderApp'))

        else:
            return render_template('home.html', route='home_1_no_link_input')
    else:
        return render_template('home.html',route='home_2', notes="successful home rendering!")
