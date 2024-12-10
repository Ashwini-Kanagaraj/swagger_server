from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    A simple hello world endpoint.
    ---
    responses:
      200:
        description: A successful response
    """
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
