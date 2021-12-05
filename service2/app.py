import random
from flask import Flask, Response


app = Flask(__name__)

@app.route('/genre', methods=['GET'])
def genre():
    genres = ['Classical', 'R&B', 'Jazz', 'Blues', 'Reggae']
    choice = random.choice(genres)
    return Response(choice, mimetype='text/plain')



if __name__ == "__main__":     #pragma: no cover
    app.run(host="0.0.0.0", port=5001, debug=True)
