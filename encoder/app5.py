from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()
    input_string = data.get('inputString', '')
    base64_string = base64.b64encode(input_string.encode('utf-8')).decode('utf-8')
    return jsonify({'base64String': base64_string})

@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    base64_string = data.get('base64String', '')
    decoded_string = base64.b64decode(base64_string).decode('utf-8')
    return jsonify({'decodedString': decoded_string})

if __name__ == '__main__':
    app.run(debug=True)
