from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    A sample endpoint that returns a greeting.
    ---
    responses:
      200:
        description: A greeting message
        schema:
          type: object
          properties:
            message:
              type: string
    """
    return jsonify({"message": "Hello, world!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
