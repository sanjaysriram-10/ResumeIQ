from flask import Blueprint, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from resumeiq.services.recruiter_service import analyze_resumes

recruiter_bp = Blueprint("recruiter", __name__)

UPLOAD_FOLDER = "resumeiq/static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@recruiter_bp.route("/")
def recruiter_dashboard():
    return render_template("recruiter/recruiter_dashboard.html")


@recruiter_bp.route("/analyze", methods=["POST"])
def analyze_candidates():
    jd_text = request.form.get("job_description")
    files = request.files.getlist("resumes")

    saved_files = []
    for file in files:
        filename = secure_filename(file.filename)
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(save_path)
        saved_files.append(file)

    results = analyze_resumes(saved_files, jd_text)
    return jsonify(results)