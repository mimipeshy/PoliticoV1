import os
from flask import Flask
from app import app

from config import app_config

config_name = "development"
app = app(config_name)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)