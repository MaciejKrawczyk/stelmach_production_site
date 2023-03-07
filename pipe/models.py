from datetime import datetime
from pipe import db, app


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False, unique=True)
    role = db.Column(db.String(180), nullable=False)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    
    
class GoFutureTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(200), nullable=False, default='f')
    date = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), nullable=False)
    gold_color_type = db.Column(db.String(200), nullable=False)
    order_id = db.Column(db.String(200), nullable=False)
    pipe = db.Column(db.String(200), nullable=True)
    program = db.Column(db.String(200), nullable=True)
    r50 = db.Column(db.Float, nullable=False)
    r51 = db.Column(db.Float, nullable=False)
    r52 = db.Column(db.Float, nullable=False)
    r60 = db.Column(db.Float, nullable=False)
    r40 = db.Column(db.Float, nullable=False)
    r61 = db.Column(db.Float, nullable=False)
    r41 = db.Column(db.Float, nullable=False)
    r20 = db.Column(db.Float, nullable=False)
    p1 = db.Column(db.Float, nullable=False)
    p2 = db.Column(db.Float, nullable=False)
    p3 = db.Column(db.Float, nullable=False)
    p5 = db.Column(db.Float, nullable=False)
    code = db.Column(db.String(10000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'"Order {self.id}"'

# --------------TOOLS---------------


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    date = db.Column(db.DateTime, default=(datetime.now))
    what_happened = db.Column(db.String(300), nullable=True)
    position_id = db.Column(db.Integer, nullable=False)


class Tools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    width = db.Column(db.String(200), nullable=True)
    angle = db.Column(db.String(200), nullable=True)
    radius = db.Column(db.String(200), nullable=True)
    company = db.Column(db.String(200), nullable=False)
    id_position = db.Column(db.Integer, nullable=False)
    shelf = db.Column(db.Integer, nullable=True)
    shelf_type = db.Column(db.Integer, nullable=True)
    id_dup = db.Column(db.Integer, nullable=False)


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    pretty_name = db.Column(db.String(200), nullable=True)


# Creates database tables, important!
with app.app_context():
    db.create_all()

