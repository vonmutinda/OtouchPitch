from flask import render_template 
from . import main 


'''
This routing function fires moment the app loads. 
'''
@main.route('/')
def index():

    return render_template('index.html')

@main.route('/pitches/proposal')
def proposal():

    return render_template('pitches.html')