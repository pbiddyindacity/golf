import os

import pytz
from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api

from db import db
from models.course import CourseModel
from models.golfer import GolferModel
from models.hole import HoleModel
from models.score import ScoreModel
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'eric'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/golf')
def home():
    return render_template('home.jinja2')


@app.route('/golf/scorecard/new', methods=['GET', 'POST'])
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

        hole_distance_list = []

        hole_distance_list.append(int(request.form.get('h1d')))
        hole_distance_list.append(int(request.form.get('h2d')))
        hole_distance_list.append(int(request.form.get('h3d')))
        hole_distance_list.append(int(request.form.get('h4d')))
        hole_distance_list.append(int(request.form.get('h5d')))
        hole_distance_list.append(int(request.form.get('h6d')))
        hole_distance_list.append(int(request.form.get('h7d')))
        hole_distance_list.append(int(request.form.get('h8d')))
        hole_distance_list.append(int(request.form.get('h9d')))
        hole_distance_list.append(int(request.form.get('h10d')))
        hole_distance_list.append(int(request.form.get('h11d')))
        hole_distance_list.append(int(request.form.get('h12d')))
        hole_distance_list.append(int(request.form.get('h13d')))
        hole_distance_list.append(int(request.form.get('h14d')))
        hole_distance_list.append(int(request.form.get('h15d')))
        hole_distance_list.append(int(request.form.get('h16d')))
        hole_distance_list.append(int(request.form.get('h17d')))
        hole_distance_list.append(int(request.form.get('h18d')))

        front_9_distance = (hole_distance_list[0] + hole_distance_list[1] + hole_distance_list[2] +
                       hole_distance_list[3] + hole_distance_list[4] + hole_distance_list[5] +
                       hole_distance_list[6] + hole_distance_list[7] + hole_distance_list[8])
        back_9_distance = (hole_distance_list[9] + hole_distance_list[10] + hole_distance_list[11] +
                      hole_distance_list[12] + hole_distance_list[13] + hole_distance_list[14] +
                      hole_distance_list[15] + hole_distance_list[16] + hole_distance_list[17])

        total_distance = front_9_distance + back_9_distance

        hole_handicap_list = []
        
        hole_handicap_list.append(int(request.form.get('h1p')))
        hole_handicap_list.append(int(request.form.get('h2h')))
        hole_handicap_list.append(int(request.form.get('h3h')))
        hole_handicap_list.append(int(request.form.get('h4h')))
        hole_handicap_list.append(int(request.form.get('h5h')))
        hole_handicap_list.append(int(request.form.get('h6h')))
        hole_handicap_list.append(int(request.form.get('h7h')))
        hole_handicap_list.append(int(request.form.get('h8h')))
        hole_handicap_list.append(int(request.form.get('h9h')))
        hole_handicap_list.append(int(request.form.get('h10h')))
        hole_handicap_list.append(int(request.form.get('h11h')))
        hole_handicap_list.append(int(request.form.get('h12h')))
        hole_handicap_list.append(int(request.form.get('h13h')))
        hole_handicap_list.append(int(request.form.get('h14h')))
        hole_handicap_list.append(int(request.form.get('h15h')))
        hole_handicap_list.append(int(request.form.get('h16h')))
        hole_handicap_list.append(int(request.form.get('h17h')))
        hole_handicap_list.append(int(request.form.get('h18h')))

        hole_par_list = []
        
        hole_par_list.append(int(request.form.get('h1p')))
        hole_par_list.append(int(request.form.get('h2p')))
        hole_par_list.append(int(request.form.get('h3p')))
        hole_par_list.append(int(request.form.get('h4p')))
        hole_par_list.append(int(request.form.get('h5p')))
        hole_par_list.append(int(request.form.get('h6p')))
        hole_par_list.append(int(request.form.get('h7p')))
        hole_par_list.append(int(request.form.get('h8p')))
        hole_par_list.append(int(request.form.get('h9p')))
        hole_par_list.append(int(request.form.get('h10p')))
        hole_par_list.append(int(request.form.get('h11p')))
        hole_par_list.append(int(request.form.get('h12p')))
        hole_par_list.append(int(request.form.get('h13p')))
        hole_par_list.append(int(request.form.get('h14p')))
        hole_par_list.append(int(request.form.get('h15p')))
        hole_par_list.append(int(request.form.get('h16p')))
        hole_par_list.append(int(request.form.get('h17p')))
        hole_par_list.append(int(request.form.get('h18p')))
        
        front_9_par = (hole_par_list[0] + hole_par_list[1] + hole_par_list[2] +
                       hole_par_list[3] + hole_par_list[4] + hole_par_list[5] + 
                       hole_par_list[6] + hole_par_list[7] + hole_par_list[8])
        back_9_par = (hole_par_list[9] + hole_par_list[10] + hole_par_list[11] + 
                      hole_par_list[12] + hole_par_list[13] + hole_par_list[14] + 
                      hole_par_list[15] + hole_par_list[16] + hole_par_list[17])

        total_par = front_9_par + back_9_par

        for i in range(1, 19):
            hole = HoleModel(course.id, i, hole_par_list[i - 1], hole_handicap_list[i - 1], hole_distance_list[i - 1])
            hole.save_to_db()

        h1p, h2p, h3p, h4p, h5p, h6p, h7p, h8p, h9p, h10p, h11p, h12p, h13p, h14p, h15p, h16p, h17p, h18p = [p for p in hole_par_list]
        h1d, h2d, h3d, h4d, h5d, h6d, h7d, h8d, h9d, h10d, h11d, h12d, h13d, h14d, h15d, h16d, h17d, h18d = [d for d in hole_distance_list]
        h1h, h2h, h3h, h4h, h5h, h6h, h7h, h8h, h9h, h10h, h11h, h12h, h13h, h14h, h15h, h16h, h17h, h18h = [h for h in hole_handicap_list]

        return render_template('course_scorecard.jinja2', name=name, city=city, state=state, slope=slope,
                               h1p=h1p, h2p=h2p, h3p=h3p, h4p=h4p, h5p=h5p, h6p=h6p, h7p=h7p, h8p=h8p, h9p=h9p,
                               h10p=h10p, h11p=h11p, h12p=h12p, h13p=h13p, h14p=h14p, h15p=h15p, h16p=h16p, h17p=h17p,
                               h18p=h18p, h1d=h1d, h2d=h2d, h3d=h3d, h4d=h4d, h5d=h5d, h6d=h6d, h7d=h7d, h8d=h8d,
                               h9d=h9d, h10d=h10d, h11d=h11d, h12d=h12d, h13d=h13d, h14d=h14d, h15d=h15d, h16d=h16d,
                               h17d=h17d, h18d=h18d, h1h=h1h, h2h=h2h, h3h=h3h, h4h=h4h, h5h=h5h, h6h=h6h, h7h=h7h,
                               h8h=h8h, h9h=h9h, h10h=h10h, h11h=h11h, h12h=h12h, h13h=h13h, h14h=h14h, h15h=h15h,
                               h16h=h16h, h17h=h17h, h18h=h18h, front_9_distance=front_9_distance,
                               back_9_distance=back_9_distance, front_9_par=front_9_par, back_9_par=back_9_par,
                               total_distance=total_distance, total_par=total_par)


    return render_template('blank_scorecard.jinja2')


