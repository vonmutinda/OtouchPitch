from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required ,DataRequired

class PitchForm(FlaskForm):
    pitch = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    pitch = TextAreaField(("What's on your mind ?"), validators=[DataRequired()])
    category = SelectField('Category', choices=[('Pickup Lines','Pickup Lines'),('About You','About You'),('Marriage Proposal','Marriage Proposal')])

    submit = SubmitField(('post'))


class CommentForm(FlaskForm):
    comment = StringField('Write a comment',validators=[DataRequired()])
    submit = SubmitField(('comment'))
