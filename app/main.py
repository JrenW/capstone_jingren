''' This script contains all flask routes and associated functions to handle server requests,
    process data and make response. decorators '@' are used to extend additional functionality
    under each route name.
'''
# import necessary packages
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from models import search_cap

# initialize a flask app object
app = Flask(__name__)

# set secret key for the current session
import secrets
app.secret_key = secrets.token_urlsafe(16)

######### helper function to process incoming data from client  #########
def embedYouTube(input_url):
    '''turn YouTube public link into embedable link'''

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
    '''embed url link from input: hypervideo explorer
        the returned link is used in explorer_query() function below
        to render an embedded tutorial video in the main page
        * currently supporting YouTube and TED talks embedding, some other free educational resources
            are directly renderable without processing
    '''

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


######### define app routes with python decorator @  #########
@app.route('/explorer_query', methods=['GET','POST'])
def explorer_query():
    ''' upon a POST request, this function retrieves the current user query from the
        hypervideo explorer input box (green), then tries to convert it to an embedable link
        return a jsonified response back to server
    '''
    # return appropriate url for embedded display depending on url type
    if request.method == "POST":
        query_str = request.form['current_query']
        query_url = make_queryURL(query_str) # convert to embedded explorer url for display
        response = jsonify({ 'user_query':  query_str,
                             'user_embedded_url':  query_url })
        return response

    if request.method == "GET":
        # else do nothing, but flag a GET request
        return 'This is a GET request'


@app.route('/caption_search', methods=['GET','POST'])
def search_caption():
    '''Upon a POST request, this function retrieves two values from the client
        1) keyword (phrase): the keyword(s) user wants to locate in the video content
        2) number of results: maximum number of captions containing the keyword
         the function calls search_cap() from models.py to apply the backend searching algorithm
         then return a jsonified dictionary of {timestamp, capstone}
    '''

    if request.method == "POST":
        # prepare relevant user data for caption search
        user_keyword = request.form['current_keyword'] # retrieve user keyword from input
        user_num_results  = int(request.form['current_num_results'])  # retrieve number of search Results from input

        user_video_id = request.form['current_video_id']
        original_url = 'www.youtube.com/watch?v='+user_video_id

        # pass user data to caption search function
        caption_results = search_cap(original_url, user_keyword, user_num_results) # return a list of dictionaries

        results_data = {} # make a dictionary of search results
        for i in range(len(caption_results)):
            results_data[str(i)] = caption_results[i]

        response = jsonify(results_data) # make response

        return response


    if request.method == "GET":
        # else do nothing, but flag a GET request
        return 'This is a GET request'


@app.route('/app', methods=['GET','POST'])
def renderApp(): # just render the main page
    '''render the main page where user can interact with three hypervideo features'''
    return render_template('main.html', session=session)


@app.route('/', methods=['GET','POST'])
def renderHome():
    '''this is the firts webpage a user will see.
        a user can insert a YouTube lecture link of her choosing and
        begin her journey in the Hypervideo Room.
        * home page will be more useful when a user-login system is built
    '''

    # get video URL from user input * should be a CC-ed YouTube link, or null
    input_url= request.form.get('videoURL')

    if request.method == 'POST':
        if input_url: # if there's some input
            user_url = embedYouTube(input_url) # convert to embed url

            # store user url at current session
            session['user_url'] = user_url
            session['input_url'] = input_url

            # store videoID for YouTube player API
            videoID = input_url.split('?v=')[1]
            session['videoID'] = videoID
            # redirect to 'app' page
            return redirect(url_for('renderApp'))

        else: # if there's no input, wait and do nothing
            return render_template('home.html')
    else: # if this is the first redirect, render home page
        return render_template('home.html')
