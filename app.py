from flask import Flask, render_template, request
# from flask_ngrok import run_with_ngrok

import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)
quit=False
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"
# print("Let's chat! (type 'quit' to exit)")
def response(sentence):
    # sentence = "do you use credit cards?"
    if sentence == "quit":
        pass
        # response_final = "Bye"
        # quit = True
    else:

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        prob_print = prob.item()*100
        prob_print = str(round(prob_print, 1))
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    response_final = f"{bot_name} {prob_print}%: {random.choice(intent['responses'])}"
        else:
            response_final=f"{bot_name} {prob_print}%: I am confused. Rephrase your question and make sure it is related to the following: <br>1) Guide about Vaccination Dose List <br>2) Side Effects of Vaccine  <br>3) Hospitals for Vaccination  <br>4)Information about vaccine"

    return response_final




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    sentence = request.form["msg"]
    if sentence == "quit":
        res = f"{bot_name}: Bye"
    else:
        res = response(sentence)
    
    return res
if __name__ == "__main__":
    app.debug = True
    app.run()

