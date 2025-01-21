from flask import Blueprint, jsonify
from middleman.auth0 import requires_auth
from middleman.logger import logger

private_bp = Blueprint("private_bp", __name__)

@private_bp.route("/", methods=["GET"], strict_slashes=False)
@requires_auth
def protected_endpoint():
    """
    Example private endpoint that requires a valid JWT.
    """
    logger.info("Private endpoint was accessed with a valid token.")
    return jsonify({"message": "This is a protected route."}), 200
