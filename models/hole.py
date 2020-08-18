from db import db

class HoleModel(db.Model):
    __tablename__ = 'holes'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    hole_number = db.Column(db.Integer)
    par = db.Column(db.Integer)
    handicap = db.Column(db.Integer)
    distance = db.Column(db.Integer)

    course = db.relationship('CourseModel')

    def __init__(self, course_id, hole_number, par, handicap, distance):
        self.course_id = course_id
        self.hole_number = hole_number
        self.par = par
        self.handicap = handicap
        self.distance = distance

    def json(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'hole_number': self.hole_number,
            'par': self.par,
            'handicap': self.handicap,
            'distance': self.distance
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_course_hole(cls, course_id, hole_number):
        return cls.query.filter_by(course_id=course_id, hole_number=hole_number).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
