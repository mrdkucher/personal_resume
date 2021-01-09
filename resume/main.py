from flask import Blueprint, current_app, render_template, send_file
import os


bp = Blueprint('main', __name__)


@bp.route("/")
def index():
    return render_template('main/index.html')


@bp.route("/about")
def about():
    return render_template('main/about.html')


@bp.route("/resume")
def resume():
    return render_template('main/resume.html')


@bp.route("/projects")
def projects():
    return render_template('main/projects.html')

# Disabled temporarily
# @bp.route("/contact")
# def contact():
#     return render_template('main/contact.html')


@bp.route("/show")
def show_static_pdf():
    file_url = os.path.join(current_app.root_path, 'static/DavidKucherResume.pdf')
    return send_file(file_url, mimetype='pdf',
                     attachment_filename='DavidKucherResume.pdf',
                     as_attachment=True)
