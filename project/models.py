# models.py

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    phone_number = db.Column(db.String)

    land_id = db.Column(db.Integer, db.ForeignKey('land.id'))
    land = db.relationship('Land',
        backref=db.backref('users', lazy='dynamic'))

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role',
        backref=db.backref('users', lazy='dynamic'))


class Land(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    level = db.Column(db.Integer)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(2000))
    text = db.Column(db.Text)
    image = db.Column(db.String(1000))

    state_id = db.Column(db.Integer, db.ForeignKey('project_state.id'))
    state = db.relationship('Project_state',
        backref=db.backref('projects', lazy='dynamic'))

    created_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', foreign_keys=[author_id],
        backref=db.backref('projects_create', lazy='dynamic'))

    modify_at = db.Column(db.DateTime)
    modifyer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    modifyer = db.relationship('User', foreign_keys=[modifyer_id],
        backref=db.backref('projects_modify', lazy='dynamic'))
    

    def set_status(self, state_id):
        if state_id < 6:
            self.state_id = state_id
            db.session.commit()
        return


    def get_likes(self, like_id):
        likes = self.likes.filter_by(like_id=like_id).all() 
        return len(likes)

    def likes_count(self):
        likes = Like.query.all()
        likes_set = []
        for like in likes:
            likes_count = len(self.likes.filter_by(like_id=like.id).all())
            likes_set.append({'like':like, 'count':likes_count})
        return likes_set


class Project_state(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    name = db.Column(db.String(100))
    icon = db.Column(db.String(100))


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True)
    descr = db.Column(db.String(100))
    icon = db.Column(db.String(100))
    color = db.Column(db.String(100))
    wieght = db.Column(db.Integer)


class User_like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_number = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('likes', lazy='dynamic'))
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship('Project',
        backref=db.backref('likes', lazy='dynamic'))
    
    like_id = db.Column(db.Integer, db.ForeignKey('like.id'))
    like = db.relationship('Like',
        backref=db.backref('project_likes', lazy='dynamic'))


