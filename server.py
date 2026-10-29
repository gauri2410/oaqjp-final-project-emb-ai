"""Flask web server for the emotion detection application."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze", "").strip()
    if not text:
        return jsonify({"error": "Please provide text to analyze."}), 400
    result = emotion_detector(text)
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Emotion service could not analyze the input."}), 502
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
