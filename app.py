from flask import Flask

from services import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def hello_world():
    emotion_detector(req)