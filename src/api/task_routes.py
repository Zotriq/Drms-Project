from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.task_repository import TaskRepository
from services.task_service import TaskService

db = Database()
repo = TaskRepository(db)
svc = TaskService(repo)

task_bp = Blueprint("task_bp", __name__, url_prefix="/tasks")

@task_bp.route("", methods=["GET"])
def list_tasks():
    ts = svc.list_tasks()
    return jsonify([t.__dict__ for t in ts]), 200

@task_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    try:
        t = svc.get_task(task_id)
        return jsonify(t.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@task_bp.route("", methods=["POST"])
def create_task():
    payload = request.json or {}
    try:
        new_id = svc.create_task(payload)
        return jsonify({"taskID": new_id}), 201
    except Exception as e:
        return jsonify({"error": "failed to create task", "detail": str(e)}), 500

@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    payload = request.json or {}
    try:
        svc.update_task(task_id, payload)
        return jsonify({"status": "updated"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        svc.delete_task(task_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
