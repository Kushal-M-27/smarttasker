from flask import Flask
from .routes import routes
from .monitoring import setup_monitoring   # <-- import monitoring setup

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    setup_monitoring(app)  # <-- register /metrics route and counter
    return app
