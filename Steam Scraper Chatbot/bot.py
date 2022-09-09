# Required libaries
import re
from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse
from emoji import emojize as em

# User defined functions
from scrape import popular_release, get_steam_image
from utils import get_info

# Initializing flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/bot', methods=['POST'])
def bot():
    # Getting user message and Creating response instance
    incoming_msg = request.values.get('Body', '').lower()
    bot_response = MessagingResponse()
    bot_message = bot_response.message()

    # Bot commands
    command = ['hello', 'hi', 'what do you do', 'start', 'commands']
    bot_commands_list = ['/get_popular_releases', '/get_new_releases', 'get_new_releases',
                         'get_popular_releases', 'get popular releases', 'get new releases']

    # bot navigation and conversation
    if incoming_msg == "hello":  # command:
        # bot_commands = f""" Hello, I am Steam Bot. I Scrape the Steam Game Store Website to get games and more. I Can do anything on the site just search through my commands and hit me {em(':smile:',language='alias')}.
       # These are my commands {em(':robot:',language='alias')}:
       # - /get_popular_releases
       # - /get_new_releases
       # - /get_"""
       # link = 'http://www.africau.edu/images/default/sample.pdf'
      #  y_link = 'https://www.youtube.com/watch?v=YslpixMUbYU'
        # bot_message.body(bot_commands)
        # bot_message.media(get_steam_image())
        # bot_message.media(link)
        # bot_message.body(y_link)
        # bot_message.media('https://download.samplelib.com/mp3/sample-3s.mp3')
        # bot_message.body(str(len(h)))
        # bot_message.media(
        # 'https://890a-197-210-52-107.ngrok.io/uploads/output_file.json')
        info = get_info()['Exchange']
        message_body = f"Exchange Summary: \n From: {info[0]}\n To:{info[1]}\n Amount: {info[2]}"

        bot_message.body(message_body)

    if incoming_msg == 'get':
        # if incoming_msg:
        from_currency = ''
        to_currency = ''
        amount = 0
        if incoming_msg:
            bot_message.body(
                "Enter Currency you are converting from:(eg. 1.NGN)")
            from_currency = incoming_msg.upper()
        # if incoming_msg:

        if '1' in incoming_msg:
            bot_message.body("Enter Currency you are converting to:(eg 2.GHS)")
            to_currency = incoming_msg.upper()
        # if incoming_msg:

        if '2' in incoming_msg:
            bot_message.body("Enter Amount:")
            amount = int(incoming_msg)

        result = get_info(from_currency, to_currency, amount)

        bot_message.body(result)
    return str(bot_response)


@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
