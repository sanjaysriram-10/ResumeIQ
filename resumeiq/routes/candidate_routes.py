from flask import Blueprint, request, jsonify, render_template
from resumeiq.services.candidate_service import analyze_candidate

candidate_bp = Blueprint("candidate", __name__)

@candidate_bp.route("/", methods=["GET"])
def dashboard():
    return render_template("candidate/candidate_dashboard.html")

@candidate_bp.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files["resume"]
    return jsonify(analyze_candidate(resume))
from flask import Blueprint, render_template, request, jsonify, session, redirect
from resumeiq.services.candidate_service import analyze_candidate

candidate_bp = Blueprint("candidate", __name__)
@candidate_bp.route("/", methods=["GET"])
def candidate_dashboard():
    if "user_id" not in session:
        return redirect("/login")
    if session.get("role") != "candidate":
        return redirect("/login")

    return render_template("candidate/candidate_dashboard.html")
@candidate_bp.route("/analyze", methods=["POST"])
def analyze_resume():
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    if "resume" not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400

    resume_file = request.files["resume"]

    if resume_file.filename == "":
        return jsonify({"error": "Empty file"}), 400

    result = analyze_candidate(resume_file)

    return jsonify(result)