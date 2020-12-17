from flask import Flask, render_template, redirect, flash, request
from mysqlconnection import connectToMySQL
import dotenv
import re
import sys
import os


app = Flask(__name__)
app.SECRET_KEY = os.getenv('APP_SECRET_KEY')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact-form', methods=["POST"])
def add_contact_to_database():
    is_valid = True
    if len(request.form['name']) < 1:
        is_valid = False
        flash("Name is a required field")
    if not request.form['name'].isalpha():
        is_valid = False
        flash("Name can only contain alphabetic chracters")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address!")
    if len(request.form['message']) < 1:
        is_valid = False
        flash ("Must contain message")

    if is_valid:
        query = "INSERT INTO contact (name, email, message, created_at, updated_at) VALUES (%(n)s, %(em)s, %(m)s, NOW(), NOW());"
        data = {
            'n': request.form['name'],
            'em': request.form['email'],
            'm': request.form['message'],
        }
        db = connectToMySQL('devspoint')
        db.query_db(query, data)
        flash("Your message has been sent")

    return redirect("/#contact")

if __name__ == "__main__":
    app.run(debug=True)