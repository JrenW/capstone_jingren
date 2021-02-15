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

# @app.route('/cap_search', methods=['GET','POST'])
# def video_hyperlink(): # feature 2 processing
#     user_url = request.form.get['']
#     return


# @app.route('/hypervideo/', methods=['POST'])
# def hypervideo():
#     session['user_url'] = request.form.get('user_url')
#         # >>> should be the first route right after submission of input link
#     return render_template('main.html', session=session,
#         route='capSearch_3_no_search_yet', len=0, time_stamp=[])


# @app.route('/ajax')
# def ajax() :
#
#     current_query = request.form.get('explorer_query')
#     current_query_url = make_queryURL(current_query)
#     response = jsonify({'user_query': current_query,
#                             'query_url': current_query_url })
#
#     return response

# @app.route('/app/hyper_explorer_json')
# def json_hyper_explorer(data):
#     response = jsonify(data)

def embedYouTube(input_url):
    # convert link to be embedable in HTML
    new_url = input_url.replace('https://www.youtube.com/watch?v=',
            'https://www.youtube.com/embed/');
    # also turn on autoplay when page loads
    ytb_configurations = '?autoplay=1&mute=1&cc_load_policy=1&fs=0&modestbranding=1&enablejsapi=1&rel=0&loop=1'
    # make embedded YouTube url
    embedded_url = new_url+ ytb_configurations+'&origin='+input_url

    return embedded_url

# def embedWikipedia(input_url):
#
#     return embedded_url




def make_queryURL(user_query_url):
    embedded_url = ''
    # 1 - check if it's a youtube url
    if 'www.youtube.com/watch?v=' in user_query_url:
        # make embedded YouTube url
        embedded_url = embedYouTube(user_query_url)
        return embedded_url

    elif "www.ted.com/talks" in user_query_url:
        embedded_url = user_query_url.replace("www.ted", "embed.ted")
        return embedded_url
        # make embedded TED talks url


    # https://www.ted.com/talks/david_mackay_a_reality_check_on_renewables?language=en

    else:
        return user_query_url  # return original url


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

        print()
        return 'GET enabled!!!'


@app.route('/caption_search', methods=['GET','POST'])
def search_caption():
    # query = request.form
    # print(query)
    if request.method == "POST":
        # prepare relevant user data for caption search
        user_keyword = request.form['current_keyword'] # retrieve user keyword from input
        user_num_results  = int(request.form['current_num_results'])  # retrieve number of search Results from input
        user_url = request.form['current_user_url']
        # convert to original, unembedded url for YouTube cap_search
        original_url = user_url.split('&origin=')[1]
        print((user_keyword, user_num_results, original_url))

        # pass user data to caption search function
        caption_results = search_cap(original_url, user_keyword, user_num_results) # return a list of dictionaries

        print(caption_results)
        print(type(caption_results))
        results_data = {}
        for i in range(len(caption_results)):
            results_data[str(i)] = caption_results[i]
        print(results_data)
        #
        # # results_data = {}
        # results_data['results'] = caption_results
        # results_data['index'] = [i for i in range(len(caption_results))]
        # return jsonified caption results to client
        response = jsonify(results_data)

        # print(response)
        # return user_keyword
        return response

    if request.method == "GET":
        print('GET enabled!!!')

        print()
        return 'GET enabled!!!'


# def json_hyper_explorer():
#     data = request.data.decode("utf-8")
#     print(data[0])
#     current_query = data.current_query
#     user_query_url = make_queryURL(current_query)
#
#     data = {}
#     data['explorer_query'] = current_query
#     data['query_url'] = user_query_url
#
#     response = jsonify(data)
#     return response



@app.route('/app', methods=['GET','POST'])
def renderApp(): # feature 2 processing
    user_url = session['user_url']

    if request.form.get('explorer_query'):

        return "EXPLORER ON"
        # current_query = request.form.get('explorer_query')
        # current_query_url = make_queryURL(current_query)
        # # response = jsonify({'user_query': current_query,
        # #                     'query_url': current_query_url })
        #
        # data = {} #make a dictionary uf user data
        # data['user_query'] = current_query
        # data['query_url'] = current_query_url
        #
        # return redirect(url_for('json_hyper_explorer', data=data))


        # with open('user.json', 'w') as outfile:
        #     json.dump(data, outfile)
        # #
        # console.log(response)
        # return response

    return render_template('main.html', session=session)



@app.route('/', methods=['GET','POST'])
def renderHome():
    # get video URL from user input * should be a CC-ed YouTube link, or null
    input_url= request.form.get('videoURL')

    if request.method == 'POST':
        if input_url: # if there's some input

            # convert link to be embedable in HTML
            # embeded_url = input_url.replace('https://www.youtube.com/watch?v=',
            #         'https://www.youtube.com/embed/');
            # # also turn on autoplay when page loads
            # ytb_configurations = '?autoplay=1&mute=1&cc_load_policy=1&fs=0&modestbranding=1&enablejsapi=1&rel=0&loop=1'
            # user_url = embeded_url+ ytb_configurations+'&origin='+input_url
            user_url = embedYouTube(input_url)

            # store user url at current session
            session['user_url'] = user_url
            session['input_url'] = input_url

            # redirect to 'app' page
            return redirect(url_for('renderApp'))

        else:
            return render_template('home.html', route='home_1_no_link_input')
    else:
        return render_template('home.html',route='home_2', notes="successful home rendering!")
