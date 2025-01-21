import os
from flask import Flask, send_from_directory, jsonify
from dotenv import load_dotenv
import logging

# Import Blueprints
from routes.public import public_bp
from routes.private import private_bp

# Import custom exceptions
from errors.exceptions import (
    BaseAppException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    HttpRequestException
)
from errors.error_content import ErrorContent

# import middleman
from middleman.auth0 import AuthError
from middleman.logger import register_logger_middleware

# import constants
from constants.env_variables import (
    Auth0Config,
    AppConfig
)

# Load environment variables from .env
load_dotenv()

def create_app():
    app = Flask(AppConfig.APP_NAME)
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.setLevel(logging.ERROR)
    # Configure logging however you'd like
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    # Register the middleware hooks
    register_logger_middleware(app)

    # Register routes
    app.register_blueprint(public_bp, url_prefix="/api")
    app.register_blueprint(private_bp, url_prefix="/api")

    @app.errorhandler(BaseAppException)
    def handle_custom_exceptions(e):
        error_content = ErrorContent.from_exception(e)
        response_body = error_content.get_details()
        return jsonify(response_body), e.status

    @app.errorhandler(AuthError)
    def handle_auth_error(e):
        error_content = ErrorContent(
            status=401,
            code="NO_AUTH_TOKEN",
            message=str(e),
            details={}
        )
        return jsonify(error_content.get_summary()), 500


    @app.errorhandler(404)
    def not_found(e):
        error_content = ErrorContent(
            status=404,
            code="NOT_FOUND",
            message=str(e),
            details={}
        )
        return jsonify(error_content.get_summary()), 404


    @app.errorhandler(Exception)
    def handle_unexpected_exceptions(e):
        error_content = ErrorContent(
            status=500,
            code="UNCAUGHT_EXCEPTION",
            message=str(e),
            details={}
        )
        return jsonify(error_content.get_summary()), 500

    return app

    # Serve a basic index.html if you want to show a landing page
    @app.route("/")
    def index():
        return send_from_directory("public", "index.html")  # if you have a /public folder
    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
