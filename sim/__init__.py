from flask import Flask, render_template
from markdown import markdown

def create_app(test_config =None):
    app = Flask(__name__)
        
    # a simple page that says hello
    @app.route('/')
    def index():
        file = open('ReadME.md', 'r')

        rm = markdown(file.read())
        return render_template('landing.html', rm=rm)

    return app