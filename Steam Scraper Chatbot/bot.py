# Required libaries
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# User defined functions
from scrape import popular_release


# Initializing flask app
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    # Getting user message and Creating response instance
    incoming_msg = request.values.get('Body', '').lower()
    bot_response = MessagingResponse()
    bot_message = bot_response.message()

    if incoming_msg == "hello":
        bot_message.body("Hello, I am Bot!!")

    return str(bot_response)


if __name__ == "__main__":
    app.run(debug=True)
