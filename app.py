from flask import Flask, send_from_directory

app = Flask(__name__)

# Route to serve Swagger UI
@app.route('/swagger-ui')
def swagger_ui():
    return send_from_directory('static', 'swagger-ui.html')

# Route for the API
@app.route('/api')
def api():
    return "API is up!"

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
