DATABASE INSTRUCTIONS AND INFO

host name: ubuntu-s-1vcpu-1gb-nyc1-01
password: g$?QaedtDe92uJE
IP address: 159.203.182.153

users: (to switch: `su aj`)
maria
ziggy

aj
ziggy

tehya
ziggy


Postgres:
database: LinkedIncognito
user: LIuser
password: ziggy

Virtualenv: LIenv

django project: LIapp


Superuser:
username: maria
email: mjm1175@nyu.edu
password: ziggy

username: aj
email: ajo331@nyu.edu
password: ziggy

username: tehya
email: tt1748@nyu.edu
password: ziggy

{% load static %} at top of html files

Run server: python manage.py runserver 0.0.0.0:8000

Start Up:
	>ssh root@159.203.182.153
		password:g$?QaedtDe92uJE
	$ su maria
		password:ziggy
	$ cd
	$ cd dev/LinkedIncognito/LinkedIncognito
	$ source LIenv/bin/activate
	$ cd LIapp



robocopy D:\Spring 2022\Senior Design\LinkedIncognito\LinkedIncognito-webpages\images\* maria@159.203.182.153:/home/maria/dev/LinkedIncognito/LinkedIncognito/LIapp/static/app/images/

still need to change hyperlinks <a> and <href> i think it should be ="/profile" or whatever url you set up in urls.py

cant figure out how to create Employer/applicant user instead of generic
cant figure out how to put both login and register on the same page

companyprofile admin

when you add a new model:
	python manage.py makemigrations
	python manage.py migrate

if you want a class (model) attribute to be optional:
	in models.py set null=True, blank=True
	in forms.py set required=False