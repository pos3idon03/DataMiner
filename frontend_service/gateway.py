from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Frontend Service!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