@app.route('/golf/golfer/create', methods=['GET', 'POST'])
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


@app.route('/golf/scorecard', methods=['GET', 'POST'])
def new_scorecard():
    if request.method == "POST":
        name = request.form.get('course')
        return redirect(url_for('course_scorecard', name=name))

    courses_list = [course for course in CourseModel.find_all()]
    return render_template('select_scorecard.jinja2', courses_list=courses_list)


@app.route('/golf/scorecard/<string:name>', methods=['GET', 'POST'])
def course_scorecard(name):
    if name == 'new':
        return redirect(url_for('create_course'))
    course = CourseModel.find_by_name(name)
    course_details = course.json()
    _id = course_details['id']
    name = course_details['name']
    city = course_details['city']
    state = course_details['state']
    slope = course_details['slope']

    front_9_distance = back_9_distance = front_9_par = back_9_par = 0
    p1f9 = p1b9 = p2f9 = p2b9 = p3f9 = p3b9 = p4f9 = p4b9 = 0
    par_list = []
    distance_list = []
    handicap_list = []

    for i in range(1, 19):
        hole = HoleModel.find_by_course_hole(_id, i)
        hole_details = hole.json()
        hole_par = hole_details['par']
        hole_distance = hole_details['distance']
        hole_handicap = hole_details['handicap']
        par_list.append(hole_par)
        distance_list.append(hole_distance)
        handicap_list.append(hole_handicap)

        if i < 10:
            front_9_par += hole_par
            front_9_distance += hole_distance
        elif i >= 10:
            back_9_par += hole_par
            back_9_distance += hole_distance

    total_par = front_9_par + back_9_par
    total_distance = front_9_distance + back_9_distance

    h1p, h2p, h3p, h4p, h5p, h6p, h7p, h8p, h9p, h10p, h11p, h12p, h13p, h14p, h15p, h16p, h17p, h18p = [p for p in par_list]
    h1d, h2d, h3d, h4d, h5d, h6d, h7d, h8d, h9d, h10d, h11d, h12d, h13d, h14d, h15d, h16d, h17d, h18d = [d for d in distance_list]
    h1h, h2h, h3h, h4h, h5h, h6h, h7h, h8h, h9h, h10h, h11h, h12h, h13h, h14h, h15h, h16h, h17h, h18h = [h for h in handicap_list]

    if request.method == "POST":
        course = CourseModel.find_by_name(name)
        course_details = course.json()
        course_id = course_details['id']
        course_name = course_details['name']
        round_date = request.form.get('round_date')
        round_datetime = datetime.strptime(round_date, '%Y-%m-%d')
        new_round_date = round_datetime.strftime('%m/%d/%Y')
        round_datetime_utc = round_datetime.astimezone(pytz.utc)
        round_timestamp = round_datetime_utc.timestamp()
        current_datetime_utc = datetime.now(tz=pytz.utc)
        enter_timestamp = int(current_datetime_utc.timestamp())

        p1f9_scores = []
        p1b9_scores = []
        p2f9_scores = []
        p2b9_scores = []
        p3f9_scores = []
        p3b9_scores = []
        p4f9_scores = []
        p4b9_scores = []
        p1_round_scores = []
        p2_round_scores = []
        p3_round_scores = []
        p4_round_scores = []
        p1h1=p1h2=p1h3=p1h4=p1h5=p1h6=p1h7=p1h8=p1h9=p1h10=p1h11=p1h12=p1h13=p1h14=p1h15=p1h16=p1h17=p1h18 = ''
        p2h1=p2h2=p2h3=p2h4=p2h5=p2h6=p2h7=p2h8=p2h9=p2h10=p2h11=p2h12=p2h13=p2h14=p2h15=p2h16=p2h17=p2h18 = ''
        p3h1=p3h2=p3h3=p3h4=p3h5=p3h6=p3h7=p3h8=p3h9=p3h10=p3h11=p3h12=p3h13=p3h14=p3h15=p3h16=p3h17=p3h18 = ''
        p4h1=p4h2=p4h3=p4h4=p4h5=p4h6=p4h7=p4h8=p4h9=p4h10=p4h11=p4h12=p4h13=p4h14=p4h15=p4h16=p4h17=p4h18 = ''
        p1_total_score = p2_total_score = p3_total_score = p4_total_score = ''

