from flask import Flask, request, jsonify, send_file
from encryption import encrypt_file, decrypt_file

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('temp_file')
    encrypt_file('temp_file', 'encrypted_file')
    # Upload 'encrypted_file' to cloud storage
    return jsonify({"message": "File uploaded and encrypted successfully."})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Download 'encrypted_file' from cloud storage
    decrypt_file('encrypted_file', 'decrypted_file')
    return send_file('decrypted_file', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
