from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def get_location():
    data = request.json or {}
    ip = request.remote_addr
    ip_info = requests.get(f'http://ip-api.com/json/{ip}').json()
    print("Browser GPS:", data)
    print("IP location fallback:", ip_info)
    return jsonify({"status": "received"})

if __name__ == '__main__':
    app.run()
