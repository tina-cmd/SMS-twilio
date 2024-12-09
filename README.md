Django SMS Messaging

User: Admin
Pass: admin

Description:
This Django application implements a feature for sending SMS messages. It utilizes a third-party SMS gateway API to send messages to specified phone numbers.
This Django application allows for the management of user names and scores. Based on the score, the application automatically sends an SMS alert using the Twilio API.

How It Works
Users' names and scores are stored in the database using the Message model.
When a Message object is saved:
If the score is 70 or higher, an SMS congratulating the user is sent.
If the score is below 70, an SMS encouraging the user to try again is sent.
The SMS is sent using the Twilio API with predefined credentials.

Key Features
Automatic SMS notifications for scores.
Simple model-based implementation.
Dynamic SMS messages based on user scores.

Example SMS Messages
Passing Score (70 or above):
"Congratulations [Name], your score is [Score]."

Failing Score (Below 70):
"Sorry [Name], your score is [Score]. Try again."

Technologies Used:
Backend Framework: Django
SMS API: (Specify the API, Twilio)
