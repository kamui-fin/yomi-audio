from flask import Flask, request, send_file
from pathlib import Path

AUDIO_DIR = Path(__file__).parent / "audio"
SOURCES = sorted(AUDIO_DIR.iterdir())

def search(term):
    # return a path to audio file
    for source in SOURCES:
        term_file = source / f"{term}.mp3" 
        if term_file.is_file():
            return str(term_file)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_audio():
    return send_file(search(request.args["expression"]))

if __name__ == '__main__':
    app.run()
