from flask import Flask, request, Response, render_template_string

app = Flask(__name__)

# Main application route
@app.route('/')
def home():
    return "Hello from App 2!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
