import http.client
import json
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request

conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

def chat_about_fragrances(question):
    # ... (Your existing chat_about_fragrances function remains unchanged)

def send_email(recipient_email, subject, body):
    # ... (Your existing send_email function remains unchanged)

# Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        email = request.form.get('email')  # Get email if provided
        response = chat_about_fragrances(question)

        if response and email:  # Send email if response is valid and email is provided
            subject = "Fragrance Recommendation"
            send_email(email, subject, response)

        return render_template('index.html', response=response)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)