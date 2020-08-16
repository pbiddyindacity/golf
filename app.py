import os

from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api

from db import db
from models.course import CourseModel
from resources.course import Course, CourseList


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

@app.route('/course/create', methods=['GET', 'POST'])
def create_course():
    if request.method == "POST":
        name = request.form.get('name')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip_code')
        slope = request.form.get('slope')
        course = CourseModel(name, city, state, zip_code, slope)
        course.save_to_db()
        courses_list = course.find_all()
        return render_template('course_created.jinja2', name=name, courses_list=courses_list)

    return render_template('create_course.jinja2')

api.add_resource(CourseList, '/courses')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
