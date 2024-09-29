# Fragrance Chatbot with Email Functionality www.askfragranceai.com

This project is a Python-based web application that allows you to interact with a fragrance expert AI and get recommendations on various fragrances. It also provides the option to email the responses.

Features
Chatbot Interaction (Implemented):

Ask questions about fragrances through a web interface.
Receive informative and helpful responses from the AI fragrance expert.
Email Functionality (Implemented):

Option to send the chatbot's responses via email directly from the web interface.
The user can provide their email address to receive the response.
Progress
Basic Flask App (Implemented):

A Flask web application has been set up with routes to handle user interactions and AJAX requests.
An index.html template provides the basic user interface for the chatbot.
Dynamic Response Display (Pending):

AJAX functionality is yet to be implemented to update the chatbot's responses without requiring a full page reload.
Error Handling (Partially Implemented):

Basic error handling is in place for API response issues and missing email credentials.
More robust error handling for other potential issues can be added in the future.
Next Steps
Implement AJAX: Add AJAX functionality to the index.html template and Flask routes to provide a smoother and more interactive user experience.
Enhance Error Handling: Improve error handling to provide more informative feedback to the user in case of various errors.
Styling and UI/UX Improvements: Use CSS and potentially JavaScript to enhance the visual appearance and user experience of the chatbot interface.
Testing and Debugging: Thoroughly test the application for different scenarios and fix any bugs or issues.
Deployment: Once the application is fully functional and tested, deploy it to a web server so it can be accessed publicly.
Prerequisites (unchanged)
Python 3.x
Required Libraries: requests, smtplib, Flask
API Key: from a service like RapidAPI
Email Credentials: (if using email functionality)
How to Run (updated)
Set Up Environment Variables (Optional):

If using email functionality, set EMAIL_ADDRESS1 and EMAIL_PASSWORD1
Run the Script:

Execute the script from your terminal:
Bash
set FLASK_APP=Mainlead.py  # On Windows
export FLASK_APP=Mainlead.py  # On macOS/Linux
flask run
Use code with caution.


Monetization
PayPal Donations (Implemented): Allow users to support the development of the AI through PayPal donations.
Google AdSense Ads (Implemented): Display targeted ads to generate additional revenue.



