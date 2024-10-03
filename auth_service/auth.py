from flask import Flask
# import mysql.connector

app = Flask(__name__)

# Database connection
# db_config = {
#     'user': 'youruser',
#     'password': 'yourpassword',
#     'host': 'mysql',
#     'database': 'auth_db'
# }
# conn = mysql.connector.connect(**db_config)

@app.route('/login', methods=['POST'])
def login():
    """ Your login logic here """

    return {"message": "Login successful!"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)