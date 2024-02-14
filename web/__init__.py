from flask import Flask, render_template

def create_app(test_config =None):
    app = Flask(__name__)
        
    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('landing.html')
    
    @app.route('/algorithms')
    def algorithm():

        return render_template('algo_landing.html')
    
    @app.route('/algorithms/<algo>')
    def models(algo):
        
        return render_template('algo_page.html')

    return app

