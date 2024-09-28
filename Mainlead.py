import http.client
import json
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import auto_py_to_exe

conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

def chat_about_fragrances(question):
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful and knowledgeable fragrance expert."},
            {"role": "user", "content": question}
        ],
        "web_access": False
    }

    headers = {
        'x-rapidapi-key': "abf60d6769msh5066b8a2895cb64p1e58bajsn326511ef8429",
        'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    conn.request("POST", "/gpt4", json.dumps(payload), headers)
    res = conn.getresponse()
    data = res.read()

    response = json.loads(data.decode("utf-8"))

    # Print the raw response for debugging (optional)
    print("Raw API response:", response)

    try:
        # Extract and print the assistant's response from the 'result' key
        assistant_response = response['result']
        print(assistant_response)
        return assistant_response  # Return the response for potential emailing
    except KeyError:
        print("Error: 'result' key not found in the API response. Please check the API documentation or response format.")
        return None  # Return None in case of an error

def send_email(recipient_email, subject, body):
    # Retrieve email credentials from environment variables
    sender_email = os.environ.get("EMAIL_ADDRESS1")  # Use the correct environment variable name
    password = os.environ.get("EMAIL_PASSWORD1")  # Use the correct environment variable name

    if not sender_email or not password:
        print("Error: Email credentials not found in environment variables.")
        return

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Adjust if using a different email provider
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

# Function to get user input, call chat_about_fragrances, and optionally send email
def get_user_question():
    while True:
        question = input("Enter your fragrance question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        response = chat_about_fragrances(question)
        if response:  # Only ask to email if there's a valid response
            send_email_choice = input("Do you want to email this response? (yes/no): ")
            if send_email_choice.lower() == 'yes':
                recipient_email = input("Enter the recipient email address: ")
                subject = "Fragrance Recommendation"
                send_email(recipient_email, subject, response)

# Example usage with pre-defined questions and user input
chat_about_fragrances("What are some popular fragrances for men?")
chat_about_fragrances("Can you recommend a fragrance for a summer evening date?")

# Get user input and continue chatting
get_user_question()
