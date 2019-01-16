from flask import current_app, send_file, request, abort, jsonify
import os
from app import app


@app.route("/")
@app.route("/index")
def index():
    dist_dir = current_app.config["DIST_DIR"]
    entry = os.path.join(dist_dir, "index.html")
    return send_file(entry)


@app.route("/api/recognize/", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        print(f.name)

        file_path = os.path.join("data", f.name)
        f.save(f"{file_path}.wav")

        return jsonify({"msg": "hello"}), 201

    abort(405)
