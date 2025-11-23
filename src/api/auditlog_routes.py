from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.auditlog_repository import AuditLogRepository
from services.auditlog_service import AuditLogService

db = Database()
repo = AuditLogRepository(db)
svc = AuditLogService(repo)

auditlog_bp = Blueprint("auditlog_bp", __name__, url_prefix="/auditlogs")

@auditlog_bp.route("", methods=["GET"])
def list_logs():
    logs = svc.list_logs()
    return jsonify([l.__dict__ for l in logs]), 200

@auditlog_bp.route("", methods=["POST"])
def create_log():
    payload = request.json or {}
    try:
        new_id = svc.create_log(payload)
        return jsonify({"logID": new_id}), 201
    except Exception as e:
        return jsonify({"error": "failed to create audit log", "detail": str(e)}), 500
