from flask import Blueprint, render_template ,request, redirect, url_for, flash , Flask

main = Blueprint('main', __name__)

main.secret_key = '220225012@rajoihskj'

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    phone = request.form.get('phone')
    Link = request.form.get('linkedin')

    # Check if data is received
    print(f"Name: {name}, Email: {email}, Message: {message}, Phone: {phone},Link: {Link}")

    return redirect(url_for('main.home'))