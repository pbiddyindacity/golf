import os


from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api

from db import db
from models.course import CourseModel
from models.golfer import GolferModel
from models.hole import HoleModel
from resources.course import Course, CourseList, SingleCourse
from resources.golfer import GolferList
from resources.hole import Hole

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'eric'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.jinja2')


@app.route('/scorecard/new', methods=['GET', 'POST'])
def create_course():
    if request.method == "POST":
        name = request.form.get('coursename')
        city = request.form.get('city')
        state = request.form.get('state')
        slope = request.form.get('slope')
        course = CourseModel(name, city, state, slope)

        if course.find_by_name(name):
            return {'message': f'A course named {name} already exists.'}
        course.save_to_db()

        print(name, city, state, slope, course)

        hole_1_distance = int(request.form.get('hole_1_distance'))
        hole_2_distance = int(request.form.get('hole_2_distance'))
        hole_3_distance = int(request.form.get('hole_3_distance'))
        hole_4_distance = int(request.form.get('hole_4_distance'))
        hole_5_distance = int(request.form.get('hole_5_distance'))
        hole_6_distance = int(request.form.get('hole_6_distance'))
        hole_7_distance = int(request.form.get('hole_7_distance'))
        hole_8_distance = int(request.form.get('hole_8_distance'))
        hole_9_distance = int(request.form.get('hole_9_distance'))
        hole_10_distance = int(request.form.get('hole_10_distance'))
        hole_11_distance = int(request.form.get('hole_11_distance'))
        hole_12_distance = int(request.form.get('hole_12_distance'))
        hole_13_distance = int(request.form.get('hole_13_distance'))
        hole_14_distance = int(request.form.get('hole_14_distance'))
        hole_15_distance = int(request.form.get('hole_15_distance'))
        hole_16_distance = int(request.form.get('hole_16_distance'))
        hole_17_distance = int(request.form.get('hole_17_distance'))
        hole_18_distance = int(request.form.get('hole_18_distance'))

        front_9_distance = (hole_1_distance + hole_2_distance + hole_3_distance +
                            hole_4_distance + hole_5_distance + hole_6_distance +
                            hole_7_distance + hole_8_distance + hole_9_distance)
        back_9_distance = (hole_10_distance + hole_11_distance + hole_12_distance +
                           hole_13_distance + hole_14_distance + hole_15_distance +
                           hole_16_distance + hole_17_distance + hole_18_distance)

        total_distance = front_9_distance + back_9_distance

        hole_1_handicap = int(request.form.get('hole_1_handicap'))
        hole_2_handicap = int(request.form.get('hole_2_handicap'))
        hole_3_handicap = int(request.form.get('hole_3_handicap'))
        hole_4_handicap = int(request.form.get('hole_4_handicap'))
        hole_5_handicap = int(request.form.get('hole_5_handicap'))
        hole_6_handicap = int(request.form.get('hole_6_handicap'))
        hole_7_handicap = int(request.form.get('hole_7_handicap'))
        hole_8_handicap = int(request.form.get('hole_8_handicap'))
        hole_9_handicap = int(request.form.get('hole_9_handicap'))
        hole_10_handicap = int(request.form.get('hole_10_handicap'))
        hole_11_handicap = int(request.form.get('hole_11_handicap'))
        hole_12_handicap = int(request.form.get('hole_12_handicap'))
        hole_13_handicap = int(request.form.get('hole_13_handicap'))
        hole_14_handicap = int(request.form.get('hole_14_handicap'))
        hole_15_handicap = int(request.form.get('hole_15_handicap'))
        hole_16_handicap = int(request.form.get('hole_16_handicap'))
        hole_17_handicap = int(request.form.get('hole_17_handicap'))
        hole_18_handicap = int(request.form.get('hole_18_handicap'))

        hole_1_par = int(request.form.get('hole_1_par'))
        hole_2_par = int(request.form.get('hole_2_par'))
        hole_3_par = int(request.form.get('hole_3_par'))
        hole_4_par = int(request.form.get('hole_4_par'))
        hole_5_par = int(request.form.get('hole_5_par'))
        hole_6_par = int(request.form.get('hole_6_par'))
        hole_7_par = int(request.form.get('hole_7_par'))
        hole_8_par = int(request.form.get('hole_8_par'))
        hole_9_par = int(request.form.get('hole_9_par'))
        hole_10_par = int(request.form.get('hole_10_par'))
        hole_11_par = int(request.form.get('hole_11_par'))
        hole_12_par = int(request.form.get('hole_12_par'))
        hole_13_par = int(request.form.get('hole_13_par'))
        hole_14_par = int(request.form.get('hole_14_par'))
        hole_15_par = int(request.form.get('hole_15_par'))
        hole_16_par = int(request.form.get('hole_16_par'))
        hole_17_par = int(request.form.get('hole_17_par'))
        hole_18_par = int(request.form.get('hole_18_par'))

        front_9_par = (hole_1_par + hole_2_par + hole_3_par +
                       hole_4_par + hole_5_par + hole_6_par +
                       hole_7_par + hole_8_par + hole_9_par)
        back_9_par = (hole_10_par + hole_11_par + hole_12_par +
                      hole_13_par + hole_14_par + hole_15_par +
                      hole_16_par + hole_17_par + hole_18_par)

        total_par = front_9_par + back_9_par

        hole_1 = HoleModel(course.id, 1, hole_1_par, hole_1_handicap, hole_1_distance)
        hole_2 = HoleModel(course.id, 2, hole_2_par, hole_2_handicap, hole_2_distance)
        hole_3 = HoleModel(course.id, 3, hole_3_par, hole_3_handicap, hole_3_distance)
        hole_4 = HoleModel(course.id, 4, hole_4_par, hole_4_handicap, hole_4_distance)
        hole_5 = HoleModel(course.id, 5, hole_5_par, hole_5_handicap, hole_5_distance)
        hole_6 = HoleModel(course.id, 6, hole_6_par, hole_6_handicap, hole_6_distance)
        hole_7 = HoleModel(course.id, 7, hole_7_par, hole_7_handicap, hole_7_distance)
        hole_8 = HoleModel(course.id, 8, hole_8_par, hole_8_handicap, hole_8_distance)
        hole_9 = HoleModel(course.id, 9, hole_9_par, hole_9_handicap, hole_9_distance)
        hole_10 = HoleModel(course.id, 10, hole_10_par, hole_10_handicap, hole_10_distance)
        hole_11 = HoleModel(course.id, 11, hole_11_par, hole_11_handicap, hole_11_distance)
        hole_12 = HoleModel(course.id, 12, hole_12_par, hole_12_handicap, hole_12_distance)
        hole_13 = HoleModel(course.id, 13, hole_13_par, hole_13_handicap, hole_13_distance)
        hole_14 = HoleModel(course.id, 14, hole_14_par, hole_14_handicap, hole_14_distance)
        hole_15 = HoleModel(course.id, 15, hole_15_par, hole_15_handicap, hole_15_distance)
        hole_16 = HoleModel(course.id, 16, hole_16_par, hole_16_handicap, hole_16_distance)
        hole_17 = HoleModel(course.id, 17, hole_17_par, hole_17_handicap, hole_17_distance)
        hole_18 = HoleModel(course.id, 18, hole_18_par, hole_18_handicap, hole_18_distance)

        hole_1.save_to_db()
        hole_2.save_to_db()
        hole_3.save_to_db()
        hole_4.save_to_db()
        hole_5.save_to_db()
        hole_6.save_to_db()
        hole_7.save_to_db()
        hole_8.save_to_db()
        hole_9.save_to_db()
        hole_10.save_to_db()
        hole_11.save_to_db()
        hole_12.save_to_db()
        hole_13.save_to_db()
        hole_14.save_to_db()
        hole_15.save_to_db()
        hole_16.save_to_db()
        hole_17.save_to_db()
        hole_18.save_to_db()

        return render_template('course_scorecard.jinja2', name=name, city=city, state=state, slope=slope,
                               hole_1_distance=hole_1_distance, hole_2_distance=hole_2_distance,
                               hole_3_distance=hole_3_distance, hole_4_distance=hole_4_distance,
                               hole_5_distance=hole_5_distance, hole_6_distance=hole_6_distance,
                               hole_7_distance=hole_7_distance, hole_8_distance=hole_8_distance,
                               hole_9_distance=hole_9_distance, hole_10_distance=hole_10_distance,
                               hole_11_distance=hole_11_distance, hole_12_distance=hole_12_distance,
                               hole_13_distance=hole_13_distance, hole_14_distance=hole_14_distance,
                               hole_15_distance=hole_15_distance, hole_16_distance=hole_16_distance,
                               hole_17_distance=hole_17_distance, hole_18_distance=hole_18_distance,
                               hole_1_par=hole_1_par, hole_2_par=hole_2_par,
                               hole_3_par=hole_3_par, hole_4_par=hole_4_par,
                               hole_5_par=hole_5_par, hole_6_par=hole_6_par,
                               hole_7_par=hole_7_par, hole_8_par=hole_8_par,
                               hole_9_par=hole_9_par, hole_10_par=hole_10_par,
                               hole_11_par=hole_11_par, hole_12_par=hole_12_par,
                               hole_13_par=hole_13_par, hole_14_par=hole_14_par,
                               hole_15_par=hole_15_par, hole_16_par=hole_16_par,
                               hole_17_par=hole_17_par, hole_18_par=hole_18_par,
                               hole_1_handicap=hole_1_handicap, hole_2_handicap=hole_2_handicap,
                               hole_3_handicap=hole_3_handicap, hole_4_handicap=hole_4_handicap,
                               hole_5_handicap=hole_5_handicap, hole_6_handicap=hole_6_handicap,
                               hole_7_handicap=hole_7_handicap, hole_8_handicap=hole_8_handicap,
                               hole_9_handicap=hole_9_handicap, hole_10_handicap=hole_10_handicap,
                               hole_11_handicap=hole_11_handicap, hole_12_handicap=hole_12_handicap,
                               hole_13_handicap=hole_13_handicap, hole_14_handicap=hole_14_handicap,
                               hole_15_handicap=hole_15_handicap, hole_16_handicap=hole_16_handicap,
                               hole_17_handicap=hole_17_handicap, hole_18_handicap=hole_18_handicap,
                               front_9_distance=front_9_distance, back_9_distance=back_9_distance,
                               front_9_par=front_9_par, back_9_par=back_9_par,
                               total_distance=total_distance, total_par=total_par)

    return render_template('blank_scorecard.jinja2')


