from flask import Blueprint, render_template, request, flash
from .models import Products
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@views.route('/isop', methods=['GET', 'POST'])
def isop():
    product_data = Products.query.all()
    return render_template("isop.html", product_data=product_data)

'''
@views.route('/admin')
def admin():
    return render_template("admin.html")
'''