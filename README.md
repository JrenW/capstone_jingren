# Capstone Project, Class 2021

### Project title: Active Learning ‘with-IN’ MOOC-style Videos 
### Student Name:  Jingren Wang, Class 2021
### Major: Computational Science
### Concentrations: Artificial Intelligence & Data Science

## Abstract

Thanks to the Massive Open Online Courses (MOOCs) movement, self-learning has become more efficient by home-watching lecture videos curated by top universities around the world. However, few self learners can really sit through, say, a three-hour Cambridge lecture video on Information Theory. In fact, 90% of MOOCs students drop out quickly after 2-week enrollment. Although lecture videos are great for knowledge dissemination, its heavy length and lack of interactivity often stifles “Active Learning”, the power engine of one’s life-long intellectual growth. <br>

With a vision to make the MOOCs experience much more ‘active’ for the benefits of self-learners, my project aims to turn passive video ‘watching’ into active video ‘reading’ by interacting with features 'with-IN' the video frame. First, the project will explore various machine-learning algorithms on automatic video content extraction & learning; then apply learning results to build a web interface with features like: <br>
      1) caption-based keyword search within a lecture videos; 
      2) editing tool for users to DIY intra-video hyperlinks for nonlinear content navigation; 
      3) embedded explorer to search and hyper-link one moment to outside video/multimedia resources; 
<br>
The final product is going to be a working web app running on Flask virtual server which takes in a youtube video link and displays interactive features stated above.

## Progress

**[Early Stage]**
- Preliminary User Interest Research [100%]
- Gap Analysis [100% ]
- MVP [80% ] -- *only on first feature -- caption-based keyword search
- Detailed Outline [100%]

**[Middle Stage]**
- Background & Literature Review [100% ]
- Product Visuals/Schematics - Mockups [70%]
- Commented code/ annotated products [45%]
- Analysis and user feedback [50%]
- Incorporation of feedbacks into feature iterations [40%]

**[Late Stage]**
0%


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
