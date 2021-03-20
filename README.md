# Capstone Project, Class 2021

## Project title: Active Learning ‘with-IN’ MOOC-style Videos 
### Student Name:  Jingren Wang, Class 2021
### Major: Computational Science
### Concentrations: Artificial Intelligence & Data Science

## Abstract

Thanks to the Massive Open Online Courses (MOOCs) movement, self-learning has become more efficient by home-watching lecture videos curated by top universities around the world. However, few self learners can really sit through college lecture videos which commonly run for two to three hours. In fact, 90% of MOOCs students drop out quickly after 2-week enrollment. Although lecture videos are great for knowledge dissemination, its heavy length and lack of interactivity often stifles “Active Learning”, the power engine of one’s life-long intellectual growth.<br>
With a vision to make the MOOCs experience much more ‘active’ for the benefits of self-learners, my project aims to turn passive video ‘watching’ into active video ‘reading’ by interacting with features 'with-IN' the video frame. First, this project explores various machine-learning algorithms on automatic video content extraction & learning; then apply learning results to build a web interface with features like: <br>
      1) a caption-based keyword search engine to find contents within a video; <br>
      2) a floating  ‘explorer’ to search external multimedia resources (e.g. wikipedia) while streaming the lecture video; <br>
      3) editing tool to create intra-video hyperlinks for nonlinear content navigation; <br>
The final product is a working web app running on Flask virtual server that accepts a youtube video link and displays all three interactive learning features outlined above.


## App design
[to be updated ]

The overall navigation journey of my app would eventually look like: 
    User Login/Set up page
    -->  User home: user insert a YouTube video link
            --> Learning Room:  nonlinear navigation of video content using three features
            -->  (maybe) save video / share video annotations to others
--> Logout/ Error handling


## How to use the app?

### Run Virtual Environment
Virtual environment is a key component in ensuring that the application is configured in the right environment

#### Requirements
- Python 3
- Pip 3
Pip3 is installed with Python3

    $ brew install python3

#### Installation
To install virtualenv via pip run:

    $ pip3 install virtualenv

### Deployment with Heroku
The app will be deployed with Heroku: [Heroku link to be inserted]

### Environment Variables
All environment variables will be stored within the .env file (yet to be created) and loaded with dotenv package.

### Run the Application 
#### (see below, or follow instructions in run_app.txt)
    $ python -m venv venv
    $ source venv/bin/activate # for MAC/UNIX
    $ venv\Scripts\activate # for WINDOWS
    $ pip install -r requirements.txt  
    $ export FLASK_ENV=development # configure flask app
    $ export FLASK_CONFIG=dev
    $ export FLASK_APP=web
    $ python3 -m flask run  # python run flask

## Resources
### for documents in-progress, please see my google drive: https://drive.google.com/drive/folders/11VS7SFv23FTX2LhctoTj2ppV-NOeCDhf?usp=sharing
