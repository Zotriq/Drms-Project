from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.shelter_repository import ShelterRepository
from services.shelter_service import ShelterService

db = Database()
repo = ShelterRepository(db)
svc = ShelterService(repo)

shelter_bp = Blueprint("shelter_bp", __name__, url_prefix="/shelters")

@shelter_bp.route("", methods=["GET"])
def list_shelters():
    ss = svc.list_shelters()
    return jsonify([s.__dict__ for s in ss]), 200

@shelter_bp.route("/<int:shelter_id>", methods=["GET"])
def get_shelter(shelter_id):
    try:
        s = svc.get_shelter(shelter_id)
        return jsonify(s.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@shelter_bp.route("", methods=["POST"])
def create_shelter():
    payload = request.json or {}
    try:
        new_id = svc.create_shelter(payload)
        return jsonify({"shelterID": new_id}), 201
    except Exception as e:
        return jsonify({"error": "failed to create shelter", "detail": str(e)}), 500

@shelter_bp.route("/<int:shelter_id>", methods=["PUT"])
def update_shelter(shelter_id):
    payload = request.json or {}
    try:
        svc.update_shelter(shelter_id, payload)
        return jsonify({"status": "updated"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@shelter_bp.route("/<int:shelter_id>", methods=["DELETE"])
def delete_shelter(shelter_id):
    try:
        svc.delete_shelter(shelter_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
