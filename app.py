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

@app.route('/api/v1.0/requests/<int:requests_id>', methods=['GET'])
def get_requests(request_id):
    requests = [requests for requests in requests if requests['id'] == task_id]
    if len(requests) == 0:
        abort(404)
    return jsonify({'requests' : requests[0]})

if __name__ == '__main__':
    app.run(debug=True)