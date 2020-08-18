from db import db

class CourseModel(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    state = db.Column(db.String(80))
    slope = db.Column(db.Float(precision=1))

#    holes = db.relationship('HoleModel', lazy='dynamic')


    def __init__(self, name, city, state, slope):
        self.name = name
        self.city = city
        self.state = state
        self.slope = slope

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
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
