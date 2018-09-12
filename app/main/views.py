from flask import render_template , request , redirect , url_for , abort , flash
from . import main 

from flask_login import login_required , current_user
from .forms import PitchForm , UpdateProfile ,PostForm , CommentForm
from ..models import Pitch , User
from .. import db , photos

'''
This routing function fires moment the app loads. 
'''
@main.route('/' ,methods=["GET","POST"])
def index():

    proposal = Pitch.query.filter_by(category = 'Marriage Proposal').all()
    openers = Pitch.query.filter_by(category = 'About You').all()
    about = Pitch.query.filter_by(category = 'About You').all()
    form = PostForm()
    if form.validate_on_submit():
        post = Pitch(body=form.pitch.data, author=current_user, category=form.category.data)
        # db.session.add(post)
        # db.session.commit()
        flash('Your pitch has been posted!')

        return redirect(url_for('main.index'))

    # posts = Pitch.retrieve_posts(id).all()


    return render_template('index.html',form=form , proposals = proposal ,  openers = openers , about = about )



'''
This route will navigate to marriage proposal pitches only .

Will query the database for pitches from proposal category then pass them to macro for looping
'''
@main.route('/pitches/proposal',methods=["GET","POST"])
def proposal():

    # pitches = Pitch.get_pitches(proposal)
    pitches = Pitch.query.filter_by(category = 'proposal').all()
    title = 'Marriage Proposal'
    return render_template('pitches.html', title = title , pitches = pitches )


'''
A route for pick-up lines page 
'''
@main.route('/pitch/pick-up')
def pick_up():

    # pitches = Pitch.get_pitches(pick_up)
    pitches = Pitch.query.filter_by(category = 'about-you').all()
    title = 'Pickup Lines'
    return render_template('pitches.html', title = title , pitches = pitches)


'''
A route for pitches of how to best describe yourself in only a minute . 
'''
@main.route('/pitch/describe-yourself')
def about_you():

    pitches = Pitch.query.filter_by(category = 'about-you').all()
    title = 'About yourself'
    return render_template('pitches.html', title = title , pitches = pitches)


'''
saving  pitchest to their respective categories . 
'''

@main.route('/pitch/new-pitch')
@login_required
def save_pitch():
    # category = request.get.args('category')

    form = PitchForm()

    if form.validate_on_submit():
        pitch = form.pitch.data

        new_pitch = Pitch(pitch_id=pitch.id, pitch = pitch.pitch,  user=current_user)
        # new_category = Category (cat = category)

        new_pitch.save_pitch()
        # new_category.save_cat()
        return redirect(url_for('.index'))

    # title = f'{pitch.category} pitch'
    return render_template('pitches.html')



'''
There also could be a route that receives pitches categories as a parameter then

fires a search method in class Pitches and returns appropriate data from db .
'''





'''
A route to redirect you to a user's profile
'''
@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

'''
A route to take you to edit user's profile 
'''

@main.route('/user/<username>/update', methods = ["POST","GET"])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data 

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', username=user.username))

    return render_template("profile/update_profile.html", form = form)


'''
A routing function for uploading profile pictures into our app .
'''

@main.route('/profile/<username>/pic/upload',methods =["POST"])
@login_required
def profile_pic(username):

    user = User.query.filter_by(username = username).first()

    if 'photos' in request.files:
        filename = photos.save(request.files['photos'])
        path = f"photos/{filename}"
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for("main.profile",username=username))


@main.route('/comments/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    comment = Comments.query.filter_by(pitch_id=id).all()

    form_comment = CommentForm()
    if form_comment.validate_on_submit():
        details = form_comment.details.data
        user = current_user

        new_comment = Comments(details = details,pitch_id=id,user =user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('pickuplines.html',form_comment = form_comment,comment=comment,uname = user.username)
