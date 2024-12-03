from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import ContactMessage  # Import the ContactMessage model
from app import db  # Import the database instance
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Flask email configuration from environment variables
SENDER_EMAIL = os.getenv("MAIL_USERNAME")
SENDER_PASSWORD = os.getenv("MAIL_PASSWORD")
SMTP_SERVER = os.getenv("MAIL_SERVER")
SMTP_PORT = int(os.getenv("MAIL_PORT"))
SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

# Admin email for notifications
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

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

        try:
            send_admin_notification(name, email, message, phone, linkedin)
            send_confirmation_email(name, email)
        except Exception as e:
            print(f"Error sending email: {e}")

        # Flash a success message (if you want to notify the user)
        flash("Thank you! Your message has been submitted successfully.")

        # Redirect to a thank-you page or home
        return redirect(url_for('main.thank_you'))

    # Render the contact form for GET requests
    return render_template('index.html')


def send_admin_notification(name, email, message, phone=None, linkedin=None):
    subject = f"New Contact Form Submission from {name}"

    # Email Body
    email_body = f"""
    <html>
    <body>
        <h3 style="color: #FF5733;">New Contact Form Submission</h3>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Message:</strong> {message}</p>
        <p><strong>Phone:</strong> {phone if phone else 'N/A'}</p>
        <p><strong>LinkedIn:</strong> {linkedin if linkedin else 'N/A'}</p>
    </body>
    </html>
    """

    # Set up MIME message
    msg = MIMEText(email_body, 'html')  # 'html' specifies the content type
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ADMIN_EMAIL

    # Send the email
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, ADMIN_EMAIL, msg.as_string())
            print("Admin notification email sent successfully!")
    except Exception as e:
        print(f"Error sending admin notification email: {e}")


def send_confirmation_email(name, recipient_email):
    subject = "Thank you for contacting LinkedInLift!"

    # Email Body with Personalization
    email_body = f"""
    <html>
    <body>
        <h2 style="color: #0077B5;">Hi {name},</h2>
        <p>Thank you for reaching out to LinkedInLift! We have received your message and will get back to you soon.</p>
        <p>If you have any further questions, feel free to reply to this email.</p>
        <p style="color: #0077B5;">Best Regards,<br>LinkedInLift Team</p>
    </body>
    </html>
    """

    # Set up MIME message
    msg = MIMEText(email_body, 'html')  # 'html' specifies the content type
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email

    # Send the email
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
            print("Confirmation email sent successfully!")
    except Exception as e:
        print(f"Error sending confirmation email: {e}")


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
