# Basic Flask REST API with SQL-Alchemy Integration

This project demonstrates how to create a simple REST API using Python and Flask, integrated with a Flask SQL-Alchemy database. The API allows for CRUD (Create, Read, Update, Delete) operations on resources.

## Getting Started

Follow these steps to set up the project locally and run the Flask REST API:

```bash
git clone <repository-url>
cd <repository-name>

python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS and Linux:
source venv/bin/activate

pip install -r requirements.txt

python main.py

The API will be accessible at [http://localhost:5000](http://localhost:5000).

## API Endpoints

The API provides the following endpoints to interact with the resources:

- `GET /video/<int:video_id>`: Get details of a specific video by its ID.
- `POST /video/<int:video_id>`: Create a new video with the provided data.
- `PATCH /video/<int:video_id>`: Update an existing video with the provided data.
- `DELETE /video/<int:video_id>`: Delete a video by its ID.

Feel free to modify and extend this project to suit your specific requirements.
