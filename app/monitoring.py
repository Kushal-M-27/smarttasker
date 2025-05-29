from flask import Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

def setup_monitoring(app):
    @app.before_request
    def before_request():
        REQUEST_COUNT.inc()

    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
