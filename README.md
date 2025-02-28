# Personal Website

This repo contains the contents of my [personal website](https://davidkucher.com). Thanks to the helpful guides I listed below!

## Local Usage:
Create a virtual environment:
```
python -m venv venv
pip install flask
```

To run the flask app and modify the app in real time, run:
```
python app.py
```

You should be able to see the app at localhost:8888 in your browser! To freeze it into static files for deployment, run:
```
python app.py freeze
```
And finally, to freeze it and serve with a local web server (again at localhost:8888), run:
```
python app.py serve
```

## Hosting with Cloudflare Pages

I use Cloudflare pages to host this site for free.
To do this, I created a page with the following configuration:
```
Build command: exit 0
Build output: build
Root directory:
Build comments: Enabled
```

This means that the Cloudflare Page will look for changes to this repo, then run a fake build command to simply exit.
Then, the site will be launched with the static files commited to the repo in the build directory.

## Notes:
Created 12/20, based on the [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/ "Flaskr Tutorial") using a free [HTML/CSS theme](https://www.themezy.com/free-website-templates/151-ceevee-free-responsive-website-template "Ceevee template"). With hosting help from this [Medium Guide](https://medium.com/swlh/create-and-host-your-personal-website-for-almost-nothing-pt-2-let-aws-do-the-work-583f2998d21a).