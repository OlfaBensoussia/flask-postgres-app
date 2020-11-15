from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .admin.routes import admin
from .api.routes import api
from .website.routes import website
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    UPLOAD_FOLDER = '/Documents'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    db_config = {'uri': 'postgresql://postgres:123456789@localhost/lin_flask'}
    app.config['SQLALCHEMY_DATABASE_URI'] = db_config['uri'] 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db = SQLAlchemy(app)
    CORS(app)
    with app.app_context():
        app.register_blueprint(admin, url_prefix="/admin")
        app.register_blueprint(api, url_prefix="/api")
        app.register_blueprint(website)
    return app