from flask import Flask
from flask_httpauth import HTTPBasicAuth
import config

auth = HTTPBasicAuth()
app = Flask(__name__)

@auth.get_password
def get_pw(username):
    if username in config.user:
        return config.user.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return config.flag

if __name__ == '__main__':
    app.run()
