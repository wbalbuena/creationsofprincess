from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='css')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

from database import init_db, Product
db = init_db(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/products")
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()