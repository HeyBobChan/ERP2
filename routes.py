from flask import request, jsonify
from schema_extractor import extract_schema
from query_generator import generate_query
from query_executor import execute_query
from file_handler import handle_file_upload
from error_handler import handle_error

def register_routes(app):
    @app.route('/extract_schema', methods=['GET'])
    def extract_schema_route():
        try:
            schema = extract_schema()
            return jsonify(schema)
        except Exception as e:
            return handle_error(e)

    @app.route('/query', methods=['POST'])
    def query_route():
        try:
            data = request.get_json()
            user_question = data['question']
            sql_query = generate_query(user_question)
            results = execute_query(sql_query)
            return jsonify(results)
        except Exception as e:
            return handle_error(e)

    @app.route('/onboard', methods=['POST'])
    def onboard_route():
        try:
            human_readable_dict = request.get_json()
            save_dictionary(human_readable_dict)
            return jsonify({"status": "success"}), 200
        except Exception as e:
            return handle_error(e)

    @app.route('/upload', methods=['POST'])
    def upload_route():
        try:
            file = request.files['file']
            handle_file_upload(file)
            return jsonify({"status": "success"}), 200
        except Exception as e:
            return handle_error(e)

"""
routes.py
---------
Defines the routes for the Flask application.

Functions:
- register_routes(app): Registers the '/extract_schema', '/query', '/onboard', and '/upload' routes for the Flask app.
- extract_schema_route(): Handles GET requests for extracting the database schema.
- query_route(): Handles POST requests for generating and executing SQL queries based on user questions.
- onboard_route(): Handles POST requests for schema onboarding.
- upload_route(): Handles POST requests for file uploads.
"""
