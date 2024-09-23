from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/integrate', methods=['GET'])
def integrate():
    return jsonify({"message": "Integration successful!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
