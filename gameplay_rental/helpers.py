from flask import request, jsonify, json

from functools import wraps


import secrets
import decimal
import requests

from gameplay_rental.models import User

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split()[1]
            print(token)

        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            our_user = User.query.filter_by(token=token).first()
            print(our_user)
            if not our_user or our_user.token != token:
                return jsonify({'message': 'token is invalid'})
            
        except:
            owner = User.query.filter_by(token=token).first()
            if token != owner.taken and secrets.compare_digest(token, owner.token):
                return jsonify({'message': 'Token is invalid'})
        return our_flask_function(our_user, *args, **kwargs)
    return decorated


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj)
    





# def search(game_name, games_name):
#     r = requests.get('https://api.rawg.io/api/games?key=86962d8203ea4e4587007fc6459fcffa')
#     data = r.json()
#     if data['response'] == 'success':
#         for order, entry in enumerate(data['results']):
#             if entry['name'].lower() == games_name.lower():
#                 return data['results'][order]['image']['url']
#     else:
#         r = requests.get('https://api.rawg.io/api/games?key=86962d8203ea4e4587007fc6459fcffa')
#         data = r.json()
#         if data['response'] == 'success':
#             for order, entry in enumerate(data['results']):
#                 if entry['name'].lower() == game_name.lower():
#                     return data['results'][order]['image']['url']
    