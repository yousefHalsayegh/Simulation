from flask import Flask, render_template
from markdown import markdown

def create_app(test_config =None):
    app = Flask(__name__)
        
    # a simple page that says hello
    @app.route('/')
    def index():
        file = open('web\content\landing.md', 'r')

        rm = markdown(file.read())
        return render_template('landing.html', rm=rm)
    
    @app.route('/algorithms')
    def algorithm():

        return render_template('algo_page.html')

    return app

