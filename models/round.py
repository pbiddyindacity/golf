from db import db

class RoundModel(db.Model):
    __tablename__ = 'rounds'
    id = db.Column(db.Integer, primary_key=True)
    golfer_id = db.Column(db.Integer, db.ForeignKey('golfers.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    round_type = db.Column(db.Integer)
    round_timestamp = db.Column(db.Integer)
    enter_timestamp = db.Column(db.Integer)
    hole_1 = db.Column(db.Integer)
    hole_2 = db.Column(db.Integer)
    hole_3 = db.Column(db.Integer)
    hole_4 = db.Column(db.Integer)
    hole_5 = db.Column(db.Integer)
    hole_6 = db.Column(db.Integer)
    hole_7 = db.Column(db.Integer)
    hole_8 = db.Column(db.Integer)
    hole_9 = db.Column(db.Integer)
    hole_10 = db.Column(db.Integer)
    hole_11 = db.Column(db.Integer)
    hole_12 = db.Column(db.Integer)
    hole_13 = db.Column(db.Integer)
    hole_14 = db.Column(db.Integer)
    hole_15 = db.Column(db.Integer)
    hole_16 = db.Column(db.Integer)
    hole_17 = db.Column(db.Integer)
    hole_18 = db.Column(db.Integer)
    golfer = db.relationship('GolferModel')
    course = db.relationship('CourseModel')

    def __init__(self, golfer_id, course_id, round_type,
                 round_timestamp, enter_timestamp,
                 hole_1, hole_2, hole_3, hole_4, hole_5, hole_6,
                 hole_7, hole_8, hole_9, hole_10, hole_11, hole_12,
                 hole_13, hole_14, hole_15, hole_16, hole_17, hole_18):
        self.golfer_id = golfer_id
        self.course_id = course_id
        self.round_type = round_type
        self.round_timestamp = round_timestamp
        self.enter_timestamp = enter_timestamp
        self.hole_1 = hole_1
        self.hole_2 = hole_2
        self.hole_3 = hole_3
        self.hole_4 = hole_4
        self.hole_5 = hole_5
        self.hole_6 = hole_6
        self.hole_7 = hole_7
        self.hole_8 = hole_8
        self.hole_9 = hole_9
        self.hole_10 = hole_10
        self.hole_11 = hole_11
        self.hole_12 = hole_12
        self.hole_13 = hole_13
        self.hole_14 = hole_14
        self.hole_15 = hole_15
        self.hole_16 = hole_16
        self.hole_17 = hole_17
        self.hole_18 = hole_18

    def json(self):
        return {
            'id': self.id,
            'golfer_id': self.id,
            'course_id': self.id,
            'round_type': self.id,
            'round_timestamp': self.id,
            'enter_timestamp': self.id,
            'hole_1': self.hole_1,
            'hole_2': self.hole_2,
            'hole_3': self.hole_3,
            'hole_4': self.hole_4,
            'hole_5': self.hole_5,
            'hole_6': self.hole_6,
            'hole_7': self.hole_7,
            'hole_8': self.hole_8,
            'hole_9': self.hole_9,
            'hole_10': self.hole_10,
            'hole_11': self.hole_11,
            'hole_12': self.hole_12,
            'hole_13': self.hole_13,
            'hole_14': self.hole_14,
            'hole_15': self.hole_15,
            'hole_16': self.hole_16,
            'hole_17': self.hole_17,
            'hole_18': self.hole_18
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
