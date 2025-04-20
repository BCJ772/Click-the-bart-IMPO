from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
FILE = "clicks.txt"

def get_clicks():
    with open(FILE, "r") as f:
        return int(f.read())

def save_clicks(count):
    with open(FILE, "w") as f:
        f.write(str(count))

@app.route("/")
def home():
    clicks = get_clicks()
    return render_template("index.html", clicks=clicks)

@app.route("/click", methods=["POST"])
def click():
    clicks = get_clicks() + 1
    save_clicks(clicks)
    return jsonify({"clicks": clicks})

if __name__ == "__main__":
    app.run(debug=True)
