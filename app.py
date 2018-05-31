from flask import Flask, jsonify, request
from flask import abort
app = Flask(__name__)




    #this methods Modify a request
    @app.route('/api/v1/users/requests/<int_id>', methods=['PUT'])
    def update_user(user_id):
        user = [user for user in users if user['id'] == user_id]
        if len(user) == 0:
            abort(404)
        if not request.json:
            abort(400)
        if 'name' in request.json and type (request.json['name']) != unicode: 
            abort(400)
        if 'email' in request.json and type (request.json['email']) != unicode:
            abort(400)
        if 'password' in request.json and type (request.json['password']) != unicode:
            abort(404)
        
        user[0]['user'] = request.json.get('name',user[0]['name'])
        user[0]['user'] = request.json.get('password',user[0]['password'])
        user[0]['user'] = request.json.get('email',user[0]['email'])
        return jsonify({'user' : user[0]})

    

if __name__ == '__main__':
    app.run(debug=True)