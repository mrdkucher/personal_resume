from flask import current_app, Flask, render_template, send_file
from flask_frozen import Freezer
import os
import sys


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/resume/")
def resume():
    return render_template('resume.html')


@app.route("/projects/")
def projects():
    return render_template('projects.html')

# Removing Resume Download for static version
# @app.route("/show/")
# def show_static_pdf():
#     file_url = os.path.join(current_app.root_path, 'static/DavidKucherResume.pdf')
#     return send_file(file_url, mimetype='pdf',
#                      download_name='DavidKucherResume.pdf',
#                      as_attachment=True)


freezer = Freezer(app)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'freeze':
            res = freezer.freeze()
        elif sys.argv[1] == 'serve':
            res = freezer.run()
    else:
        app.run(port=8888)
