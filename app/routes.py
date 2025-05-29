from flask import Blueprint, jsonify

routes = Blueprint('routes', __name__)

@routes.route("/health")
def health():
    return jsonify({"status": "ok"})

@routes.route("/metrics")
def metrics():
    return jsonify({"uptime": "99%", "active_users": 12})
