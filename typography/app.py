import json
import io
from flask import send_file
from flask import Flask, render_template, request, jsonify
from analyzer import analyze_website

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/extract")
def extract():
    return render_template("extract.html")


@app.route("/classify")
def classify():
    return render_template("classify.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    url = data.get("website")

    if not url:
        return jsonify({"error": "URL missing"}), 400

    result = analyze_website(url)

    return jsonify(result)

@app.route("/download", methods=["POST"])
def download_report():

    data=request.get_json()
    url=data.get("website")

    result=analyze_website(url)

    file_data=json.dumps(result,indent=4)

    return send_file(
        io.BytesIO(file_data.encode()),
        mimetype="application/json",
        as_attachment=True,
        download_name="css_analysis_report.json"
    )

if __name__ == "__main__":
    app.run(debug=True)