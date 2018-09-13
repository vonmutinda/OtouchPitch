from flask import render_template , request , redirect , url_for , abort , flash
from . import main 

from flask_login import login_required , current_user
from .forms import PitchForm , UpdateProfile ,PostForm , CommentForm
from ..models import Pitch , User ,Comment
from .. import db , photos

'''
This routing function fires moment the app loads. 
'''
@main.route('/' ,methods=["GET","POST"])
def index():

    form = PostForm()
    form_comment = CommentForm()

    pickup = Pitch.query.filter_by(category = "Pickup Lines").all()
    about = Pitch.query.filter_by(category = "About You").all()
    marryme = Pitch.query.filter_by(category = "Marriage Proposal").all()

    author = current_user
    if author:
        if form.validate_on_submit():
            form = Pitch(pitch=form.pitch.data, user=author, category=form.category.data)

            form.save_pitch()

            flash('Your pitch has been posted!')

            return redirect(url_for('.index'))


    else:
        flash("You need to be logged in") 
 
    return render_template('index.html',form = form ,form_comment = form_comment , pickup = pickup,about=about,marryme=marryme)

# @main.route('/posting')
# @login_required
# def home():
#     return  render_template('auth/login.html')

'''
This route will navigate to marriage proposal pitches only .

Will query the database for pitches from proposal category then pass them to macro for looping
'''
@main.route('/pitches/proposal',methods=["GET","POST"])
@login_required
def proposal(): 
    pitches = Pitch.query.filter_by(category = 'Marriage Proposal').all()
    title = 'Marriage Proposal'

    return render_template('pitches.html', title = title ,pitches = pitches )


'''
A route for pick-up lines page 
'''
@main.route('/pitch/pick-up',methods=["GET","POST"])
@login_required
def pick_up():

    pitches = Pitch.query.filter_by(category = 'Pickup Lines').all()
    title = 'Pickup Lines'
    return render_template('pitches.html', title = title,pitches = pitches )


'''
A route for pitches of how to best describe yourself in only a minute . 
'''
@main.route('/pitch/describe-yourself',methods=["GET","POST"])
@login_required
def about_you():

    pitches = Pitch.query.filter_by(category = 'About You').all()

    title = 'About yourself'
    return render_template('pitches.html', title = title , pitches = pitches )




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

@main.route('/profile/<username>/pic/upload',methods =["POST","GET"])
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
    comment = Comment.query.filter_by(pitch_id=id).all()
    user = current_user

    form_comment = CommentForm()
    if form_comment.validate_on_submit():
        details = form_comment.details.data
        user = current_user

        new_comment = Comment(details = details,pitch_id=id,user =user)
        db.session.add(new_comment)
        db.session.commit()

    return render_template('comments.html',form_comment = form_comment,comment=comment,uname = user.username)
