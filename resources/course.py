from flask_restful import Resource, reqparse
from models.course import CourseModel


class Course(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="The name of the golf course.")
    parser.add_argument('city',
                        type=str,
                        required=True,
                        help="The name of the city where the golf course is located.")
    parser.add_argument('state',
                        type=str,
                        required=True,
                        help="The name of the state where the golf course is located.")
    parser.add_argument('slope',
                        type=float,
                        required=True,
                        help="The slope rating for the golf course."
                             "An entry of 0 means the slope was not listed on the scorecard.")

    def get(self, name):
        course = CourseModel.find_by_name(name)
        if course:
            return course.json()
        return {'message': 'Course not found.'}, 404

    def post(self, name):
        if CourseModel.find_by_name(name):
           return {'message': f"A course with name '{name}' is already entered into the database."}, 400
        data = Course.parser.parse_args()
        course = CourseModel(name, **data)

        try:
            course.save_to_db()
        except:
            return {'message': 'An error occurred inserting the course into the database.'}, 500

        return course.json(), 201

    def put(self, course_id):
        pass

    def delete(self, course_id):
        course = CourseModel.find_by_id(course_id)
        if course:
            course.delete_from_db()
            return {'message': 'The course has been deleted from the database.'}
        return {'message': 'Course not found.'}, 404


class CourseList(Resource):
    def get(self):
        return {'courses': [course.json() for course in CourseModel.find_all()]}

class SingleCourse(Resource):
    def get(self, name):
        return {'course': [course.json() for course in CourseModel.find_by_name(name)]}

