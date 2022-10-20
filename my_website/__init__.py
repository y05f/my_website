import os

from flask import Flask, render_template, redirect
from flask import make_response
from io import BytesIO



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/projects')
    def get_projects():
        return render_template('/projects.html')
    
    @app.route('/resume')
    def get_resume():
        with open('./my_website/static/resume.pdf','rb') as pdf_file:
            binary_pdf = BytesIO(pdf_file.read())
            response = make_response(binary_pdf)
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = \
                'inline; filename=%s.pdf' % 'safi_resume'
            return response
        
    return app