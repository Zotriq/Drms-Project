from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.notification_repository import NotificationRepository
from services.notification_service import NotificationService

db = Database()
repo = NotificationRepository(db)
svc = NotificationService(repo)

notification_bp = Blueprint("notification_bp", __name__, url_prefix="/notifications")

@notification_bp.route("", methods=["GET"])
def list_notifications():
    ns = svc.list_notifications()
    return jsonify([n.__dict__ for n in ns]), 200

@notification_bp.route("/<int:notification_id>", methods=["GET"])
def get_notification(notification_id):
    try:
        n = svc.get_notification(notification_id)
        return jsonify(n.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@notification_bp.route("", methods=["POST"])
def create_notification():
    payload = request.json or {}
    try:
        new_id = svc.create_notification(payload)
        return jsonify({"notificationID": new_id}), 201
    except Exception as e:
        return jsonify({"error": "failed to create notification", "detail": str(e)}), 500

@notification_bp.route("/<int:notification_id>", methods=["PUT"])
def update_notification(notification_id):
    payload = request.json or {}
    try:
        svc.update_notification(notification_id, payload)
        return jsonify({"status": "updated"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@notification_bp.route("/<int:notification_id>", methods=["DELETE"])
def delete_notification(notification_id):
    try:
        svc.delete_notification(notification_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