### PLAYER 1 ###

        p1_name = request.form.get('golfer_1')
        p1 = GolferModel.find_by_name(p1_name)
        if p1:
            p1_details = p1.json()
            p1_id = p1_details['id']
            p1_name = p1_details['name']

            p1h1 = request.form.get('p1_hole_1_score')
            p1h2 = request.form.get('p1_hole_2_score')
            p1h3 = request.form.get('p1_hole_3_score')
            p1h4 = request.form.get('p1_hole_4_score')
            p1h5 = request.form.get('p1_hole_5_score')
            p1h6 = request.form.get('p1_hole_6_score')
            p1h7 = request.form.get('p1_hole_7_score')
            p1h8 = request.form.get('p1_hole_8_score')
            p1h9 = request.form.get('p1_hole_9_score')
            p1h10 = request.form.get('p1_hole_10_score')
            p1h11 = request.form.get('p1_hole_11_score')
            p1h12 = request.form.get('p1_hole_12_score')
            p1h13 = request.form.get('p1_hole_13_score')
            p1h14 = request.form.get('p1_hole_14_score')
            p1h15 = request.form.get('p1_hole_15_score')
            p1h16 = request.form.get('p1_hole_16_score')
            p1h17 = request.form.get('p1_hole_17_score')
            p1h18 = request.form.get('p1_hole_18_score')

            p1f9_scores.extend([p1h1, p1h2, p1h3, p1h4, p1h5, p1h6, p1h7, p1h8, p1h9])
            p1b9_scores.extend([p1h10, p1h11, p1h12, p1h13, p1h14, p1h15, p1h16, p1h17, p1h18])

            for i in range(len(p1f9_scores)):
                p1_round_scores.append(p1f9_scores[i])
            for i in range(len(p1b9_scores)):
                p1_round_scores.append(p1b9_scores[i])

            if len(p1f9_scores) == 9 and len(p1b9_scores) == 9:
                p1_round_type = '18 holes'
            elif len(p1f9_scores) == 9 and len(p1b9_scores) != 9:
                p1_round_type = 'Front 9'
            elif len(p1f9_scores) != 9 and len(p1b9_scores) == 9:
                p1_round_type = 'Back 9'
            elif len(p1f9_scores) != 9 and len(p1b9_scores) != 9:
                p1_round_type = 'Invalid'

            for i in range(1, 19):
                hole_number = i
                score = int(p1_round_scores[i - 1])
                p1_score = ScoreModel(course_id, p1_id, hole_number, score, p1_round_type, round_timestamp, enter_timestamp)
                p1_score.save_to_db()
                if i < 10:
                    p1f9 += score
                elif i >= 10:
                    p1b9 += score

            p1_total_score = p1b9 + p1f9

            p1h1, p1h2, p1h3, p1h4, p1h5, p1h6, p1h7, p1h8, p1h9 = [score for score in p1f9_scores]
            p1h10, p1h11, p1h12, p1h13, p1h14, p1h15, p1h16, p1h17, p1h18 = [score for score in p1b9_scores]

        else:
            p1_name = p1f9 = p1b9 = ''

        ### PLAYER 2 ###
        p2_name = request.form.get('golfer_2')
        p2 = GolferModel.find_by_name(p2_name)
        if p2:
            p2_details = p2.json()
            p2_id = p2_details['id']
            p2_name = p2_details['name']

            p2h1 = request.form.get('p2_hole_1_score')
            p2h2 = request.form.get('p2_hole_2_score')
            p2h3 = request.form.get('p2_hole_3_score')
            p2h4 = request.form.get('p2_hole_4_score')
            p2h5 = request.form.get('p2_hole_5_score')
            p2h6 = request.form.get('p2_hole_6_score')
            p2h7 = request.form.get('p2_hole_7_score')
            p2h8 = request.form.get('p2_hole_8_score')
            p2h9 = request.form.get('p2_hole_9_score')
            p2h10 = request.form.get('p2_hole_10_score')
            p2h11 = request.form.get('p2_hole_11_score')
            p2h12 = request.form.get('p2_hole_12_score')
            p2h13 = request.form.get('p2_hole_13_score')
            p2h14 = request.form.get('p2_hole_14_score')
            p2h15 = request.form.get('p2_hole_15_score')
            p2h16 = request.form.get('p2_hole_16_score')
            p2h17 = request.form.get('p2_hole_17_score')
            p2h18 = request.form.get('p2_hole_18_score')

            p2f9_scores.extend([p2h1, p2h2, p2h3, p2h4, p2h5, p2h6, p2h7, p2h8, p2h9])
            p2b9_scores.extend([p2h10, p2h11, p2h12, p2h13, p2h14, p2h15, p2h16, p2h17, p2h18])

            for i in range(len(p2f9_scores)):
                p2_round_scores.append(p2f9_scores[i])
            for i in range(len(p2b9_scores)):
                p2_round_scores.append(p2b9_scores[i])

            if len(p2f9_scores) == 9 and len(p2b9_scores) == 9:
                p2_round_type = '18 holes'
            elif len(p2f9_scores) == 9 and len(p2b9_scores) != 9:
                p2_round_type = 'Front 9'
            elif len(p2f9_scores) != 9 and len(p2b9_scores) == 9:
                p2_round_type = 'Back 9'
            elif len(p2f9_scores) != 9 and len(p2b9_scores) != 9:
                p2_round_type = 'Invalid'

            for i in range(1, 19):
                hole_number = i
                score = int(p2_round_scores[i - 1])
                p2_score = ScoreModel(course_id, p2_id, hole_number, score, p2_round_type, round_timestamp, enter_timestamp)
                p2_score.save_to_db()
                if i < 10:
                    p2f9 += score
                elif i >= 10:
                    p2b9 += score

            p2_total_score = p2b9 + p2f9

            p2h1, p2h2, p2h3, p2h4, p2h5, p2h6, p2h7, p2h8, p2h9 = [score for score in p2f9_scores]
            p2h10, p2h11, p2h12, p2h13, p2h14, p2h15, p2h16, p2h17, p2h18 = [score for score in p2b9_scores]

        else:
            p2_name = p2f9 = p2b9 = ''

