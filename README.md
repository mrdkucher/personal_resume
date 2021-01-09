# Personal Website

## Notes:
- Created 12/20, based on the [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/ "Flaskr Tutorial").
- Using a free [HTML/CSS theme](https://www.themezy.com/free-website-templates/151-ceevee-free-responsive-website-template "Ceevee template").

## Usage:
`resume/__init__.py` contains the application factory, telling Flask how to setup an instance of the application, including defining blueprints for pages, optionally creating routes, and setting up the application config (from a file or in code) to attach a database, specify debug settings, etc.  
To run the app in a dev environment, be sure to activate the virtualenv (`. venv/bin/activate`), and set the `FLASK_APP` and `FLASK_ENV` env variables to `resume` and `development`, respectively. Then simply run `flask run`.