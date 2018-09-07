from . import db

class User ( db.Model ):
    __table__ = "users"
    id 
    username 
    