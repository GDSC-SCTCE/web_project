# Survey Form

## Introduction

A simple survey form with database


## Getting the Application Running

1. Clone the repository and open `survey_form_with_database by Fahad` folder in vscode.
2. To make this project running at first you should create a virtual environment by typing the following in the command prompt:
```sh 
mkvirtualenv virtualenv_name 
```

3. Check whether you are in the virtual environment, if not type the following in command prompt to enter virtual environment:
```sh
workon virtualenv_name
```

4. Once in virtual environment, check the working directory and confirm you are in the `survey_form_with_database by Fahad` folder
5. Then type the following in command prompt:
```sh
pip install -r requirements
``` 
6. Confirm the installations and then type the following to migrate the data:
```sh
python manage.py migrate
```
6. Confirm the migration is error free, and then type the following in command prompt and follow the instructions in terminal to create a superuser:
```sh 
python manage.py createsuperuser
``` 
7. Now type the following to start the website server in localhost:
```sh
python manage.py runserver
```
8. Now type the following in your browser to access the website:
```sh
localhost:8000
```
8. Now type the following in your browser to access the admin panel of website, then login using the credentials or superuser:
```sh
localhost:8000/admin
```
<!-- CONTACT -->
## Contact

Fahad P N - <a href='https://www.linkedin.com/in/fahad-p-n-93a7441b4/'>LinkedIn</a>


