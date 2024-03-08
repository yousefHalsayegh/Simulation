import random as rd
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
        tree = Node(rd.randint(1,100))
        for i in range(10):
            tree.insert_node(rd.randint(0,100))
        
        return render_template('algo_page.html', tree=tree)
    
    return app

