from flask import Flask, request, jsonify
import requests
import subprocess

# app = Flask(__name__)

# @app.route('/run-git-log', methods=['GET'])
# def run_git_log():
#     repo_path = requests.args.get('repo_path')
#     if repo_path is not None:
#         try:
#             return jsonify({"success": True, "output": repo_path}), 200
#         except subprocess.CalledProcessError as e:
#             return jsonify({"success": False, "error": str(e)}), 500
#     else:
#         return jsonify({"success": False, "error": "Repository path not found!"}), 404


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


