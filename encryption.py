from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
import os

# Initialize the Flask app
app = Flask(__name__)

# Configuration for file uploads
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'your_secret_key'

# Generate a key (only do this once and store it securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Create uploads folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def encrypt_file(filepath):
    """Encrypt the file at the specified path."""
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """Handle file uploads and encrypt the uploaded file."""
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            encrypt_file(filepath)
            return redirect(url_for('index'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
