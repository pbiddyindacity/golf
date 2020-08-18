from flask_restful import Resource, reqparse
from models.hole import HoleModel


class Hole(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('course_id',
                        type=int,
                        required=True,
                        help="The ID for the course.")
    parser.add_argument('hole_number',
                        type=int,
                        required=True,
                        help="The number of the hole on the golf course.")
    parser.add_argument('par',
                        type=int,
                        required=True,
                        help="The par for the hole.")
    parser.add_argument('handicap',
                        type=int,
                        required=True,
                        help="The difficulty rating for the hole compared to the others on the course.")
    parser.add_argument('distance',
                        type=int,
                        required=True,
                        help="The total distance for the hole in yards.")


    def get(self, course_id, hole_number):
        hole = HoleModel.find_by_course_hole(course_id, hole_number)
        if hole:
            return hole.json()
        return {'message': 'Hole not found.'}, 404

    def post(self, course_id, hole_number):
        if HoleModel.find_by_course_hole(course_id, hole_number):
           return {'message': f"This hole has already been entered into the database."}, 400
        data = Hole.parser.parse_args()
        hole = HoleModel(**data)

        try:
            hole.save_to_db()
        except:
            return {'message': 'An error occurred inserting the hole into the database.'}, 500

        return hole.json(), 201

    def put(self, course_id, hole_number):
        pass

    def delete(self, course_id, hole_number):
        hole = HoleModel.find_by_course_hole(course_id, hole_number)
        if hole:
            hole.delete_from_db()
            return {'message': 'The hole has been deleted from the database.'}
        return {'message': 'Hole not found.'}, 404


