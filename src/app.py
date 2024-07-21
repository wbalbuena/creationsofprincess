from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# "mysql+mysqldb://{username}:{password}@{hostname}/{databasename}"
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://wbalbuena:NTC7cur6jvg*gzd-rxg@wbalbuena.mysql.pythonanywhere-services.com/wbalbuena$default"

# For running locally:
# SQLALCHEMY_DATABASE_URI = 'sqlite:///products.db'

app = Flask(__name__, template_folder='templates', static_folder='css')

# pool_recycle - how long a database connection can be left unused before discarded
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle':280}

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(100), nullable=False)
    dimensions = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String(100), nullable=False)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/products")
def products():
    return render_template('products.html', products=Product.query.all())

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()