from flask import Flask, render_template, request, send_file
import pydicom
import numpy as np

app = Flask(__name__)

def logistic_map(x, r, n):
    """
    Logistic map function for generating pseudo-random numbers.
    """
    result = []
    for _ in range(n):
        x = r * x * (1 - x)
        result.append(x)
    return result

def encrypt_image(pixel_data, key):
    """
    Encrypt binary pixel data using XOR operation with a logistic map key.
    """
    key_stream = np.array(logistic_map(0.5, key, len(pixel_data)))
    encrypted_data = np.bitwise_xor(pixel_data.astype(np.uint16), (key_stream * 65535).astype(np.uint16))
    return encrypted_data

def decrypt_image(encrypted_data, key):
    """
    Decrypt binary pixel data using XOR operation with a logistic map key.
    """
    key_stream = np.array(logistic_map(0.5, key, len(encrypted_data)))
    decrypted_data = np.bitwise_xor(encrypted_data.astype(np.uint16), (key_stream * 65535).astype(np.uint16))
    return decrypted_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Check if the user uploaded a DICOM file for encryption
            if 'dicom_file_encrypt' in request.files:
                # Get the DICOM file for encryption from the HTML form
                dicom_file_encrypt = request.files['dicom_file_encrypt']
                # Read the DICOM file
                dicom_data_encrypt = pydicom.dcmread(dicom_file_encrypt)

                # Get the pixel data as binary
                pixel_data_encrypt = dicom_data_encrypt.pixel_array.flatten()

                # Get the encryption key from the HTML form
                encryption_key = float(request.form['encryption_key'])

                # Encrypt the pixel data
                encrypted_data = encrypt_image(pixel_data_encrypt, encryption_key)

                # Save the encrypted image
                dicom_data_encrypt.PixelData = encrypted_data.astype(np.uint16).tobytes()
                dicom_data_encrypt.save_as('encrypted_dicom.dcm')

                return render_template('index.html', message_encrypt="Encryption successful! You can now download the encrypted file.")
                
            # Check if the user uploaded a DICOM file for decryption
            if 'dicom_file_decrypt' in request.files:
                # Get the DICOM file for decryption from the HTML form
                dicom_file_decrypt = request.files['dicom_file_decrypt']
                # Read the DICOM file
                dicom_data_decrypt = pydicom.dcmread(dicom_file_decrypt)

                # Get the pixel data as binary
                pixel_data_decrypt = dicom_data_decrypt.pixel_array.flatten()

                # Get the decryption key from the HTML form
                decryption_key = float(request.form['decryption_key'])

                # Decrypt the pixel data
                decrypted_data = decrypt_image(pixel_data_decrypt, decryption_key)

                # Save the decrypted image
                dicom_data_decrypt.PixelData = decrypted_data.astype(np.uint16).tobytes()
                dicom_data_decrypt.save_as('decrypted_dicom.dcm')

                return render_template('index.html', message_decrypt="Decryption successful! You can now download the decrypted file.")

        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
