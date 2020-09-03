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

        distance_list = []
        handicap_list = []
        par_list = []

        for i in range(1, 19):
            distance_str = "h" + str(i) + "d"
            handicap_str = "h" + str(i) + "h"
            par_str = "h" + str(i) + "p"
            distance_list.append(int(request.form.get(distance_str)))
            handicap_list.append(int(request.form.get(handicap_str)))
            par_list.append(int(request.form.get(par_str)))
            hole = HoleModel(course.id, i, par_list[i - 1], handicap_list[i - 1], distance_list[i - 1])
            hole.save_to_db()

        course_dict = {
            'name': name,
            'city': city,
            'state': state,
            'slope': slope,
            'distance': {
                'hole_distances': distance_list,
                'front_9_distance': sum(distance_list[:9]),
                'back_9_distance': sum(distance_list[9:]),
                'total_distance': sum(distance_list)
            },
            'handicap': {
                'hole_handicaps': handicap_list,
                'front_9_handicap': sum(handicap_list[:9]),
                'back_9_handicap': sum(handicap_list[9:]),
                'total_handicap': sum(handicap_list)
            },
            'par': {
                'hole_pars': par_list,
                'front_9_par': sum(par_list[:9]),
                'back_9_par': sum(par_list[9:]),
                'total_par': sum(par_list)
            }
        }

        return render_template('course_scorecard.jinja2', course_dict=course_dict)

    return render_template('blank_scorecard.jinja2')


@app.route('/golf/scorecard/<string:name>', methods=['GET', 'POST'])
def course_scorecard(name):
    if name == 'new':
        return redirect(url_for('create_course'))
    course = CourseModel.find_by_name(name)
    course_details = course.json()
    _id = course_details['id']
    city = course_details['city']
    state = course_details['state']
    slope = course_details['slope']
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

    if request.method == "POST":
        course = CourseModel.find_by_name(name)
        course_details = course.json()
        course_name = name
        course_id = course_details['id']
        round_date = request.form.get('round_date')
        round_datetime = datetime.strptime(round_date, '%Y-%m-%d')
        round_datetime = round_datetime.astimezone(pytz.utc)
        round_string = round_datetime.strftime('%Y%m%d%H%M%S')
        enter_datetime = datetime.now(tz=pytz.utc)
        enter_string = enter_datetime.strftime('%Y%m%d%H%M%S')

        for p in range(1, 5):
            front_9_count = back_9_count = 0
            round_scores = []
            golfer_string = "golfer_" + str(p)
            name = request.form.get(golfer_string)
            player = GolferModel.find_by_name(name)
            if player:
                details = player.json()
                _id = details['id']
                for h in range(1, 19):
                    hole_string = "p" + str(p) + "_hole_" + str(h) + "_score"
                    hole_score = request.form.get(hole_string)
                    round_scores.append(hole_score)
                    score = round_scores[h - 1]
                    if score == '':
                        score = 0
                    else:
                        score = int(score)

                    if h < 10 and score != 0:
                        front_9_count += 1
                    elif h >= 10 and score != 0:
                        back_9_count += 1

                    player_score = ScoreModel(course_id, _id, h, score, p, round_string, enter_string)
                    player_score.save_to_db()

        return redirect(url_for('round', course_name=course_name, enter_string=enter_string))

    golfers_list = [golfer for golfer in GolferModel.find_all()]
    course_dict = {
        'name': name,
        'city': city,
        'state': state,
        'slope': slope,
        'distance': {
            'hole_distances': distance_list,
            'front_9_distance': sum(distance_list[:9]),
            'back_9_distance': sum(distance_list[9:]),
            'total_distance': sum(distance_list)
        },
        'handicap': {
            'hole_handicaps': handicap_list,
            'front_9_handicap': sum(handicap_list[:9]),
            'back_9_handicap': sum(handicap_list[9:]),
            'total_handicap': sum(handicap_list)
        },
        'par': {
            'hole_pars': par_list,
            'front_9_par': sum(par_list[:9]),
            'back_9_par': sum(par_list[9:]),
            'total_par': sum(par_list)
        }
    }
    return render_template('course_scorecard.jinja2', course_dict=course_dict, golfers_list=golfers_list)


