from flask import render_template , request , redirect , url_for 
from . import main 

from flask_login import login_required , current_user
from .forms import PitchForm 
from ..models import Pitch

'''
This routing function fires moment the app loads. 
'''
@main.route('/')
def index():

    proposal = Pitch.get_pitches('proposal')
    openers = Pitch.get_pitches('openers')
    about = Pitch.get_pitches('about')

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
@login_required
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
        title = form.title.data
        review = form.review.data

        # new_review = Review(movie.id,title,movie.poster,review)
        # Updated review instance
        new_pitch = Pitch(pitch_id=pitch.id, pitch = pitch.pitch,  user=current_user)

        new_pitch.save_pitch()
        return redirect(url_for('.movie',id = pitch.id ))

    title = f'{pitch.category} pitch'
    return render_template('pitches.html')