from flask import Flask
import pathlib
app = Flask(__name__)
import sys

@app.route("/")
def hello():
    print("Access to test folder detected!")
    return "Hello from Python!"

@app.route("/teste")
def hello2():
    print("Access to test folder detected!")
    print("blablabla Chuck", file=sys.stderr)
    print(str(pathlib.Path().absolute()), file=sys.stderr)
    return "Hello from Chuck!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
