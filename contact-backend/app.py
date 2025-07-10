from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# --- CONFIGURE MAIL SETTINGS ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

# --- ROUTE TO HANDLE FORM SUBMISSION ---
@app.route('/contact', methods=['POST'])
def contact():
    data = request.form if request.form else request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'No data received.'}), 400

    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    if not all([name, email, subject, message]):
        return jsonify({'status': 'error', 'message': 'All fields are required.'}), 400

    msg = Message(
        subject=f"New Contact: {subject}",
        sender=email,
        recipients=[app.config['MAIL_USERNAME']],
        body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    )
    try:
        mail.send(msg)
        return jsonify({'status': 'success', 'message': 'Email sent!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
