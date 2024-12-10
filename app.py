from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health_check():
    return 'OK', 200  # A simple response indicating the app is healthy

if __name__ == '__main__':
    app.run(debug=True)
