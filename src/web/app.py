from flask import Flask, render_template, request, jsonify
from pathlib import Path
import sys

# Add parent directory to path to import hash_analyzer
sys.path.append(str(Path(__file__).parent.parent))
from hash_analysis.hash_analyzer import compute_hash, compute_hash_with_salt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hash', methods=['POST'])
def hash_password():
    data = request.get_json()
    password = data.get('password')
    algorithm = data.get('algorithm', 'md5')
    salt = data.get('salt')

    if not password:
        return jsonify({'error': 'Parola gerekli'}), 400

    try:
        if salt:
            result = compute_hash_with_salt(password, salt, algorithm)
        else:
            result = compute_hash(password, algorithm)
        
        return jsonify({
            'password': password,
            'salt': salt,
            'algorithm': algorithm,
            'hash': result
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/analyze', methods=['POST'])
def analyze_hash():
    data = request.get_json()
    hash_value = data.get('hash')
    algorithm = data.get('algorithm')

    if not hash_value:
        return jsonify({'error': 'Hash değeri gerekli'}), 400

    # TODO: Hash analizi özelliklerini ekle
    return jsonify({
        'message': 'Hash analizi özelliği henüz eklenmedi',
        'hash': hash_value,
        'algorithm': algorithm
    })

if __name__ == '__main__':
    app.run(debug=True) 