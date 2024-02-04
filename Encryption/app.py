from flask import Flask, render_template, request, jsonify
from encrypt import encrypt_data, decrypt_data

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    input_data = data['data']
    encryption_key = float(data['key'])

    # Call the encrypt function (implement this function)
    encrypted_data = encrypt_data(input_data, encryption_key)
    
    return jsonify({'encryptedData': encrypted_data})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    encrypted_data = data['data']
    decryption_key = float(data['key'])

    # Call the decrypt function (implement this function)
    decrypted_data = decrypt_data(encrypted_data, decryption_key)
    
    return jsonify({'decryptedData': decrypted_data})

if __name__ == '__main__':
    app.run(debug=True)
