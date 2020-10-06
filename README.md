# Capstone Project, Class 2021

### Project title: Active Learning ‘with-IN’ MOOC-style Videos 
### Student Name:  Jingren Wang, Class 2021
### Major: Computational Science
### Concentrations: Artificial Intelligence & Data Science

## Abstract

Thanks to the Massive Open Online Courses (MOOCs) movement, self-learning has become more efficient by home-watching lecture videos curated by top universities around the world. However, few self learners can really sit through, say, a three-hour Cambridge lecture video on Information Theory. In fact, 90% of MOOCs students drop out quickly after 2-week enrollment. Although lecture videos are great for knowledge dissemination, its heavy length and lack of interactivity often stifles “Active Learning”, the power engine of one’s life-long intellectual growth. <br>
With a vision to make the MOOCs experience much more ‘active’ for the benefits of self-learners, my project aims to turn passive video ‘watching’ into active video ‘reading’ by interacting with features 'with-IN' the video frame. First, the project will explore various machine-learning algorithms on automatic video content extraction & learning; then apply learning results to build a web interface with features like **1) caption-based content search within a lecture videos; 2) video moment annotation toolbox; and 3) video-to-video hyperlinks for nonlinear content navigation.**
The final product is going to be a working web app running on Flask which takes in a youtube video link and displays interactive features stated above.

## Progress
[Early Stage]
- Preliminary User Interest Research [DONE]
- Gap Analysis [70% DONE]
- MVP [50% DONE] -- *only on first feature -- caption-based keyword search
- Detailed Outline [90%] -- *reflected in CP192 final proposal

[Middle Stage]
- Commented code/ annotated products [35%]
- Analysis and user feedback [15%]
- Visuals/Schematics [40%]
- Incorporation of feedbacks [0%]
- Backgruond section [100% DONE]

[Late Stage]
0%


## How to use the app?
# Run Virtual Environment
Virtual environment is a key component in ensuring that the application is configured in the right environment

# Requirements
- Python 3
- Pip 3
> $ brew install python3
Pip3 is installed with Python3

# Installation
To install virtualenv via pip run:

> $ pip3 install virtualenv

# Deployment with Heroku
The app will be deployed with Heroku: [Heroku link to be inserted]

# Environment Variables
All environment variables will be stored within the .env file (yet to be created) and loaded with dotenv package.

# Run the Application (to be updated)
> $ python -m venv venv
> $ source venv/bin/activate
> # Activate virtual environment for MAC/UNIX
> $ venv\Scripts\activate
> # Activate virtual environment for WINDOWS
> $ pip install -r requirements.txt
> $ export FLASK_ENV=development
> $ export FLASK_CONFIG=dev
> $ export FLASK_APP=web
> $ python3 -m flask run


## Resources
### google drive link: https://drive.google.com/drive/folders/11VS7SFv23FTX2LhctoTj2ppV-NOeCDhf?usp=sharing