@app.route('/golfer/create', methods=['GET', 'POST'])
def create_golfer():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        golfer = GolferModel(name, email, phone)
        if golfer.find_by_name(name):
            return {'message': f'A golfer named {name} already exists.'}
        golfer.save_to_db()
        golfers_list = golfer.find_all()
        return render_template('golfer_created.jinja2', name=name, golfers_list=golfers_list)

    return render_template('create_golfer.jinja2')


@app.route('/scorecard', methods=['GET', 'POST'])
def new_scorecard():
    if request.method == "POST":
        name = request.form.get('course')
        return redirect(url_for('course_scorecard', name=name))

    courses_list = [course for course in CourseModel.find_all()]
    return render_template('select_scorecard.jinja2', courses_list=courses_list)


@app.route('/scorecard/<string:name>', methods=['GET', 'POST'])
def course_scorecard(name):
    if name == 'new':
        return redirect(url_for(create_course))
    course = CourseModel.find_by_name(name)
    course_details = course.json()
    _id = course_details['id']
    name = course_details['name']
    city = course_details['city']
    state = course_details['state']
    slope = course_details['slope']

    hole_1 = HoleModel.find_by_course_hole(_id, 1)
    hole_2 = HoleModel.find_by_course_hole(_id, 2)
    hole_3 = HoleModel.find_by_course_hole(_id, 3)
    hole_4 = HoleModel.find_by_course_hole(_id, 4)
    hole_5 = HoleModel.find_by_course_hole(_id, 5)
    hole_6 = HoleModel.find_by_course_hole(_id, 6)
    hole_7 = HoleModel.find_by_course_hole(_id, 7)
    hole_8 = HoleModel.find_by_course_hole(_id, 8)
    hole_9 = HoleModel.find_by_course_hole(_id, 9)
    hole_10 = HoleModel.find_by_course_hole(_id, 10)
    hole_11 = HoleModel.find_by_course_hole(_id, 11)
    hole_12 = HoleModel.find_by_course_hole(_id, 12)
    hole_13 = HoleModel.find_by_course_hole(_id, 13)
    hole_14 = HoleModel.find_by_course_hole(_id, 14)
    hole_15 = HoleModel.find_by_course_hole(_id, 15)
    hole_16 = HoleModel.find_by_course_hole(_id, 16)
    hole_17 = HoleModel.find_by_course_hole(_id, 17)
    hole_18 = HoleModel.find_by_course_hole(_id, 18)
    hole_1_details = hole_1.json()
    hole_2_details = hole_2.json()
    hole_3_details = hole_3.json()
    hole_4_details = hole_4.json()
    hole_5_details = hole_5.json()
    hole_6_details = hole_6.json()
    hole_7_details = hole_7.json()
    hole_8_details = hole_8.json()
    hole_9_details = hole_9.json()
    hole_10_details = hole_10.json()
    hole_11_details = hole_11.json()
    hole_12_details = hole_12.json()
    hole_13_details = hole_13.json()
    hole_14_details = hole_14.json()
    hole_15_details = hole_15.json()
    hole_16_details = hole_16.json()
    hole_17_details = hole_17.json()
    hole_18_details = hole_18.json()

    hole_1_distance = hole_1_details['distance']
    hole_2_distance = hole_2_details['distance']
    hole_3_distance = hole_3_details['distance']
    hole_4_distance = hole_4_details['distance']
    hole_5_distance = hole_5_details['distance']
    hole_6_distance = hole_6_details['distance']
    hole_7_distance = hole_7_details['distance']
    hole_8_distance = hole_8_details['distance']
    hole_9_distance = hole_9_details['distance']
    hole_10_distance = hole_10_details['distance']
    hole_11_distance = hole_11_details['distance']
    hole_12_distance = hole_12_details['distance']
    hole_13_distance = hole_13_details['distance']
    hole_14_distance = hole_14_details['distance']
    hole_15_distance = hole_15_details['distance']
    hole_16_distance = hole_16_details['distance']
    hole_17_distance = hole_17_details['distance']
    hole_18_distance = hole_18_details['distance']

    front_9_distance = (hole_1_distance + hole_2_distance + hole_3_distance +
                        hole_4_distance + hole_5_distance + hole_6_distance +
                        hole_7_distance + hole_8_distance + hole_9_distance)
    back_9_distance = (hole_10_distance + hole_11_distance + hole_12_distance +
                       hole_13_distance + hole_14_distance + hole_15_distance +
                       hole_16_distance + hole_17_distance + hole_18_distance)

    total_distance = front_9_distance + back_9_distance

    hole_1_handicap = hole_1_details['handicap']
    hole_2_handicap = hole_2_details['handicap']
    hole_3_handicap = hole_3_details['handicap']
    hole_4_handicap = hole_4_details['handicap']
    hole_5_handicap = hole_5_details['handicap']
    hole_6_handicap = hole_6_details['handicap']
    hole_7_handicap = hole_7_details['handicap']
    hole_8_handicap = hole_8_details['handicap']
    hole_9_handicap = hole_9_details['handicap']
    hole_10_handicap = hole_10_details['handicap']
    hole_11_handicap = hole_11_details['handicap']
    hole_12_handicap = hole_12_details['handicap']
    hole_13_handicap = hole_13_details['handicap']
    hole_14_handicap = hole_14_details['handicap']
    hole_15_handicap = hole_15_details['handicap']
    hole_16_handicap = hole_16_details['handicap']
    hole_17_handicap = hole_17_details['handicap']
    hole_18_handicap = hole_18_details['handicap']

    hole_1_par = hole_1_details['par']
    hole_2_par = hole_2_details['par']
    hole_3_par = hole_3_details['par']
    hole_4_par = hole_4_details['par']
    hole_5_par = hole_5_details['par']
    hole_6_par = hole_6_details['par']
    hole_7_par = hole_7_details['par']
    hole_8_par = hole_8_details['par']
    hole_9_par = hole_9_details['par']
    hole_10_par = hole_10_details['par']
    hole_11_par = hole_11_details['par']
    hole_12_par = hole_12_details['par']
    hole_13_par = hole_13_details['par']
    hole_14_par = hole_14_details['par']
    hole_15_par = hole_15_details['par']
    hole_16_par = hole_16_details['par']
    hole_17_par = hole_17_details['par']
    hole_18_par = hole_18_details['par']

    front_9_par = (hole_1_par + hole_2_par + hole_3_par +
                   hole_4_par + hole_5_par + hole_6_par +
                   hole_7_par + hole_8_par + hole_9_par)
    back_9_par = (hole_10_par + hole_11_par + hole_12_par +
                  hole_13_par + hole_14_par + hole_15_par +
                  hole_16_par + hole_17_par + hole_18_par)

    total_par = front_9_par + back_9_par

    golfers_list = [golfer for golfer in GolferModel.find_all()]

    return render_template('course_scorecard.jinja2', name=name, city=city, state=state, slope=slope,
                           hole_1_distance=hole_1_distance, hole_2_distance=hole_2_distance,
                           hole_3_distance=hole_3_distance, hole_4_distance=hole_4_distance,
                           hole_5_distance=hole_5_distance, hole_6_distance=hole_6_distance,
                           hole_7_distance=hole_7_distance, hole_8_distance=hole_8_distance,
                           hole_9_distance=hole_9_distance, hole_10_distance=hole_10_distance,
                           hole_11_distance=hole_11_distance, hole_12_distance=hole_12_distance,
                           hole_13_distance=hole_13_distance, hole_14_distance=hole_14_distance,
                           hole_15_distance=hole_15_distance, hole_16_distance=hole_16_distance,
                           hole_17_distance=hole_17_distance, hole_18_distance=hole_18_distance,
                           hole_1_par=hole_1_par, hole_2_par=hole_2_par,
                           hole_3_par=hole_3_par, hole_4_par=hole_4_par,
                           hole_5_par=hole_5_par, hole_6_par=hole_6_par,
                           hole_7_par=hole_7_par, hole_8_par=hole_8_par,
                           hole_9_par=hole_9_par, hole_10_par=hole_10_par,
                           hole_11_par=hole_11_par, hole_12_par=hole_12_par,
                           hole_13_par=hole_13_par, hole_14_par=hole_14_par,
                           hole_15_par=hole_15_par, hole_16_par=hole_16_par,
                           hole_17_par=hole_17_par, hole_18_par=hole_18_par,
                           hole_1_handicap=hole_1_handicap, hole_2_handicap=hole_2_handicap,
                           hole_3_handicap=hole_3_handicap, hole_4_handicap=hole_4_handicap,
                           hole_5_handicap=hole_5_handicap, hole_6_handicap=hole_6_handicap,
                           hole_7_handicap=hole_7_handicap, hole_8_handicap=hole_8_handicap,
                           hole_9_handicap=hole_9_handicap, hole_10_handicap=hole_10_handicap,
                           hole_11_handicap=hole_11_handicap, hole_12_handicap=hole_12_handicap,
                           hole_13_handicap=hole_13_handicap, hole_14_handicap=hole_14_handicap,
                           hole_15_handicap=hole_15_handicap, hole_16_handicap=hole_16_handicap,
                           hole_17_handicap=hole_17_handicap, hole_18_handicap=hole_18_handicap,
                           front_9_distance=front_9_distance, back_9_distance=back_9_distance,
                           front_9_par=front_9_par, back_9_par=back_9_par,
                           total_distance=total_distance, total_par=total_par, golfers_list=golfers_list)


@app.route('/golfers')
def golfers():
    golfers_list = [golfer for golfer in GolferModel.find_all()]
    return render_template("golfers.jinja2", golfers_list=golfers_list)


api.add_resource(SingleCourse, '/scorecard/<string:name>')
api.add_resource(CourseList, '/courses')
api.add_resource(GolferList, '/golfers')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
