from crypt import methods
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scrape import popular_release


# initializing flask app
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    pass
