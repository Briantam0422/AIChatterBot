import sys

from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Wing',
)

trainer = ChatterBotCorpusTrainer(chatbot)

# trainer.train(
#     "chatterbot.corpus.chinese.order"
# )

print('Type something to begin...')

# The following loop will execute each time the user enters input
user_input = input()


def get_date():
    # words = ["年", "月"]
    # if all(user_input for x in words):
    if "年" in user_input:
        month = user_input.split("月")[0]
        return month

get_date()

# user_input = input()
#
# bot_response = chatbot.get_response(user_input)
#
# print(bot_response)
