from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def get_location():
    data = request.json
    print("Received location:", data)
    return jsonify({"status": "received"})

if __name__ == '__main__':
    app.run()
