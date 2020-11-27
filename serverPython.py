from flask import Flask
app = Flask(__name__)
import sys

@app.route("/")
def hello():
    print("Access to test folder detected!")
    return "Hello from Python!"

@app.route("/teste")
def hello2():
    print("Access to test folder detected!")
    print("blabla Chuck", file=sys.stderr)
    return "Hello from Chuck!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
