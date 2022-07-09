from flask import Flask
from sqlalchemy import create_engine, insert, text

app = Flask(__name__)

@app.route("/", methods=["GET"])
def starting_url():
    json_data = flask.request.json
    a_value = json_data["a_key"]
    return "JSON value sent: " + a_value

app.run(host="0.0.0.0", port=8080)