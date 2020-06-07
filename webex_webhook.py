import flask
from flask import request,jsonify
from webexteamssdk import WebexTeamsAPI
import json

# *** Created by : Jyoti Gautam

# Flask Configuration below
app = flask.Flask(__name__)
app.config["DEBUG"]

# team variable contain some data that Webex Bot will send when it sees team message.
team=[
    {
        'Service Provider':{
            'team_Name' : ['Jyoti','John','doe']
        }
    }
]

@app.route('/',methods=['POST'])
def post():
    # Here comes your Bot token to send the message when
    bot_token = 'Your Bot Token'
    api = WebexTeamsAPI(bot_token)

    # Posted_data will contain the entire POST json response from the triggered webex group and BOT
    posted_data = request.json
    print(posted_data)
    message=api.messages.get(messageId=posted_data["data"]["id"])   #data and id parameters will help us get the message posted by mentioning bot name in the webex chat with the message
    roomId= message.roomId
    print(message)
    #Below code checks the received message and respond accordingly. Please write your bot name and then message you wnat to receive.
    if message.text == "<your bot name> team":
        team_mem = team[0]['Service Provider']['team_Name']
        api.messages.create(roomId=roomId, text="Team Member: " +str(team_mem))
    if message.text == "My_test help":
        api.messages.create(roomId=roomId, markdown="--use @My_Test team<br> --use @My_Test help <br>Please reach out to jyogauta for any issue.") # My_test is my bot name
    return "<h1>I read message</p>"

#NO NEED to Write below code.
@app.route('/',methods=['GET'])
def home():
   return "<h1>You arrived at the right page</h1>"


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080) # To run our server

