from flask import Flask, render_template
from ai.node import Node

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
        tree = Node(10)
        tree.insert_node(12)
        return render_template('algo_page.html', output=tree)

    return app

