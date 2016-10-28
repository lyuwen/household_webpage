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

## User settings

When you are able to run the website locally, 
then you should be able to put it online as well.

After that you need to configure users as the website is 
majorly protected by user authorization.

Currently the code will load all the users and data in the 
```home_members``` group.
Just put everyone in that group and it's good to go.

## Features

1. Shared purchases and balance for members

1. Payment recording

## Features will come in the future

1. Support for multiple home groups.

1. Email notification support for superuser