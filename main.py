from flask import Flask, request, jsonify
from loguru import logger
app = Flask(__name__)

@app.route("/json", methods=["POST"])
def index():
    logger.info("-----------------------")
    logger.info("%s\n%s" % (request.path, request.headers))
    logger.info(request.json)
    return jsonify({});
if __name__ == '__main__':
    app.run(debug=True)