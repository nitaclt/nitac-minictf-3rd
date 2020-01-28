from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


users = [
    User(1, 'piyo', 'you_must_watch_sb69'),
    User(2, 'appp', 'chikara_is_power'),
    User(3, 'hoge', 'verification_code_is_admin_access_token'),
    User(4, 'chhtd', "Let's_access_distination_IP_address"),
    User(5, 'admin', 'qwerty')
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super_secret'

jwt = JWT(app, authenticate, identity)


@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity.id


if __name__ == '__main__':
    app.run()
