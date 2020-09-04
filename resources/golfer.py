from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_restful import Resource, reqparse
from models.golfer import GolferModel

parser = reqparse.RequestParser()
parser.add_argument('name',
                    type=str,
                    required=True,
                    help="The name of the golf course.")
parser.add_argument('email',
                    type=str,
                    required=True,
                    help="The email address for the golfer.")
parser.add_argument('phone',
                    type=str,
                    required=True,
                    help="The phone number for the golfer.")


class GolferRegister(Resource):

    def post(self):
        data = parser.parse_args()
        if GolferModel.find_by_name(data['name']):
            return {'message': f"A golfer with name '{data['name']}' is already entered into the database."}, 400
        golfer = GolferModel(**data)
        try:
            golfer.save_to_db()
        except:
            return {'message': 'An error occurred inserting the golfer into the database.'}, 500
        golfer_data = golfer.json()
        return redirect(url_for('golfer_created', data=jsonify(golfer_data['name'])), code=307), 201

class Golfer(Resource):
    def get(self, name):
        golfer = GolferModel.find_by_name(name)
        if golfer:
            return golfer.json()
        return {'message': 'Golfer not found.'}, 404

    def post(self, name):
        if GolferModel.find_by_name(name):
           return {'message': f"A golfer with name '{name}' is already entered into the database."}, 400
        data = Golfer.parser.parse_args()
        golfer = GolferModel(**data)

        try:
            golfer.save_to_db()
        except:
            return {'message': 'An error occurred inserting the golfer into the database.'}, 500

        return redirect(url_for('golfers')), 201

    def put(self, golfer_id):
        pass

    def delete(self, golfer_id):
        golfer = GolferModel.find_by_id(golfer_id)
        if golfer:
            golfer.delete_from_db()
            return {'message': 'The golfer has been deleted from the database.'}
        return {'message': 'Golfer not found.'}, 404


class GolferList(Resource):
    def get(self):
        golfers_data = {'golfers': [golfer.json() for golfer in GolferModel.find_all()]}
#        return redirect(url_for('golfers'), golfers_data), 201
        return golfers_data
