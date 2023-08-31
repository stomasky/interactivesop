from flask import Flask, Blueprint, render_template, request, redirect, flash, url_for
from . import db
from .models import db,Products
from flask_sqlalchemy import SQLAlchemy

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        password = request.form.get('password')

        if password == 'interactiveSOP':
            return redirect(url_for('views.isop'))
        else:
            flash('Incorrect Password/Contraseña Incorrecta', category='error')

    return render_template("login.html")

@auth.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        SKU = request.form.get('SKU')
        channel = request.form.get('channel')
        container = request.form.get('container')
        units_per_container = request.form.get('units_per_container')
        box_size = request.form.get('box_size')
        bag_y_n = request.form.get('bag_y_n')
        bag_size = request.form.get('bag_size')
        sprayer_cap = request.form.get('sprayer_cap')

        new_product = Products(
            SKU = SKU,
            channel = channel,
            SKUchannel = str(SKU)+str(channel),
            container = container,
            units_per_container = units_per_container,
            box_size = box_size,
            bag_y_n = bag_y_n,
            bag_size = bag_size,
            sprayer_cap = sprayer_cap)
        
        db.session.add(new_product)
        db.session.commit()
        flash('Product Added: '+ SKU + ' for ' + channel, category='success')

    return render_template("admin.html")

@auth.route('/isop', methods=['GET', 'POST'])
def isop():

    return render_template("isop.html")