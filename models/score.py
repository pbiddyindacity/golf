from db import db

class ScoreModel(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    golfer_id = db.Column(db.Integer, db.ForeignKey('golfers.id'))
    hole_number = db.Column(db.Integer, db.ForeignKey('holes.hole_number'))
    score = db.Column(db.Integer)
    round_type = db.Column(db.String)
    scorecard_position = db.Column(db.Integer)
    round_string = db.Column(db.String)
    enter_string = db.Column(db.String)

    golfer = db.relationship('GolferModel')
    course = db.relationship('CourseModel')
    hole = db.relationship('HoleModel')

    def __init__(self, course_id, golfer_id, hole_number, score, round_type, scorecard_position,
                 round_string, enter_string, golfer, course, hole):
        self.course_id = course_id
        self.golfer_id = golfer_id
        self.score = score
        self.hole_number = hole_number
        self.round_type = round_type
        self.scorecard_position = scorecard_position
        self.round_string = round_string
        self.enter_string = enter_string
        self.golfer = golfer
        self.course = course
        self.hole = hole

    def json(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'golfer_id': self.golfer_id,
            'score': self.score,
            'hole_number': self.hole_number,
            'round_type': self.round_type,
            'scorecard_position': self.scorecard_position,
            'round_string': self.round_string,
            'enter_string': self.enter_string,
            'golfer': self.golfer,
            'course': self.course,
            'hole': self.hole
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_round_by_enter_string(cls, enter_string):
        return cls.query.filter_by(enter_string=enter_string).all()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
