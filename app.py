from flask import Flask
from routes import register_routes
from utils import load_environment_variables

# Load environment variables from .env file
load_environment_variables()

app = Flask(__name__)

# Register routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)

"""
app.py
---------
This file initializes the Flask application, loads environment variables, and registers routes.
It starts the server when run directly.

Functions:
- load_environment_variables(): Load environment variables from the .env file.
- register_routes(app): Register API routes for the Flask app.

Configuration:
- The Flask application is configured to run in debug mode for development purposes.
"""
