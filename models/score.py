from db import db

class ScoreModel(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    golfer_id = db.Column(db.Integer, db.ForeignKey('golfers.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    hole_number = db.Column(db.Integer, db.ForeignKey('holes.hole_number'))
    round_type = db.Column(db.Integer)
    round_timestamp = db.Column(db.Integer)
    enter_timestamp = db.Column(db.Integer)

    golfer = db.relationship('GolferModel')
    course = db.relationship('CourseModel')

    def __init__(self, golfer_id, course_id, round_type,
                 round_timestamp, enter_timestamp):
        self.golfer_id = golfer_id
        self.course_id = course_id
        self.hole_number = hole_number
        self.round_type = round_type
        self.round_timestamp = round_timestamp
        self.enter_timestamp = enter_timestamp


    def json(self):
        return {
            'id': self.id,
            'golfer_id': self.id,
            'course_id': self.id,
            'hole_number': self.hole_number,
            'round_type': self.id,
            'round_timestamp': self.id,
            'enter_timestamp': self.id,
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
