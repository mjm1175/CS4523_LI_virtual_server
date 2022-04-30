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

that port is already in use: sudo fuser -k 8000/tcp

PAT: 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
git push https://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@github.com/mjm1175/CS4523_LI_virtual_server.git

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

no placeholder for password1 also not registering as password field

last updated not working(on resume)

need edit resume/education/experience
need add experience form
no feedback when enter wrong password
download button for coverletter and cv
some kind of error with the skills entry on experience form