from flask import Flask, request
import config

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def auth_flag():
    if request.method == "GET":
        return """
        <form action="/" method="POST">
        username
        <input name="username"></input><br>
        password
        <input name="password"></input><br>
        verification code
        <input name="verification_code"></input><br>
        <input type="submit">
        </form>
        """
    else:
        if str(request.form["username"]) == config.username and str(request.form["password"]) == config.password and str(request.form["verification_code"]) == config.verification_code:
            return """{}""".format(config.flag)
        else:
            return """Invalid credentials."""


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
