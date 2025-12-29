from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 DevOps Portfolio: Flask App with CI/CD Pipeline!"

@app.route('/health')
def health():
    return "✅ Healthy", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
