from flask import Flask, jsonify, request
from github import integrate_github
from gitlab import integrate_gitlab

app = Flask(__name__)

@app.route('/integrate', methods=['GET'])
def integrate():
    # Get the 'link' query parameter from the request
    link = request.args.get('link')

    if link:
        if "github" in link:
            integrate_github.clone_repo(link)
            return jsonify({"message": f"Integration successful with github: {link}"})
        elif "gitlab" in link:
            integrate_gitlab.clone_repo(link)
            return jsonify({"message": f"Integration successful with gitlab: {link}"})
        else:
            return jsonify({"error": "Invalid link! Please provide a valid github or gitlab URL."}), 400
    else:
        return jsonify({"error": "No link provided!"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
