from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/json", methods=["POST"])
def index():
    print("-----------------------\n%s\n%s%s" % (request.path, request.headers, request.json))
    return jsonify({});
if __name__ == '__main__':
    app.run(debug=True)