import logging

from flask import Flask
from google.cloud import datastore

datastore_client = datastore.Client.from_service_account_json('CHANGE_ME.json')

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    key = datastore_client.key('account', CHANGE_ME, namespace='CHANGE_ME')
    data = datastore_client.get(key)
    return 'Hello World!'


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
