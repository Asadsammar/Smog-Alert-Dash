from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Example predictions data
predictions_data = {
    "Lahore": {"PM2.5": [150, 180, 200], "PM10": [250, 280, 300]},
    "Faisalabad": {"PM2.5": [120, 140, 160], "PM10": [200, 230, 250]},
    "Gujranwala": {"PM2.5": [100, 110, 130], "PM10": [180, 200, 220]},
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/predictions/<city>")
def get_predictions(city):
    city_predictions = predictions_data.get(city)
    if city_predictions:
        return jsonify(city_predictions)
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
