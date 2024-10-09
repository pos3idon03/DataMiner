from flask import Flask, jsonify, request
from github import integrate_github 
from gitlab import integrate_gitlab
import logging
import os
import requests



app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@app.route('/integrate', methods=['GET'])
def integrate():
    # Get the 'link' query parameter from the request
    link = request.args.get('link')
    logger.info(f"Got the link for call: {link}")
    if link:
        if "github.com" in link:
            repo_path = integrate_github.clone_repo(link)
            logger.info({f"{repo_path}"})
            logger.info(f"Clone of github repo {link} done")
            return {"message": f"Integration successful with github: {link}"}
        elif "gitlab.com" in link:
            integrate_gitlab.clone_repo(link)
            logger.info(f"Clone of gitlab repo {link} done")
            return {"message": f"Integration successful with gitlab: {link}"}
        else:
            return jsonify({"error" : "Invalid link! Please provide a valid github or gitlab URL."}), 400
    else:
        return jsonify({"error": "No link provided!"}), 400

@app.route('/logfile', methods=['GET'])
def logfile():
    system_name = request.args.get('system')
    if system_name:
        exists = integrate_github.check_for_system(system_name)
        if exists == False:
            logger.info(f"system-exists: {exists}")
            return jsonify({"message": f"System {system_name} does not exist"}), 200
        if exists == True:
            log_file = f"./github/logs/{system_name}/{system_name}.log"
            with open(log_file, 'r', encoding='utf-16', errors='ignore') as file:
                log_data = file.read()
                logger.info(f"log file sent")
                return jsonify({"log_data": log_data})
    else:
        return jsonify({"error": "No system provided!"}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
