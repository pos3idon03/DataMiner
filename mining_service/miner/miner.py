from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# Database connection
client = MongoClient(os.getenv('DATABASE_URL'))
db = client.get_default_database()

@app.route('/mine', methods=['GET'])
def mine():
    # Your mining logic here
    return {"message": "Mining completed!"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

