import os
from flask import Flask, jsonify
from flask import render_template
from main import run_engine

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/run")
def run():
    try:
        result = run_engine()
        return jsonify(result)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/logs")
def logs():
    with open("app.log", "r") as f:
        content = f.read()
        return f"<pre>{content}</pre>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", 
            port=os.environ.get("PORT", 5000), debug=True) 