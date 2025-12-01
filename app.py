from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "<h1>Hello from GitLab CI + Docker!</h1><p>This web app is served from a container.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
