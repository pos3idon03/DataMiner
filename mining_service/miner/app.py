import os
from flask import Flask, request, jsonify
import requests
import subprocess
import logging
# from pymongo import MongoClient


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Database connection
# client = MongoClient(os.getenv('DATABASE_URL'))
# db = client.get_default_database()

@app.route('/mine', methods=['GET'])
def mine():
    """  Mine a new block """
    return {"message": "Mining completed!"}

@app.route('/get-log', methods=['GET'])
def run_git_log():
    system = request.args.get('log_file')
    url = f"http://integration_service:5000/logfile?system={system}"
    try:   
        response=requests.get(url)
        response.raise_for_status()
        logger.info(f"Response is received {response} with status code {response.status_code}")
        if response.status_code == 200:
            try:
                return jsonify({"success": True, "output" : response.json()}), 200
            except subprocess.CalledProcessError as e:
                return jsonify({"success": False, "error": str(e)}), 500
        else:
            return jsonify({"success": False, "error": "Repository path not found!"}), 404
    except requests.exceptions.RequestException as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
