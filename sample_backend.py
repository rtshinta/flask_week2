from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def randomID():
    l1 = chr(random.randint(65, 122))
    l2 = chr(random.randint(65, 122))
    l3 = chr(random.randint(65, 122))
    num = random.randint(100, 999)
    return l1 + l2 + l3 + str(num)

@app.route('/')
def hello_world():
    return 'Hello, world!'

"""@app.route('/users')
def get_users():
    search_username = request.args.get('name')
    if search_username:
        subdict = {'users_list' : []}
        for user in users['users_list']:
            if user['name'] == search_username:
                subdict['users_list'].append(user)
        return subdict
    return users"""
    
@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return ({})
        return users
    elif request.method == 'DELETE':
        if id:
            count = 0
            for user in users['users_list']:
                if user['id'] == id:
                    users['users_list'].pop(count)
                    resp = jsonify(success=True)
                    resp.status_code = 201
                    return resp
                count += 1
        return jsonify(success=False)

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        if search_username and search_job:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username and user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict
        if search_username:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = randomID()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        resp.status_code = 201
        #resp.status_code = 200 #optionally, you can always set a response code. 
        # 200 is the default code for a normal response
        return resp
    elif request.method == 'DELETE':
        userToDelete = request.args.get('name')
        if userToDelete:
            count = 0
            for user in users['users_list']:
                if user['name'] == userToDelete:
                    users['users_list'].pop(count)
                    resp = jsonify(success=True)
                    resp.status_code = 201
                    return resp
                count += 1
        return jsonify(success=False)
    