### PLAYER 3 ###
        p3_name = request.form.get('golfer_3')
        p3 = GolferModel.find_by_name(p3_name)
        if p3:
            p3_details = p3.json()
            p3_id = p3_details['id']
            p3_name = p3_details['name']

            p3h1 = request.form.get('p3_hole_1_score')
            p3h2 = request.form.get('p3_hole_2_score')
            p3h3 = request.form.get('p3_hole_3_score')
            p3h4 = request.form.get('p3_hole_4_score')
            p3h5 = request.form.get('p3_hole_5_score')
            p3h6 = request.form.get('p3_hole_6_score')
            p3h7 = request.form.get('p3_hole_7_score')
            p3h8 = request.form.get('p3_hole_8_score')
            p3h9 = request.form.get('p3_hole_9_score')
            p3h10 = request.form.get('p3_hole_10_score')
            p3h11 = request.form.get('p3_hole_11_score')
            p3h12 = request.form.get('p3_hole_12_score')
            p3h13 = request.form.get('p3_hole_13_score')
            p3h14 = request.form.get('p3_hole_14_score')
            p3h15 = request.form.get('p3_hole_15_score')
            p3h16 = request.form.get('p3_hole_16_score')
            p3h17 = request.form.get('p3_hole_17_score')
            p3h18 = request.form.get('p3_hole_18_score')

            p3f9_scores.extend([p3h1, p3h2, p3h3, p3h4, p3h5, p3h6, p3h7, p3h8, p3h9])
            p3b9_scores.extend([p3h10, p3h11, p3h12, p3h13, p3h14, p3h15, p3h16, p3h17, p3h18])

            for i in range(len(p3f9_scores)):
                p3_round_scores.append(p3f9_scores[i])
            for i in range(len(p3b9_scores)):
                p3_round_scores.append(p3b9_scores[i])

            if len(p3f9_scores) == 9 and len(p3b9_scores) == 9:
                p3_round_type = '18 holes'
            elif len(p3f9_scores) == 9 and len(p3b9_scores) != 9:
                p3_round_type = 'Front 9'
            elif len(p3f9_scores) != 9 and len(p3b9_scores) == 9:
                p3_round_type = 'Back 9'
            elif len(p3f9_scores) != 9 and len(p3b9_scores) != 9:
                p3_round_type = 'Invalid'

            for i in range(1, 19):
                hole_number = i
                score = int(p3_round_scores[i - 1])
                p3_score = ScoreModel(course_id, p3_id, hole_number, score, p3_round_type, round_timestamp, enter_timestamp)
                p3_score.save_to_db()
                if i < 10:
                    p3f9 += score
                elif i >= 10:
                    p3b9 += score

            p3_total_score = p3b9 + p3f9

            p3h1, p3h2, p3h3, p3h4, p3h5, p3h6, p3h7, p3h8, p3h9 = [score for score in p3f9_scores]
            p3h10, p3h11, p3h12, p3h13, p3h14, p3h15, p3h16, p3h17, p3h18 = [score for score in p3b9_scores]

        else:
            p3_name = p3f9 = p3b9 = ''

