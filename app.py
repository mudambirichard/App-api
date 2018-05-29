from flask import Flask, jsonify
from flask import abort
app = Flask(__name__)

requests = [
    {
        'id': 1,
        'name':'Ritah Mugaga',
        'email': 'mufda@gmail.com',
        'password': '',
        
    }
]

@app.route('/api/v1.0/requests', methods=['GET'])
def get_requests( ):
    return jsonify({'requests': requests})


if __name__ == '__main__':
    app.run(debug=True)