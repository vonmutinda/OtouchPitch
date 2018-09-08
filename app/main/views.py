from flask import render_template 
from . import main 


'''
This routing function fires moment the app loads. 
'''
@main.route('/')
def index():

    return render_template('index.html')


'''
This route will navigate to marriage proposal pitches only .

Will query the database for pitches from proposal category then pass them to macro for looping
'''
@main.route('/pitches/proposal')
def proposal():

    return render_template('pitches.html')


'''
A route for pick-up lines page 
'''
@main.route('/pitch/pick-up')
def pick_up():


    return render_template('pitches.html')


'''
A route for pitches of how to best describe yourself in only a minute . 
'''
@main.route('/pitch/describe-yourself')
def about_you():


    return render_template('pitches.html')