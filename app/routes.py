from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    return """
    <h1>Coming soon.</h1>
    <hr>
    <div><a href="https://github.com/crazymidnight/speech-recognition">
    Visit project github page.</div>
    """
