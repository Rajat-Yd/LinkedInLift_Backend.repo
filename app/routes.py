from flask import Blueprint, render_template ,request, redirect, url_for, flash , Flask

main = Blueprint('main', __name__)

main.secret_key = 'rajat0911q'

@main.route('/')
def home():
    return render_template("index.html")

# Add this to handle form submissions
@main.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    link = request.form.get('linkedin')
    phone = request.form.get('phone')

    # Debugging to see received data
    print(f"Name: {name}, Email: {email}, Message: {message}, Link: {link}, Phone: {phone}")

    flash("Thank you for reaching out! We'll get back to you soon.")
    return redirect(url_for('index'))