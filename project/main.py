# main.py

from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from .models import User, Role, Land, Project, Like, User_like, Project_state
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        ideas = Project.query.filter_by(state_id=1).all()
        projects = Project.query.filter(Project.state_id.in_((2,3))).all()
        archive = Project.query.filter(Project.state_id.in_((4,5))).all()
        likes = Like.query.all()
        return render_template('index.html',ideas=ideas, projects=projects, archive=archive, likes=likes)
    else:
        return render_template('index.html')


@main.route('/like_action/<int:project_id>/<int:like_id>')
@login_required
def like_action(project_id, like_id):
    new_like = User_like(user_id=current_user.id, project_id=project_id, like_id=like_id)
    db.session.add(new_like)
    db.session.commit()
    project = Project.query.filter_by(id=project_id).first()
    likes_count = project.get_likes(like_id)
    return {'new_count':likes_count} #redirect(request.referrer)


@main.route('/new_idea', methods=['POST'])
@login_required
def new_idea():
    title = request.form.get('title')
    description = request.form.get('description')
    image = request.form.get('image')
    text = request.form.get('text')
    
    state = Project_state.query.filter_by(level=0).first()

    new_project = Project(title=title,
                             description=description,
                             image=image,
                             text=text,
                             state=state,
                             author=current_user,
                             modifyer=current_user,
                             created_at=datetime.now(),
                             modify_at=datetime.now()
                             )
    db.session.add(new_project)
    db.session.commit()

    return redirect(request.referrer)


@main.route('/project/<int:project_id>')
@login_required
def project_detail(project_id):
    project = Project.query.filter_by(id=project_id).first()
    return render_template('project.html', project=project)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


