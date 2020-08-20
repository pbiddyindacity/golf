from flask_restful import Resource, reqparse
from models.score import ScoreModel

class Score(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('course_id',
                        type=int,
                        required=True,
                        help="The ID for the course.")
    parser.add_argument('golfer_id',
                        type=int,
                        required=True,
                        help="The ID for the golfer.")
    parser.add_argument('hole_number',
                        type=int,
                        required=True,
                        help="The number of the hole on the golf course.")
    parser.add_argument('round_type',
                        type=str,
                        required=True,
                        help="Front 9, back 9, or 18 holes.")
    parser.add_argument('round_timestamp',
                        type=int,
                        required=True,
                        help="The timestamp of the date the round was played.")
    parser.add_argument('enter_timestamp',
                        type=int,
                        required=True,
                        help="The timestamp for when the round was entered into the database.")

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass