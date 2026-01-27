from flask import Flask
import os
from resumeiq.routes.auth_routes import auth_bp
from resumeiq.routes.candidate_routes import candidate_bp
from resumeiq.routes.recruiter_routes import recruiter_bp
from resumeiq.routes.profile_routes import profile_bp
from resumeiq.routes.home_routes import home_bp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "templates")
)

app.secret_key = "resumeiq_secret_key"

app.register_blueprint(auth_bp)
app.register_blueprint(candidate_bp, url_prefix="/candidate")
app.register_blueprint(recruiter_bp, url_prefix="/recruiter")
app.register_blueprint(profile_bp)
app.register_blueprint(home_bp)
print(app.url_map)

if __name__ == "__main__":
    app.run()
