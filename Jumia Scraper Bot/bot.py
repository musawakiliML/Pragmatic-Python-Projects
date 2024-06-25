# Required libaries
from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse
from emoji import emojize as em
import uuid
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
    profile_name = request.values.get('ProfileName','')
    print(request.values)
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
        # info = get_info()['Exchange']
        # message_body = f"Exchange Summary: \n From: {info[0]}\n To:{info[1]}\n Amount: {info[2]}"
        message_body = f"Hello, {profile_name}!!! \n"
        info_message = """Good Day, These are the categories of products we have \n 1. Stationary \n 2. Electronics \n 3. Food. \n Reply with a number(eg. 1)"""

        bot_message.body(message_body)
        bot_message.body(info_message)
    if incoming_msg == "1":
        info = """Great! \n Under Stationary We have the following products. \n 1. Stapler \n 2. Highlighter \n 3. Eraser \n 4. Paper Clip \n 5. Pen \n What do you want to order?"""
        bot_message.body(info)
    if incoming_msg == "stapler":
        details = "Great!\nGive me your name, Phonenumber, address and Quantity.\nFormat:Order: Name - Phone Number - Address \n eg. Order: Musa - 0812345678 - No.5 beside bank road, bauchi - 123"
        bot_message.body(details)
    if "order" in incoming_msg:
        order_info = f"Order has been recieved!! Thank You.\n Order Id: {uuid.uuid1()}"
        good_bye = "Goodbye."
        bot_message.body(order_info)    
        bot_message.body(good_bye)
    # if incoming_msg == '1':
    #     # if incoming_msg:
    #     from_currency = ''
    #     to_currency = ''
    #     amount = 0
    #     if incoming_msg:
    #         bot_message.body(
    #             "Enter Currency you are converting from:(eg. 1.NGN)")
    #         from_currency = incoming_msg.upper()
    #     # if incoming_msg:

    #     if '1' in incoming_msg:
    #         bot_message.body("Enter Currency you are converting to:(eg 2.GHS)")
    #         to_currency = incoming_msg.upper()
    #     # if incoming_msg:

    #     if '2' in incoming_msg:
    #         bot_message.body("Enter Amount:")
    #         amount = int(incoming_msg)

    #     result = get_info(from_currency, to_currency, amount)

    #     bot_message.body(result)
    return str(bot_response)


@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
