import os
import time
import openai
import yaml
# Opens a (*.yml) file using YAML with a read parameter. Setting it as "file".
path = os.path.join(os.path.curdir, "config.yml")
with open(path, "r") as file:
    # Sets "cfg" to load in "file".
    cfg = yaml.safe_load(file)
# This line of code states, for a "section" in "cfg" execute the code below.
# The "section" is later defined as "api_key".
for section in cfg:
    apikey = cfg["api_key"]
    your_name = cfg["your_name"]
    # print("Hello " + your_name + ", your API KEY is: " + apikey)
    # time.sleep(5)
    
openai.api_key = apikey
def types():
    os.system("clear")
    print("This script was developed by Parker Phillips, using Open AI.")
    time.sleep(5)
    os.system("clear")
    print("* OG / Gangster behavior")
    print("* Devilish Guy behavior")
    print("* Type in your own place to generate a behavior. (e.g New York)")
    print("* Modern behavior / act like people today.")
    print("* Long Time friends behavior")
    print("* Homeless behavior")
    print("* Shakespeare behavior")
    type = int(input("Select a text-based behavior for the AI (1-7): "))
    # A system that detects the input was "1" or not.
    if (type == 1):
        os.system("clear")
        # Changes the behavior of the AI. Tells the AI to talk with some slang.
        place = input("Please input your preferred 'slang' captial. (e.g New York): ")
        friendstype = "Remember your a gangster from " + place + " too. Keep it cool with some slang when you talk to me."
        os.system("clear")
    if (type == 2):
        # Changes the behavior of the AI. Tells the AI to act like a bad guy.
        friendstype = "Please act like a devilish guy. Remember you are my loyal friend. We just do not speak about being friends."
        os.system("clear")  
    if (type == 3):
        # Changes the behavior of the AI. You input the place / location.
        secondary_place = input("Please type in a place: ")
        friendstype = "Please act like you are from " + secondary_place + " when you conversate with me."
        os.system("clear")
    if (type == 4):
        # Changes the behavior of the AI. Tells the AI to be like the people of today. Modernized.
        friendstype = "Please act like the people today. People that are living in a modern society. When you conversate with me."
        os.system("clear")
    if (type == 5):
        # Changes the behavior of the AI. Tells the AI to act like you have been friends for a long time.
        friendstype = "Please act like were long time loyal friends when you conversate with me."        
        os.system("clear")
    if (type == 6):
        # Changes the behavior of the AI. Tells the AI to act like it is a homeless AI.
        friendstype = "Please act like you are homeless."
        os.system("clear")
    if (type == 7):
        # Changes the behavior of the AI. Telling it to only act like Shakespeeare.
        friendstype = "Please act like Shakespeare when you conversate with me."
        openai.Model.list()
        os.system("clear")
    def initial_interaction():
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are my loyal friend." + friendstype + " It is time for our daily conversation."},
        ]
        )
        print(completion.choices[0].message.content)
        ai_response = completion.choices[0].message.content
        def continuation():
            response = input("Enter your response: ")
            if your_name != None:
                completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Please call me by " + your_name + " is my name. Only call me by name when needed. Respond to this message as if you were my friend. Do not greet me nor ask me about my day. I only want you to respond to the message I give you. Analyze the set of text. Make aure you read why I sent this in order to make sure your responss is fitting. I first sent this in response to you. You sent this: " + ai_response + " and I sent this: " + response},
                    {"role": "system", "content": "Respond to this message as if you were my friend. Keep it on the down low by asking how my day was or a gernal question do not mention the term friend. " + friendstype + " Do not greet me nor ask me about my day. I only want you to respond to the message I give you. Analyze the set of text. Make sure you read why I sent this in order to make sure your response is fitting. I first sent this in response to you. You sent this:" + ai_response + " and I sent this: " + response},
                ]
                )
                print(completion.choices[0].message.content)
                return continuation()
            else:
                completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Respond to this message as if you were my friend. Keep it on the down low by asking how my day was or a general question do not mention the term friend. " + friendstype + " Do not greet me or ask me about my day. I only want you to respond to the message I give you A. Analyze the set of text. Make sure you read why I sent this in order ti make sure your response is fitting. I first sent this in response to you. You sent me this: " + ai_response + " and I sent this: " + response},    
                ]
                )
                print(completion.choices[0].message.content)
                return continuation()
        return continuation()
            
        
    initial_interaction()
types()
