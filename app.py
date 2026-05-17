from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    # මේකෙන් අපිට බලාගන්න පුළුවන් App එක දුවන Server එකේ විස්තර
    server_info = os.environ.get('COMPUTERNAME', 'Linux Container')
    return f"<h1>Hello from KloudSchool Deep Dive!</h1><p>Running on: {server_info}</p>"

if __name__ == "__main__":
    app.run()