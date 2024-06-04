from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_marshmallow import Marshmallow
from flask_restx import Api, Resource


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_db.db"
app.config['FLASK_ADMIN_SWATCH'] = 'sandstone'
app.config['SECRET_KEY'] = 'the random string'
admin = Admin(app, name='flask app', template_mode='bootstrap4')
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
api = Api(app)


@app.route('/home')
def hello_world():
    return render_template('home.html')


class Shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    address = db.Column(db.String, unique=True, nullable=False)
    visit_time = db.Column(db.String)
    phone = db.Column(db.String)


@api.route('/shops_list', endpoint='shops_list')
class ShopsList(Resource):
    def get(self):
        list_schema = ShopsSchema(many=True)
        return list_schema.dump(Shops.query.all()), 200


class ShopsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Shops


with app.app_context():
    db.create_all()

admin.add_view(ModelView(Shops, db.session))

# app.run()     #  * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
