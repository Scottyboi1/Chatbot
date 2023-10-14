import google.generativeai as palm
import os

palm.configure(api_key=os.environ['AIzaSyBtk1aaZdajLnEyV0yTGqvy7IaBoNZD88A'])

response = palm.chat(messages=["Hello."])
print(response.last) #  'Hello! What can I help you with?'
response.reply("Can you tell me a joke?")