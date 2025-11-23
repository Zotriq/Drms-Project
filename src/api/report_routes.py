from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.report_repository import ReportRepository
from services.report_service import ReportService

db = Database()
repo = ReportRepository(db)
svc = ReportService(repo)

report_bp = Blueprint("report_bp", __name__, url_prefix="/reports")

@report_bp.route("", methods=["GET"])
def list_reports():
    rs = svc.list_reports()
    return jsonify([r.__dict__ for r in rs]), 200

@report_bp.route("/<int:report_id>", methods=["GET"])
def get_report(report_id):
    try:
        r = svc.get_report(report_id)
        return jsonify(r.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@report_bp.route("", methods=["POST"])
def create_report():
    payload = request.json or {}
    try:
        new_id = svc.create_report(payload)
        return jsonify({"reportID": new_id}), 201
    except Exception as e:
        return jsonify({"error": "failed to create report", "detail": str(e)}), 500

@report_bp.route("/<int:report_id>", methods=["DELETE"])
def delete_report(report_id):
    try:
        svc.delete_report(report_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
