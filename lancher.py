#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from chatterbot import ChatBot
reload(sys)
sys.setdefaultencoding("utf-8")
import logging
logging.basicConfig(level=logging.INFO)



# Create a new ChatBot instance
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    trainer='chatterbot.trainers.ListTrainer',
    database='chatterbot-database'
)
print('Type something to begin...')



# Get a response for some unexpected input
response = bot.get_response('كيف الحال')
print(response)