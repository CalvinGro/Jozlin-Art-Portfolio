from flask import Flask

def create_app():
    """
    Application Factory Function
    - Creates and configures a Flask app instance.
    - Registers blueprints for modular route management.
    """
    # Initialize Flask app
    app = Flask(__name__)

    # Set a secure key for session management
    app.config['SECRET_KEY'] = 'wreoigerwoigiufdpoifjfdewrpoijro cxmvewfiwoiefpo'

    from .views import views

    # Import and register blueprints
    app.register_blueprint(views, url_prefix='/')
    return app 