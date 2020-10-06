from flask import Flask, render_template, send_file, request

app = Flask(__name__)

from app import routes
