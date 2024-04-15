from flask import Flask
from .models import *
from flask_login import LoginManager

def create_app():
    
    app = Flask(__name__)
    app.secret_key = "JANETOKOH"
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    
    db.init_app(app)
    
    
    from .views import views 
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    
    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = '/admin_login'
    login_manager.init_app(app)
    
    
    # Define user_loader callback
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(User.id))
    
    
    return app

