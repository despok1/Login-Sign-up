from flask import Flask, request, redirect
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests

secret_key = "secre.tt_26"

app = Flask(__name__)
CORS(app)

app.secret_key = secret_key
CLIENT_ID = "360444884335-299hul0pnn7g3c5f92kg63r77jk3k0ug.apps.googleusercontent.com"


@app.route("/", methods=["GET"])
def home():
    return "This is EXPAND Platform API!"

@app.route("/google_login", methods=["POST"])
def get_user():
    print(request.form.get("credential"))
    get_user_data(request.form.get("credential"))
    return "123"

def get_user_data(token: str):
    try:
        print("try working...")

        id_info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        print("🐍 idinfo", id_info)

        user_data = {
            "name": id_info["name"],
            "email": id_info["email"],
            "picture": id_info["picture"],
            "given_name": id_info["given_name"],
            "family_name": id_info["family_name"],
        }

        print("🐍 userData: ", user_data)

        return user_data

    except Exception as error:
        print("failed get user data, error: ", error)
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