### PLAYER 4 ###
        p4_name = request.form.get('golfer_4')
        p4 = GolferModel.find_by_name(p4_name)
        if p4:
            p4_details = p4.json()
            p4_id = p4_details['id']
            p4_name = p4_details['name']

            p4h1 = request.form.get('p4_hole_1_score')
            p4h2 = request.form.get('p4_hole_2_score')
            p4h3 = request.form.get('p4_hole_3_score')
            p4h4 = request.form.get('p4_hole_4_score')
            p4h5 = request.form.get('p4_hole_5_score')
            p4h6 = request.form.get('p4_hole_6_score')
            p4h7 = request.form.get('p4_hole_7_score')
            p4h8 = request.form.get('p4_hole_8_score')
            p4h9 = request.form.get('p4_hole_9_score')
            p4h10 = request.form.get('p4_hole_10_score')
            p4h11 = request.form.get('p4_hole_11_score')
            p4h12 = request.form.get('p4_hole_12_score')
            p4h13 = request.form.get('p4_hole_13_score')
            p4h14 = request.form.get('p4_hole_14_score')
            p4h15 = request.form.get('p4_hole_15_score')
            p4h16 = request.form.get('p4_hole_16_score')
            p4h17 = request.form.get('p4_hole_17_score')
            p4h18 = request.form.get('p4_hole_18_score')

            p4f9_scores.extend([p4h1, p4h2, p4h3, p4h4, p4h5, p4h6, p4h7, p4h8, p4h9])
            p4b9_scores.extend([p4h10, p4h11, p4h12, p4h13, p4h14, p4h15, p4h16, p4h17, p4h18])

            for i in range(len(p4f9_scores)):
                p4_round_scores.append(p4f9_scores[i])
            for i in range(len(p4b9_scores)):
                p4_round_scores.append(p4b9_scores[i])

            if len(p4f9_scores) == 9 and len(p4b9_scores) == 9:
                p4_round_type = '18 holes'
            elif len(p4f9_scores) == 9 and len(p4b9_scores) != 9:
                p4_round_type = 'Front 9'
            elif len(p4f9_scores) != 9 and len(p4b9_scores) == 9:
                p4_round_type = 'Back 9'
            elif len(p4f9_scores) != 9 and len(p4b9_scores) != 9:
                p4_round_type = 'Invalid'

            for i in range(1, 19):
                hole_number = i
                score = int(p4_round_scores[i - 1])
                p4_score = ScoreModel(course_id, p4_id, hole_number, score, p4_round_type, round_timestamp, enter_timestamp)
                p4_score.save_to_db()
                if i < 10:
                    p4f9 += score
                elif i >= 10:
                    p4b9 += score

            p4_total_score = p4b9 + p4f9

            p4h1, p4h2, p4h3, p4h4, p4h5, p4h6, p4h7, p4h8, p4h9 = [score for score in p4f9_scores]
            p4h10, p4h11, p4h12, p4h13, p4h14, p4h15, p4h16, p4h17, p4h18 = [score for score in p4b9_scores]

        else:
            p4_name = p4f9 = p4b9 = ''

        return redirect(url_for('round', course_name=course_name, enter_timestamp=enter_timestamp))

    golfers_list = [golfer for golfer in GolferModel.find_all()]

    return render_template('course_scorecard.jinja2', name=name, city=city, state=state, slope=slope,
                           h1p=h1p, h2p=h2p, h3p=h3p, h4p=h4p, h5p=h5p, h6p=h6p, h7p=h7p, h8p=h8p, h9p=h9p,
                           h10p=h10p, h11p=h11p, h12p=h12p, h13p=h13p, h14p=h14p, h15p=h15p, h16p=h16p, h17p=h17p,
                           h18p=h18p, h1d=h1d, h2d=h2d, h3d=h3d, h4d=h4d, h5d=h5d, h6d=h6d, h7d=h7d, h8d=h8d, h9d=h9d,
                           h10d=h10d, h11d=h11d, h12d=h12d, h13d=h13d, h14d=h14d, h15d=h15d, h16d=h16d, h17d=h17d,
                           h18d=h18d, h1h=h1h, h2h=h2h, h3h=h3h, h4h=h4h, h5h=h5h, h6h=h6h, h7h=h7h, h8h=h8h, h9h=h9h,
                           h10h=h10h, h11h=h11h, h12h=h12h, h13h=h13h, h14h=h14h, h15h=h15h, h16h=h16h, h17h=h17h,
                           h18h=h18h, front_9_distance=front_9_distance, back_9_distance=back_9_distance,
                           front_9_par=front_9_par, back_9_par=back_9_par,
                           total_distance=total_distance, total_par=total_par, golfers_list=golfers_list)


