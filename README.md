# Capstone Project, Class 2021

## Project title: Active Learning ‘with-IN’ MOOC-style Videos 
### Student Name:  Jingren Wang, Class 2021
### Major: Computational Science
### Concentrations: Artificial Intelligence & Data Science

## Abstract

Thanks to the Massive Open Online Courses (MOOCs) movement, self-learning has become more efficient by home-watching lecture videos curated by top universities worldwide. However, few self-learners can sit through college lecture videos which commonly run for two to three hours. Surprisingly 90% of MOOCs students drop out quickly after two-week enrollment. Although lecture videos are great for knowledge dissemination, their heavy length and lack of interactivity often stifle “active learning”, the power engine of one’s life-long intellectual growth.<br>

With a vision to make the MOOCs experience much more “active” for the benefits of self-learners, my project aims to turn passive video “watching” into active video “reading” by interacting with features “with-IN” the video frame. First, this project explores various machine-learning algorithms on automatic video content extraction & learning; then apply learning results to build a web interface with features like: <br>

  1) a caption-based keyword search engine to find contents within a video; <br>
  2) a floating  ‘explorer’ to search external multimedia resources (e.g. wikipedia) while streaming the lecture video; <br>
   3) editing tool to create intra-video hyperlinks for nonlinear content navigation; <br>
    
The final product is a working web app built on python Flask framework. The app will accept a youtube video link and redirect to the main page where users can interact with all three interactive learning features outlined above.

## File System
* app folder - contains all Flask web routes defined in 'main.py'; 'templates' folder for all htmls, and static folder for graphical icons.
* main.py - contain all decorated functions registered to Flask app routes to handle different concerns separately; helper functions are also included here; most importantly, a flask 'app' instance is initiated here. 
* run.py - this file launch the app instance declared in main.py
* models.py - a separate python file to collect all backend algorithms for data processing
* requirements.txt - contain a list of required modules and their versions for Flask app functios to work properly
* Procfile - a file for Heroku to understand what to do once app is built for deployment
*  run_app.txt - auxiliary file to instruct manual deployment on local machine

## App Deployment 

### Deploy with Heroku
The app will be deployed with Heroku: https://hypervideo-learning.herokuapp.com/

*Note: please try and reload the webpage for several times if you encountered a 500 Internal Server Error, especially if you are behind a proxy.

### Manual Deployment from Git clone

#### Requirements
- Python 3
- Pip 3
Pip3 is installed with Python3

    $ brew install python3

#### Run Virtual Environment
Virtual environment is a key component in ensuring that the application is configured in the right environment

#### Installation
To install virtualenv via pip run:

    $ pip3 install virtualenv

#### Run the Application 
#### (see below, or follow instructions in run_app.txt)
    $ python -m venv venv
    $ source venv/bin/activate # for MAC/UNIX
    $ venv\Scripts\activate # for WINDOWS
    $ pip install -r requirements.txt  
    $ export FLASK_ENV=development # configure flask app
    $ export FLASK_CONFIG=dev
    $ export FLASK_APP=web
    $ python3 -m flask run  # python run flask

