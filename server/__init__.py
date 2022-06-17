from flask import (
    abort, 
    jsonify,
    Flask, 
    request
)
from flask_cors import CORS

from models import setup_db

def create_app(test_config=None):
    app=Flask(__name__)
    setup_db(app)
    CORS(app, origins=['http://127.0.0.1:5001'], max_age=10)

    # request handler
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    # endpoints
    @app.route('/')
    def home():
        return "HelloWorld!"

    # error handler
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 404,
            'message': 'resource not found'
        }), 404

    return app