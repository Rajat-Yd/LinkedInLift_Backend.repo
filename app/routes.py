# # from flask import Blueprint, render_template ,request, redirect, url_for, flash , Flask

# # main = Blueprint('main', __name__)

# # main.secret_key = '220225012@rajoihskj'

# # @main.route('/')
# # def home():
# #     return render_template("index.html")

# @main.route('/submit-form', methods=['POST'])
# def submit_form():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     message = request.form.get('message')
#     phone = request.form.get('phone')
#     Link = request.form.get('linkedin')

#     # Check if data is received
#     print(f"Name: {name}, Email: {email}, Message: {message}, Phone: {phone},Link: {Link}")

#     return redirect(url_for('main.home'))

# from flask import Flask, render_template, request, redirect, url_for
# from app.models import ContactMessage
# from app import db

# @app.route('/contact', methods=['POST', 'GET'])
# def contact():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']

#         # Save to the database
#         new_message = ContactMessage(name=name, email=email, message=message)
#         db.session.add(new_message)
#         db.session.commit()

#         # Redirect to a thank-you page
#         return redirect(url_for('thank_you'))

#     return render_template('contact.html')

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import ContactMessage  # Import the ContactMessage model
from app import db  # Import the database instance

# Create the main Blueprint
main = Blueprint('main', __name__)

# Route for the home page
@main.route('/')
def home():
    return render_template("index.html")


# Route for the contact page (GET for displaying form, POST for form submission)
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        phone = request.form.get('phone')  # Optional field
        linkedin = request.form.get('linkedin')  # Optional field

        # Validate form data
        if not name or not email or not message:
            flash("Please fill out all required fields.", "error")
            return redirect(url_for('main.contact'))

        # Debugging: Print data to terminal
        print(f"Name: {name}, Email: {email}, Message: {message}, Phone: {phone}, LinkedIn: {linkedin}")

        # Save to the database
        new_message = ContactMessage(
            name=name,
            email=email,
            message=message,
            phone=phone,
            linkedin=linkedin
        )
        db.session.add(new_message)
        db.session.commit()

        # Flash a success message (if you want to notify the user)
        flash("Thank you! Your message has been submitted successfully.")

        # Redirect to a thank-you page or home
        return redirect(url_for('main.thank_you'))

    # Render the contact form for GET requests
    return render_template('index.html')

# (Optional) Route for a thank-you page
@main.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')  # Create a thank_you.html file in the templates folder

# Route to view all messages (admin feature, optional)
@main.route('/messages')
def view_messages():
    # Fetch all messages from the database
    messages = ContactMessage.query.all()
    return render_template('messages.html', messages=messages)  # Create a messages.html file
