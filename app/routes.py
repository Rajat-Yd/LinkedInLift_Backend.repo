from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import ContactMessage  # Import the ContactMessage model
from flask_mail import Message  # Import the database instance
from app import db, mail

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

        send_confirmation_email(email)

        # Flash a success message (if you want to notify the user)
        flash("Thank you! Your message has been submitted successfully.")

        # Redirect to a thank-you page or home
        return redirect(url_for('main.thank_you'))

    # Render the contact form for GET requests
    return render_template('index.html')

def send_confirmation_email(user_email):
    # Create the confirmation email
    msg = Message('Thank You for Contacting Us',
                  recipients=[user_email])  # recipient's email address
    msg.body = 'Thank you for reaching out to us. We will get back to you soon!'
    try:
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

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
