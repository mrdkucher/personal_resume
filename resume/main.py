from flask import Blueprint, flash, render_template, send_file

import sys


bp = Blueprint('main', __name__)


@bp.route("/")
def index():
    return render_template('main/index.html')


@bp.route("/about")
def about():
    return render_template('main/about.html')


@bp.route("/projects")
def projects():
    return render_template('main/projects.html')


@bp.route("/show")
def show_static_pdf():
    print(sys.path)
    with open('kucher_resume/static/DavidKucherResume.pdf', 'rb') as static_file:
        return send_file(static_file, attachment_filename='DavidKucherResume.pdf') # TODO, broken
