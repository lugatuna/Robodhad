# -*- coding: utf-8 -*-
from chatterbot import ChatBot


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)


chatbot = ChatBot(
    'GitterBot',
    gitter_room='lugatuna',
    gitter_api_token='da9d61ff2cfc07e8f1ab',
    gitter_only_respond_to_mentions=False,
    input_adapter='chatterbot.input.Gitter',
    output_adapter='chatterbot.output.Gitter',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.train('chatterbot.corpus.english')

# The following loop will execute each time the user enters input
while True:
    try:
        response = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break