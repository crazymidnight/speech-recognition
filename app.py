from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1>Welcome to my web page</h1>"
