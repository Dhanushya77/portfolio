# from flask import Flask, render_template
# from flask_mail import Mail, Message

# app = Flask(__name__)
# mail = Mail(app)
# @app.route('/')

# @app.route('/index')
# def index():
#     return render_template('index.html')

# app.run()

from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use Gmail SMTP server
app.config['MAIL_PORT'] = 587  # Port for Gmail SMTP
app.config['MAIL_USE_TLS'] = True  
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'dhanushyavs@gmail.com'
app.config['MAIL_PASSWORD'] = 'pwmr uakz ejtq hjio'  
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Create the email message
        msg = Message(
            subject=f"{name} contacting you via portfolio",
            recipients=['dhanushyavs@gmail.com'], 
            body=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        )

        try:
            # Send the email
            mail.send(msg)
            return redirect(url_for('index'))  # Redirect to homepage after sending the message
        except Exception as e:
            print(f"Error sending email: {e}")
            return "There was an error sending your message. Please try again later."

if __name__ == '__main__':
    app.run(debug=True)
