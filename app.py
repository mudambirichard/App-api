from flask import Flask, jsonify, request
from flask import abort
app = Flask(__name__)

users = [
    {
        'id': 1,
        'name':'Ritah Mugaga',
        'email': 'mufda@gmail.com',
        'password': '',
        
    },

      {
        'id': 2,
        'name':'Kato Ann',
        'email': 'mufda@gmail.com',
        'password': '',
        
    },

      {
        'id': 3,
        'name':'Paul Kasozi',
        'email': 'mufda@gmail.com',
        'password': '',
        
    }


]
@app.route('/')
def index():
    return "<h1>Welcome To Mantainance-Tracker</h2>"
    
# this is the method that fetch all the requests of a logged in user
@app.route('/api/v1/users/requests/', methods=['GET'])
def get_requests():
    return jsonify({'users': users})

#this is the method that fetcth the request that belongs to the logged in user
@app.route('/api/v1/users/requests/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user ['id'] == user_id] 
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

#This method Create a request
@app.route('/api/v1/users/requests/', methods=['POST'])
def create_request():
    if not request.json or not 'name' in request.json:
        abort(400)
    usr = {
        'id' : users[-1]['id'] + 1,
        'name' : request.get_json()['name'],
        'password' : request.get_json()['password'],
        'email' :request.get_json()['email']
    }
    users.append(usr)
    return jsonify({'user' : users})

#this method modify the brequest.

@app.route('/api/v1/users/requests/<int:user_id>/', methods=['PUT'])
def update_user(user_id):

    if len(request.json) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if not 'name' in request.json: 
        abort(400)
    if not 'password' in request.json:
        abort(400)
    if not 'email' in request.json: 
        abort(400)
    ind = user_id -1 
    obj = users[ind]
    obj["name"] = request.get_json()['name']
    obj["password"] = request.get_json()["password"]
    obj["email"] = request.get_json()["email"]

    users[ind] = obj
    
    return jsonify(obj),200




if __name__ == '__main__':
    app.run(debug=True)