@app.route('/golf/scorecard/<string:course_name>/<string:enter_string>')
def round(course_name, enter_string):

    scores_dict = {'p1': {'name': '', 'score_list': '', 'front_9': '', 'back_9': '', 'total': ''},
                   'p2': {'name': '', 'score_list': '', 'front_9': '', 'back_9': '', 'total': ''},
                   'p3': {'name': '', 'score_list': '', 'front_9': '', 'back_9': '', 'total': ''},
                   'p4': {'name': '', 'score_list': '', 'front_9': '', 'back_9': '', 'total': ''}
                   }
    score_styles = {'p1': [],
                   'p2': [],
                   'p3': [],
                   'p4': []
                   }

    scores = [score.json() for score in ScoreModel.find_round_by_enter_string(enter_string)]
    course = CourseModel.find_by_id(scores[0]['course_id']).json()
    holes = [hole.json() for hole in HoleModel.find_by_course(course['id'])]
    round_date = [score['round_string'] for score in scores][0]
    date = datetime.strptime(round_date, '%Y%m%d%H%M%S')
    round_date = date.strftime('%m/%d/%Y')
    distance = [hole['distance'] for hole in holes]
    par = [hole['par'] for hole in holes]

    for i in range(1, 5):
        styles_list = []
        for score in scores:
            if score['scorecard_position'] == i:
                name = score['golfer'].name
                round_scores = [score['score'] for score in scores if score['scorecard_position'] == i]
                front_9 = sum(round_scores[:9])
                back_9 = sum(round_scores[9:])
                total = sum(round_scores)
        for q in range(len(round_scores)):
            if round_scores[q] == 0:
                round_scores[q] = ''
                styles_list.append("par")
            else:
                if round_scores[q] - par[q] <= -2:
                    styles_list.append("eagle")
                elif round_scores[q] - par[q] == -1:
                    styles_list.append("birdie")
                elif round_scores[q] - par[q] == 0:
                    styles_list.append("par")
                elif round_scores[q] - par[q] == 1:
                    styles_list.append("bogey")
                elif round_scores[q] - par[q] == 2:
                    styles_list.append("double-bogey")
                elif round_scores[q] - par[q] >= 3:
                    styles_list.append("triple-bogey")

                if name is not None and scores is not None:
                    player_string = "p" + str(i)
                    scores_dict[player_string] = {
                        'name': name,
                        'score_list': round_scores,
                        'front_9': front_9,
                        'back_9': back_9,
                        'total': total
                    }
                    score_styles[player_string] = {
                        'styles': styles_list
                    }

        name = round_scores = front_9 = back_9 = total = None

    round = {
        'scores': scores_dict,
        'score_styles': score_styles,
        'date': round_date,
        'course': {
            'name': course_name,
            'city': course['city'],
            'state': course['state'],
            'slope': course['slope'],
            'distance': {
                'hole_distances': distance,
                'front_9_distance': sum(distance[:9]),
                'back_9_distance': sum(distance[9:]),
                'total_distance': sum(distance)
            },
            'par': {
                'hole_pars': par,
                'front_9_par': sum(par[:9]),
                'back_9_par': sum(par[9:]),
                'total_par': sum(par)
            },
            'handicap': [hole['handicap'] for hole in holes],
        }

    }
#    return round
    return render_template('submitted_scorecard.jinja2', round=round)


@app.route('/golf/golfers')
def golfers():
    golfers_list = [golfer for golfer in GolferModel.find_all()]
    return render_template("golfers.jinja2", golfers_list=golfers_list)


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
