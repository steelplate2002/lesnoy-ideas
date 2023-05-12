# main.py

from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from .models import User, Role, Land, Project, Like, User_like
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        click = request.form.get('like_click').split(':')
        new_like = User_like(user_id=click[0], project_id=click[1], like_id=click[2])
        db.session.add(new_like)
        db.session.commit()

    if current_user.is_authenticated:
        ideas = Project.query.all()
        likes = Like.query.all()
        return render_template('index.html',ideas=ideas, likes=likes)
    else:
        return render_template('index.html')


@main.route('/like_action/<int:project_id>/<int:like_id>')
@login_required
def like_action(project_id, like_id):
    new_like = User_like(user_id=current_user.id, project_id=project_id, like_id=like_id)
    db.session.add(new_like)
    db.session.commit()
    return redirect(request.referrer)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


