from flask import Flask, jsonify, request
from flask_cors import CORS  # Allow CORS for all domains
import requests

app = Flask(__name__)
CORS(app)  
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        url = "https://datasets-server.huggingface.co/rows"
        params = {
            'dataset': 'LDJnr/Puffin',
            'config': 'default',
            'split': 'train',
            'offset': 0,
            'length': 100
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Return JSON response to the client
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
