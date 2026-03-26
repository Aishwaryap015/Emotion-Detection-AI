from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text = request.form.get("text")

    if not text:
        return jsonify({"error": "No input"})

    result = emotion_detector(text)

    print("RESULT:", result)  # 🔥 DEBUG

    if result is None:
        return jsonify({"error": "API failed"})

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)