# project.py

from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from .models import User, Role, Land, Project, Like, User_like, Project_state
from . import db
from datetime import datetime

project = Blueprint('project', __name__)

@project.route('/project/<int:project_id>/set_state/<int:state_id>')
@login_required
def project_set_state(project_id, state_id):
    project = Project.query.filter_by(id=project_id).first()
    project.set_status(state_id)
    return render_template('project.html', project=project)
