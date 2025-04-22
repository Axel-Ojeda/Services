from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/length", methods=["POST"])
def get_length():
    data = request.get_json()
    text = data.get("text", "")
    return jsonify({"length": len(text)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
