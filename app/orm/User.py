import werkzeug
model:User

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(164))
    #密码不允许明文存储
    password_hash = db.Column(db.String(164))

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    #对用户传入的明文密码进行加密
    @property
    def password(self):
        """
        password属性函数
        不允许直接读取原始值
        """
        return "密码不是可读形式！"

    @password.setter
    def password(self, password):
        """
        设置密码hash值
        """
        self.password_hash = werkzeug.security.generate_password_hash(password)

    def verify_password(self, password):
        """
        将用户输入的密码加密后与数据库对比
        """
        return werkzeug.security.generate_password_hash(password)