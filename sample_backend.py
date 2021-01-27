from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
import string
from model_mongodb import User


app = Flask(__name__)

#CORS stands for Cross Origin Requests.
CORS(app) #Here we'll allow requests coming from any domain. Not recommended for production environment.



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        if search_username and search_job:
            # TODO: Replace with database access
            #result = find_users_by_name_job(search_username, search_job)  
            result = User().find_by_name_and_job(search_username, search_job)
        elif search_username:
            # using list shorthand for filtering the list.
            # TODO: Replace with database access
            #result = [user for user in users['users_list'] if user['name'] == search_username]
            result = User().find_by_name(search_username)
        else:
            result = User().find_all()
        return {"users_list": result}
    elif request.method == 'POST':
        userToAdd = request.get_json() # no need to generate an id ourselves
        newUser = User(userToAdd)
        newUser.save() # pymongo gives the record an "_id" field automatically
        resp = jsonify(newUser), 201
        return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        user = User({"_id":id})
        if user.reload() :
            return user
        else :
            return jsonify({"error": "User not found"}), 404
    elif request.method == 'DELETE':
        user = User({"_id":id})
        resp = user.remove()

        # TODO: Check the resp object if the removal was successful or not.
        # Return a 404 status code if it was not successful
        #print(resp)
        if resp['n'] == 1 and resp['ok'] == 1.0:
            return resp, 204
        return jsonify({"error": "User not found"}), 404

"""def find_users_by_name_job(name, job):
    subdict = {'users_list' : []}
    for user in users['users_list']:
        if user['name'] == name and user['job'] == job:
            subdict['users_list'].append(user)
    return subdict  """