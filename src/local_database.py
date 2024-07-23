# create database for running the website locally

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(100), nullable=False)
    dimensions = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String(100), nullable=True)

with app.app_context():
    db.drop_all()
    db.create_all()

# Add to list and run script again to update database.
product_list = [
    Product(product_name='Backpack', price=60, color='French Blue & White w/ Adjustable Straps', dimensions='D = 7 3/4" H = 9" W = 10"', category='Bags', image_path='../css/images/products/Backpack Navy-White/Backpack-7.png'),
    Product(product_name='Bucket Bag', price=50, color='Mint Green & White w/ Detachable Straps', dimensions='D = 7 1/4" H = 10 1/2" W = 11 1/2"', category='Bags', image_path='../css/images/products/Bucket Bag Blue-White/Bucket Bag-1.png'),
    Product(product_name='Bucket Bag', price=50, color='Dark & Lt Grey', dimensions='D = 7 1/4" H = 9" W = 11"', category='Bags', image_path='../css/images/products/Bucket Bag Grey/Bucket Bag-10.png'),
    Product(product_name='Bucket Bag', price=40, color='Peach', dimensions='D = 8" H = 7" W = 10"', category='Bags', image_path='../css/images/products/Bucket Bag Pink/Bucket Bag-3.png'),
    Product(product_name='Bucket Bag', price=50, color='Pink & White', dimensions='D = 8 3/4" H = 9" W = 10 1/2"', category='Bags', image_path='../css/images/products/Bucket Bag Pink-White/Bucket Bag-2.png'),
    Product(product_name='Bucket Bag', price=50, color='Tan & Brown w/ Detachable Straps', dimensions='D = 8 1/2" H = 10 1/4" W = 12"', category='Bags', image_path='../css/images/products/Bucket Bag Tan-Brown/Bucket Bag-8.png'),
    Product(product_name='Bucket Bag', price=40, color='Forest Green & White', dimensions='D = 10" H = 9" W = 11 1/2"', category='Bags', image_path='../css/images/products/Bucket Bag White-Green/Bucket Bag-11.png'),
    Product(product_name='Bucket Bag', price=40, color='Grey & White', dimensions='D = 10" H = 8 1/2" W = 11"', category='Bags', image_path='../css/images/products/Bucket Bag White-Grey/Bucket Bag-14.png'),
    Product(product_name='Bucket Bag', price=45, color='White & Purple w/ Adjustable and Detachable Straps', dimensions='D = 7" H = 8 1/2" W = 9"', category='Bags', image_path='../css/images/products/Bucket Bag White-Purple/Bucket Bag-12.png'),
    Product(product_name='Bucket Bag', price=50, color='Peach & White w/ Detachable Straps', dimensions='D = 8" H = 9 1/2" W = 11"', category='Bags', image_path='../css/images/products/Bucket Bag White-Salmon/Bucket Bag-5.png'),
    Product(product_name='Bucket Bag', price=45, color='White & Mint Green', dimensions='D = 8" H = 9" W = 11"', category='Bags', image_path='../css/images/products/Bucket Bag White-Teal/Bucket Bag-13.png'),
    Product(product_name='Bucket Bag', price=40, color='White & Mint Green', dimensions='D = 7 3/4" H = 8 1/2" W = 10"', category='Bags', image_path='../css/images/products/Bucket Bag White-Teal2/Bucket Bag-15.png'),
    Product(product_name='Bucket Bag', price=40, color='Yellow & White w/ Detachable Straps', category='Bags'),
    Product(product_name='Kids Bag', price=10, color='Mint Green w/ White Ribbon', category='Other Bags', image_path='../css/images/products/Kid Bag Teal-White/Kid Bag-6.png'),
    Product(product_name='Mini Bucket Bag', price=30, color='Coral', category='Other Bags', image_path='../css/images/products/Mini Bucket Bag Pink/D1E158A2-77C3-422A-BD1D-19A6F4B35194_1_105_c.jpeg'),
    Product(product_name='Small Tote Bag', price=35, color='Peach & Ecru', category='Other Bags', image_path='../css/images/products/Mini Bucket Bag Pink-White/Bucket Bag-16.png'),
    Product(product_name='Large Tote Bag', price=65, color='Ecru w/ Polka Dots', category='Other Bags', image_path='../css/images/products/Tote Bag Polka/Tote Bag-18.png'),
    Product(product_name='Wristlet', price=35, color='Grey w/ Key Charm', category='Other Bags', image_path='../css/images/products/Wristlet Grey/Wristlet-17.png'),
    Product(product_name='Wristlet', price=30, color='Lime Green', category='Other Bags', image_path='../css/images/products/Wristlet Lime/Wristlet-4.png'),
    Product(product_name='Wristlet', price=40, color='Watermelon w/ Key Charm', category='Other Bags', image_path='../css/images/products/Wristlet Watermelon/04D8C30D-8500-4C98-B485-E0000AB9C585_1_105_c.jpeg'),
    Product(product_name='Bucket Hat', price=40, color='Brown w/ Tan Designs', category='Hats', image_path='../css/images/products/Bucket Hat Brown-Tan/Screenshot 2023-10-04 at 11.24.42 AM.png'),
    Product(product_name='Bucket Hat', price=40, color='Grey w/ Designs', category='Hats', image_path='../css/images/products/Bucket Hat Grey/Screenshot 2023-10-04 at 11.23.42 AM.png'),
    Product(product_name='Bucket Hat', price=50, color='Grey w/ Pink Flowers', category='Hats', image_path='../css/images/products/Bucket Hat Grey-Pink/Screenshot 2023-10-04 at 11.16.21 AM.png'),
    Product(product_name='Bucket Hat', price=30, color='Grey & White', category='Hats', image_path='../css/images/products/Bucket Hat Grey-White/Screenshot 2023-10-04 at 11.15.38 AM.png'),
    Product(product_name='Bucket Hat', price=30, color='Navy Blue', category='Hats', image_path='../css/images/products/Bucket Hat Navy/Screenshot 2023-10-04 at 11.18.58 AM.png'),
    Product(product_name='Bucket Hat', price=35, color='Purple & White', category='Hats', image_path='../css/images/products/Bucket Hat Purple-White/Screenshot 2023-10-04 at 11.22.34 AM.png'),
    Product(product_name='Bucket Hat', price=40, color='Red & White Flowers', category='Hats', image_path='../css/images/products/Bucket Hat Red-White/Screenshot 2023-10-04 at 11.19.51 AM.png')
]

with app.app_context():
    for product in product_list:
        existing_product = Product.query.filter_by(product_name=product.product_name, color=product.color).first()
        if existing_product is None:
            new_product = Product(product_name=product.product_name, price=product.price, 
                                  color=product.color, dimensions=product.dimensions, category=product.category, image_path=product.image_path)
            db.session.add(new_product)
            print(f'Product {product.product_name} - {product.color} added.')

    db.session.commit()