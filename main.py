from flask import Flask, jsonify

app = Flask(__name__)

# Link ka custom route: /pub/rupamlive/api
@app.route('/pub/rupamlive/api', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "creator": "Rupam",
        "message": "Welcome to Rupam's Official API!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
