from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! from Flask"

@app.route('/dashboard')
def dashboard():
    return "<h1>Dashboard</h1><p>This is a simple dashboard page.</p>"

if __name__ == "__main__":
    app.run(debug=True)