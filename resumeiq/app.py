"""
ResumeIQ - ATS Resume Analyzer Application
Main application entry point
"""

from flask import Flask
from config import Config

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    from routes.candidate_routes import candidate_bp
    app.register_blueprint(candidate_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
