import flask-sqlalchemy
import Permission

class Role(db.Model):
    """
    用户角色
    """
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(164))

    default = db.Column(db.Boolean, default=False, index=True)

    permissions = db.Column(db.Integer)

    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        """
        创建用户角色
        """
        roles = {
            #定义了两个用户角色（User， Admin）
            'User' : (Permission.EMPLOYEE, True),
            'Admin' : (Permission.MANAGER | Permission.EMPLOYEE, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
            db.session.commit()