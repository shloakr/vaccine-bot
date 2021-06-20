# Vaccine Bot

### Description 
This model uses a rule based chatbot. A rule based chatbot was used as answers should be highly accurate when used for medical information. The model was created using Deep Neural Netoworks with the Pytourch library. The text was first stemmed and tokenized after which a bag of words was created. The python flask library was used for the website. The website is made using Bootstrap4, jquery, html and css.

### Video Example

response structure:
"{name of bot} {%accuary of the question matching the intents.json}: {response}"

https://drive.google.com/file/d/1BBo2THnYupALUwum8IZz8fU7Knxndh34/view?usp=sharing

### Images

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/70055735/122668168-7750fb80-d1d4-11eb-8679-fbbb3e48caaf.png">

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/70055735/122668202-a5ced680-d1d4-11eb-9275-aa386dcd2d4e.png">


## To run this on your local host
**Mac or Linux**
Install VirtualEnv.<br/>
```python3 -m venv env```<br/>
```source env/bin/activate```<br/>
At this point make sure to have your virtual environment activated. You should get ```(env)``` in you terminal.<br/>
```pip install -r requirements.txt```<br/>
At this point make sure to be in your folder that holds the ```app.py``` file.<br/>
```python app.py```<br/>
Then copy paste the local host with the port in any web browser. It will most likely start with '127.0'.

## Issues
Hosting this projects exccesed Heroku Slug Limit of 500mb

## Cite
If you find the code in the repository useful, please cite it using:
```
@miscsShloakr2021vaccine-bot,
  author = {Shloak Rathod},
  title = {An Open Source Implementation of Vaccine Information Bot},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {Available at \url{https://github.com/shloakr/vaccine-bot/}}
}
```
