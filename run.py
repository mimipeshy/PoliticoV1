import os
from app.api.app import create_app
from flask import make_response, jsonify

app = create_app("development")


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.errorhandler(404)
def error404(e):
    return make_response(jsonify({"Status": 404,
                                  "Data": "Not Found".format(e)}), 404)


@app.errorhandler(403)
def error404(e):
    return make_response(jsonify({"Status": 403,
                                  "Data": "Forbidden".format(e)}), 403)


@app.errorhandler(500)
def error404(e):
    return make_response(jsonify({"Status": 500,
                                  "Data": "Internal Server Error".format(e)}), 500)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run()