@app.route('/golf/scorecard/<string:course_name>/<int:enter_timestamp>')
def round(course_name, enter_timestamp):
    scores = [score.json() for score in ScoreModel.find_round_by_enter_timestamp(enter_timestamp)]
    p1_scores = [score['score'] for score in scores if score['golfer_id'] == 1]
    p2_scores = [score['score'] for score in scores if score['golfer_id'] == 2]
    p3_scores = [score['score'] for score in scores if score['golfer_id'] == 3]
    p4_scores = [score['score'] for score in scores if score['golfer_id'] == 4]
    course = CourseModel.find_by_id(scores[0]['course_id']).json()
    holes = [hole.json() for hole in HoleModel.find_by_course(course['id'])]
    date = [score['round_timestamp'] for score in scores][0].strftime('%m/%d/%Y')
    round = {'p1_scores': p1_scores,
            'p2_scores': p2_scores,
            'p3_scores': p3_scores,
            'p4_scores': p4_scores,
            'course name': course['name'],
            'city': course['city'],
            'state': course['state'],
            'slope': course['slope'],
            'hole_numbers': [hole['hole_number'] for hole in holes],
            'distance': [hole['distance'] for hole in holes],
            'par': [hole['par'] for hole in holes],
            'handicap': [hole['handicap'] for hole in holes]}

    return render_template('submitted_scorecard.jinja2', round=round)


@app.route('/golf/golfers')
def golfers():
    golfers_list = [golfer for golfer in GolferModel.find_all()]
    return render_template("golfers.jinja2", golfers_list=golfers_list)


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
