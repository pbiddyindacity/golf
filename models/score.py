from db import db

class ScoreModel(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    golfer_id = db.Column(db.Integer, db.ForeignKey('golfers.id'))
    hole_number = db.Column(db.Integer, db.ForeignKey('holes.hole_number'))
    score = db.Column(db.Integer)
    round_type = db.Column(db.Integer)
    round_timestamp = db.Column(db.DateTime)
    enter_timestamp = db.Column(db.DateTime)

    golfer = db.relationship('GolferModel')
    course = db.relationship('CourseModel')
    hole = db.relationship('HoleModel')

    def __init__(self, course_id, golfer_id, hole_number, score, round_type,
                 round_timestamp, enter_timestamp):
        self.course_id = course_id
        self.golfer_id = golfer_id
        self.score = score
        self.hole_number = hole_number
        self.round_type = round_type
        self.round_timestamp = round_timestamp
        self.enter_timestamp = enter_timestamp


    def json(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'golfer_id': self.golfer_id,
            'score': self.score,
            'hole_number': self.hole_number,
            'round_type': self.round_type,
            'round_timestamp': self.round_timestamp,
            'enter_timestamp': self.enter_timestamp
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_round_by_enter_timestamp(cls, enter_timestamp):
        return cls.query.filter_by(enter_timestamp=enter_timestamp).all()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
