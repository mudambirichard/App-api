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
@app.route('/api/v1.0/users/requsets', methods=['GET'])
def get_requests( ):
    return jsonify({'users': users})

#this is the method that fetcth the request that belongs to the logged in user
@app.route('/api/v1/users/requests/<int:user_id>', methods=['GET'])
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
        'name' : request.json['name'],
        'password' : request.json['password'],
        'email' :request.json['email']
    }
    user.append(usr)
    return jsonify({'user' : users})

#this method modify the brequest.
@app.route('/api/v1/users/requests/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if users['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type (request.json['name']) != unicode:
        abort(400)
    if 'password' in request.json and type (request.json['password']) != unicode:
        abort(400)
    if 'email' in request.json and type (request.json['email']) != unicode:
        abort(400)
    user[0]['user'] = request.json.get('name',user[0]['name'])
    user[0]['user'] = request.json.get('password',user[0]['password'])
    user[0]['user'] = request.json.get('email',user[0]['email'])
    return  jsonify({'user':user[0]})




if __name__ == '__main__':
    app.run(debug=True)