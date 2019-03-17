from flask import Flask

from app import create_app
from config import DEBUG

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])