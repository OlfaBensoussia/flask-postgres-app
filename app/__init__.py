from flask import Flask
from flask_cors import CORS

from .admin.routes import admin
from .admin.routes import db as db_admin
from .api.routes import api
from .api.routes import db as db_api
from .website.routes import website


def create_app():
    app = Flask(__name__)

    UPLOAD_FOLDER = '/Documents'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    db_config = {'uri': 'postgresql://postgres:123456789@localhost/lin_flask'}
    app.config['SQLALCHEMY_DATABASE_URI'] = db_config['uri'] 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db_admin.init_app(app)
    CORS(app)
    with app.app_context():
        db_admin.create_all()
        app.register_blueprint(admin, url_prefix="/admin")
        app.register_blueprint(api, url_prefix="/api")
        app.register_blueprint(website)
    return app