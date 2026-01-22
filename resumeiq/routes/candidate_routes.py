"""
Candidate routes - handles all candidate-related endpoints
"""

from flask import Blueprint, render_template, request, jsonify
from services.candidate_service import CandidateService

candidate_bp = Blueprint('candidate', __name__, url_prefix='/candidate')
candidate_service = CandidateService()

@candidate_bp.route('/dashboard', methods=['GET'])
def candidate_dashboard():
    """Display candidate dashboard"""
    return render_template('candidate/candidate_dashboard.html')

@candidate_bp.route('/analyze', methods=['POST'])
def analyze_resume():
    """Analyze uploaded resume"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    result = candidate_service.analyze_resume(file)
    return jsonify(result)
