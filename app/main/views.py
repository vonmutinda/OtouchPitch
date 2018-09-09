from flask import render_template , request , redirect , url_for 
from . import main 

from flask_login import login_required , current_user
from .forms import PitchForm 
from ..models import Pitch , Category

'''
This routing function fires moment the app loads. 
'''
@main.route('/')
def index():

    proposal = Pitch.get_pitches('proposal')
    openers = Pitch.get_pitches('openers')
    about = Pitch.get_pitches('about')

    return render_template('index.html',proposal=proposal,openers=openers,about=about)



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


'''
saving  pitchest to their respective categories . 
'''

@main.route('/pitch/new-pitch')
@login_required
def save_pitch():
    category = request.get.args('category')

    form = PitchForm()

    if form.validate_on_submit():
        pitch = form.pitch.data

        new_pitch = Pitch(pitch_id=pitch.id, pitch = pitch.pitch,  user=current_user)
        new_category = Category (cat = category)

        new_pitch.save_pitch()
        new_category.save_cat()
        return redirect(url_for('.index'))

    # title = f'{pitch.category} pitch'
    return render_template('pitches.html')



'''
There also could be a route that receives pitches categories as a parameter then

fires a search method in class Pitches and returns appropriate data from db .
'''