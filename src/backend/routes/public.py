from flask import Blueprint, jsonify
from middleman.logger import logger

public_bp = Blueprint("public_bp", __name__)

@public_bp.route("/ping", methods=["GET"])
def ping():
    """
    Example public endpoint: returns "pong".
    """
    logger.info("Public /ping endpoint was called.")
    return jsonify({"message": "pong"}), 200
