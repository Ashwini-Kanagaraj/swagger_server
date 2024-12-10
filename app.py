from flask import Flask
app = Flask(__name__)

@app.route('/health')
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  # This will make the app accessible from external IPs
