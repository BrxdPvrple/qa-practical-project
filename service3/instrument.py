import random
from flask import Flask, Response


app = Flask(__name__)

@app.route("/instrument", methods=["GET"])
def instrument():
    instruments = ['Guitar', 'Piano', 'Saxophone', 'Violin']
    choice = random.choice(instruments)
    return Response(choice, mimetype="text/plain")


if __name__ == "__main__":  #pragma: no cover
    app.run(host="0.0.0.0", port=5002, debug=True)