from flask import Flask, render_template

def create_app(test_config =None):
    app = Flask(__name__)
        
    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('landing.html')

    return app