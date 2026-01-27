import os
import uuid
from flask import Blueprint, render_template, request, jsonify
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

    resume_items = []

    for file in files:
        if not file.filename:
            continue

        original_name = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex}_{original_name}"
        save_path = os.path.join(UPLOAD_FOLDER, unique_name)
        file.save(save_path)

        resume_items.append({
            "file": file,
            "stored_name": unique_name,
            "original_name": original_name
        })

    results = analyze_resumes(resume_items, jd_text)
    return jsonify(results)