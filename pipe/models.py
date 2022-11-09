from datetime import datetime
from pipe import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False, unique=True)
    roles = db.relationship('Role', secondary='user_roles')
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
    
    
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

db.create_all()