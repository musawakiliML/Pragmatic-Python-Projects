# Required libaries
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from emoji import emojize as em

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

    # Bot commands
    command = ['hello', 'hi', 'what do you do', 'start', 'commands']
    bot_commands_list = ['/get_popular_releases','/get_new_releases','get_new_releases','get_popular_releases', 'get popular releases', 'get new releases']
    
    # bot navigation and conversation
    if incoming_msg in command:
        bot_commands = f"""Hello, I am Steam Bot. I Scrape the Steam Game Store Website to get games and more. I Can you anything on the site just search through my commands and hit me {em(':smile:', language="alias")}.
        These are my commands {em(":robot:", language="alias")} :
        - /get_popular_releases
        - /get_new_releases
        """
       
    
        bot_message.body(bot_commands)
        # bot_message.body(str(len(h)))

    return str(bot_response)


if __name__ == "__main__":
    app.run(debug=True)
