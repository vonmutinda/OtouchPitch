from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import UserMixin 
from . import login_manager

class User(UserMixin , db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255) , unique = True , index = True )
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
        
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitches(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer , db.ForeignKey("categories.id"))

    users = db.relationship('User',backref = 'pitch',lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitches.query.filter_by(pitch_id = id).all()

        return pitches


class Category(db.Model):
    
    __tablename__ = 'categories'

    id = db.Column (db.Integer , primary_key = True)
    category = db.Column (db.String)
