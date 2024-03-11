# recipe-app

Web-application built with Python using the Django framework. 

## How to get the project running:

*Note: You will need to work in a virtual environment with Django installed*

### If you have not yet created a virtual environment on your machine:

- To create a virtual environment you will need to install virtualenvwrapper `pip install virtualenvwrapper`
- Once installed run `mkvirtualenv test-environment`
- Then run `workon a2-ve-recipeapp` to load the installed environment
- Finally, run `pip install django` (mac) or `py -m pip install Django` (win) to install Django in the environment

### Once in you virtual environment:

- Navigate to root folder in terminal
- Run the following: `python manange.py runserver`
- In browser, navigate to http://127.0.0.1:8000/

Users are able to do the following:
- View all recipes in list
- Click on any recipe to view it's details
