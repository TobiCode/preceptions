import sqlite3

from flask import Flask, jsonify, request

import precepts

conn = sqlite3.connect('percept_webs.db')

app = Flask(__name__)

@app.route("/")
def hello_world():
    welcome_string = "Hello. Welcome to the webservice for the Preception App."
    return welcome_string        


#get_random_preception(conn)

if __name__ == '__main__':
    app.register_blueprint(precepts.precepts_routes)
    app.run(debug=True, port=5050)