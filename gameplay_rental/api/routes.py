from flask import Blueprint, request, jsonify
from gameplay_rental.helpers import token_required
from gameplay_rental.models import db, Game, game_schema, games_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
@token_required
def getdata(our_user):
    return {'some': 'value'}

@api.route('/game', methods = ['POST'])
@token_required
def create_gameplay(our_user):

    game_search = request.json['search']
    game_search_precise = request.json['game_search_precise']
    game_search_exact = request.json['game_search_exact']
    game_platforms = request.json['game_platforms']
    game_stores = request.json['game_stores']
    game_developers = request.json['game_developers']
    game_dates = request.json['game_dates']
    game_publishers = request.json['game_publishers']
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    game = Game(game_search, game_search_precise, game_search_exact, game_platforms, game_stores, game_developers, game_dates, game_publishers, user_token = user_token)

    db.session.add(game)
    db.session.commit()

    response = game_schema.dump(game)

    return jsonify(response)

@api.route('/game', methods = ['GET'])
@token_required
def get_game(our_user):
    owner = our_user.token
    Game = Game.query.filter_by(user_token = owner).all()
    response = games_schema.dump(Game)

    return jsonify(response)

@api.route('/games/<id>', methods = ['GET'])
@token_required
def get_games(our_user, id):
    if id:
        Game = Game.query.get(id)
        response = game_schema.dump(Game)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Id required'}), 401

@api.route('/games/<id>', methods = ['GET'])
@token_required
def update_game(our_user, id):
    Game = Game.query.get(id)
    Game.game_search = request.json['search']
    Game.game_search_precise = request.json['game_search_precise']
    Game.game_search_exact = request.json['game_search_exact']
    Game.game_platforms = request.json['game_platforms']
    Game.game_stores = request.json['game_stores']
    Game.game_developers = request.json['game_developers']
    Game.game_dates = request.json['game_dates']
    Game.game_publishers = request.json['game_publishers']
    Game.user_token = our_user.token

    db.session.commit()

    response = game_schema.dump(Game)

    return jsonify(response)

@api.route('/games/<id>', methods = ['DELETE'])
@token_required
def delete_games(our_user, id):
    Game = Game.query.get(id)
    db.session.delete(Game)
    db.session.commit()

    response = game_schema.dump(Game)
    return jsonify(response)
# https://api.rawg.io/api/games?key=86962d8203ea4e4587007fc6459fcffa
