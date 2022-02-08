
DJANGO E-COMMERCE


Shops  nowadays are now turning their businesses online to provide their customers a better experience. One of the most popular e-commerce website IN kenya is jumia. Using the django framework on an eccommerce application is  recommendedbecause it is an open-source, high-level Python web framework. Its emphasis on reusable components makes it faster for developers to build web apps on top of Python and  It presents itself as a web framework for perfectionists with deadlines.

ABOUT THIS PROJECT

It is an E-commerce system built in Django. It contains all the essentials for adding products and  .

DEMO

This simple e-commerce application demonstrates CRUD operations using DBsqlite . This web app is 100% free to use, you can customize it to build a more sophisticated e-commerce web application. Feel free to submit an issue on GitHub if you found any bug or even better – submit a pull request.

This web application is currently hosted on Heroku, https://brenda-shop.herokuapp.com/store to view the demo. Heroku is for testing only - it does not support file uploads as the filesystem is readonly. Although you can still test the image upload functionality but all images will automatically be deleted after a couple of minutes.


To Install:
Cloning the Repository:

$ git clone https://github.com/reanbrenda/eshop.git

$ cd Eshop-main

Installing the environment control:

$ pip install virtualenv

$ virtualenv env

Activating the environment:

on Windows:

env\Scripts\activate

on Mac OS / Linux:

$ source env/bin/activate

Installing dependencies:

$ pip install -r requirements.txt


Last commands to start:

$ python manage.py makemigrations

$ python manage.py migrate

Create a super user:

$ python manage.py createsuperuser admin-name

Finishing running server:

$ python manage.py runserver
