import time
import logging
from flask import request, g

logger = logging.getLogger("SyntaxSentinel")  

def register_logger_middleware(app):
    """
    Registers 'before_request' and 'after_request' hooks on the Flask app
    to log request start and completion, including response time.
    """

    @app.before_request
    def log_request_start():
        g.start_time = time.time()
        logger.info(f"Started {request.method} {request.path}")

    @app.after_request
    def log_request_end(response):
        start_time = getattr(g, 'start_time', time.time())
        duration = (time.time() - start_time) * 1000  # ms
        status_code = response.status_code
        logger.info(f"Completed {request.method} {request.path} {status_code} in {duration:.2f}ms")
        return response
