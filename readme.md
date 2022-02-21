# StackOverflow

We simulated the most famous site for searching with specific task of their choosing. 

## you can  
    * Search with limiting  per min(5) and per day(100) for each session.
 
## Install

* you need to install python3
* you need to install pip or pip3 package
* postman or google chrome

## Run the project

* download the project 
* open the project in terminal by press `Ctrl-Alt+T`
* install virtualenv `pip install virtualenv` 
* init your virtualenv `virtualenv env`
* active virtualenv `source env/bin/activate`
* install required packages on virtualenv `pip install -r requirements.txt`
* migrate models to create tables in db `python manage.py migrate`
* run server `python manage.py runserver`
* open browser on this link http://127.0.0.1:8000/stackoversearch/
 
