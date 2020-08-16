from db import db

class CourseModel(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    state = db.Column(db.String(80))
    zip_code = db.Column(db.Integer)
    slope = db.Column(db.Float(precision=1))
#    rounds = db.relationship('RoundModel', lazy='dynamic')

    def __init__(self, name, city, state, zip_code, slope):
        self.name = name
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.slope = slope

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'slope': self.slope
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_city(cls, city):
        return cls.query.filter_by(city=city).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
