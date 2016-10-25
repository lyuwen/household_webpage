# Household Website

This is just a simple and easy-to-setup web App, 
that allows you to manage multiple stuff within
a household.

## Installation

First you need to have django. You can run a local
version with that.
If you want to make it accessible on internet.
There're few free options:

1. [PythonAnywhere](https://www.pythonanywhere.com)

1. [Heroku](https://www.heroku.com)

And that's basicly it.

## Basic settings

1. First you need to create a database. A SQLite is suffice,
but if you want MySQL please proceed with caution.

1. Find settings.py.local and settings.py.production
in ./mysite/mysite/ directory. Make a copy of settings.py.local
to settings.py and fill in the DATABASE settings.

1. Then create a superuser for the web App with

    ```bash
    ./manage.py createsuperuser
    ```

1. Do the migrations for Django with
    
    ```
    ./manage.py makemigrations
    ./manage.py migrate
    ```

1. Then you should be able to run the website locally with
    
    ```
    ./manage.py runserver
    ```
