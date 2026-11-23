from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(message="Hello from Flask API!")

@app.get("/about")
def about():
    return jsonify(message="This is a simple Flask API")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
