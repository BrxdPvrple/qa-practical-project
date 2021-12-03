from flask import Flask, render_template
import requests


app = Flask(__name__)



@app.route('/')
def home():
    genre = requests.get('http://genres:5001/genre')
    instrument = requests.get('http://instruments:5002/instrument')
    results = {'genre': genre.text, 'instrument': instrument.text}
    video = requests.post('http://backend:5003/video', json=results)

    return render_template('index.html', genre=genre.text, instrument=instrument.text, video=video.text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)