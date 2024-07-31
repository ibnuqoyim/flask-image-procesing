from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'instance/uploads'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

    from . import routes
    app.register_blueprint(routes.bp)
    return app