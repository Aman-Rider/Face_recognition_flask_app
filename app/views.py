from flask import render_template, redirect, request, url_for
import os

UPLOAD_FOLDER = 'static/uploads'
def base():
    return render_template('base.html')

def index():
    return render_template("index.html")

def faceapp():
    return render_template("faceapp.html")


def gender():
    if request.method =='POST':
        f= request.files['image']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)
    return render_template("gender.html")