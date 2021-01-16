#What is ChatBot --> It is a program simulates a conversation between a user and a computer
#There are two types of ChatBot on the basis of implemented technologies and use --> 1.Self Learning ChatBot ,2.Rule Based ChatBot
#ChatterBot --> python library which uses ML and conversational dialog engine(Automated Responces) and we can create ChatBot in any of HighLevel Languages(eng,hindi...)
#Limitation of ChatBot --> 1.Domain knowledge(language boundry while talkin bet human and a computer)
#Training the chatbot -->there is lib called Chatterbot-corpus(whic has all the responces for our input)
#Use case --> Flask(framework) Chatbot

#Steps involed-->
#1.Make a web app using flask
#2.App contains a chatbot using html+css
#3.Train the bot
#4.Make conversation with the app

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer#for training the chatbot

app = Flask(__name__)

#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

# Create object of ChatBot class
english_bot = ChatBot('Chatterbot')

#Create object of ChatBot class with Storage Adapter
# english_bot = ChatBot(
#     'Chatterbot',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     database_uri='sqlite:///database.sqlite3'
# )

#Training our data
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
