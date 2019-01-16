from flask import current_app, send_file, render_template
import os
from app import app


@app.route("/")
@app.route("/index")
def index():
    dist_dir = current_app.config["DIST_DIR"]
    entry = os.path.join(dist_dir, "index.html")
    return send_file(entry)
