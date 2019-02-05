import os
from app.api.app import create_app

app = create_app("development")


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)
