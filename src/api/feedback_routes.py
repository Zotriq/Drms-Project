from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.feedback_repository import FeedbackRepository
from services.feedback_service import FeedbackService

db = Database()
repo = FeedbackRepository(db)
svc = FeedbackService(repo)

feedback_bp = Blueprint("feedback_bp", __name__, url_prefix="/feedbacks")

@feedback_bp.route("", methods=["GET"])
def list_feedback():
    fs = svc.list_feedback()
    return jsonify([f.__dict__ for f in fs]), 200

@feedback_bp.route("/<int:feedback_id>", methods=["GET"])
def get_feedback(feedback_id):
    try:
        f = svc.get_feedback(feedback_id)
        return jsonify(f.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@feedback_bp.route("", methods=["POST"])
def create_feedback():
    payload = request.json or {}
    try:
        new_id = svc.create_feedback(payload)
        return jsonify({"feedbackID": new_id}), 201
    except Exception as e:
        return jsonify({"error": "failed to create feedback", "detail": str(e)}), 500

@feedback_bp.route("/<int:feedback_id>", methods=["DELETE"])
def delete_feedback(feedback_id):
    try:
        svc.delete_feedback(feedback_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
