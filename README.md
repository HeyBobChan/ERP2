# Natural Language Interface for Priority ERP

## Overview
This project allows users to interact with their Priority ERP database using natural language queries. The system translates these queries into SQL, executes them, and returns results in a user-friendly format. The onboarding process helps map non-self-explanatory schema elements to understandable labels.

## Features
- Natural language to SQL query translation
- Database schema extraction and management
- Onboarding process for schema labeling
- File upload and processing

## Setup
1. Clone the repository.
2. Create a `.env` file with your configuration (see `.env.example`).
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the application: `python app.py`.

## API Endpoints
- **GET /extract_schema**: Extracts the database schema.
- **POST /query**: Generates and executes a SQL query from a natural language question.
- **POST /onboard**: Handles schema onboarding.
- **POST /upload**: Handles file uploads.
