'''

Flask is a Python web developement framework to build web applications. It comes with jinja2, a templating language
for Python, and Werkzeug, a WSGI utility module.

Flask is a web application framework written in Python. It was developed by Armin Ronacher, who led a team of
international Python enthusiasts called Poocco. Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template
engine.Both are Pocco projects.

Flask is a web framework, it’s a Python module that lets you develop web applications easily.
It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager)

It does have many cool features like url routing, template engine. It is a WSGI web app framework.

WEB FRAMEWORK:
Web Framework represents a collection of libraries and modules that enable web application developers to
write applications without worrying about low-level details such as protocol, thread management,

WSGI:
The Web Server Gateway Interface (Web Server Gateway Interface, WSGI) has been used as a standard for Python web
application development. WSGI is the specification of a common interface between web servers and web applications.

Werkzeug
Werkzeug is a WSGI toolkit that implements requests, response objects, and utility functions. This enables a
web frame to be built on it. The Flask framework uses Werkzeg as one of its bases.

jinja2
jinja2 is a popular template engine for Python.A web template system combines a template with a specific
data source to render a dynamic web page.
This allows you to pass Python variables into HTML templates.

PostgreSQL:
PostgreSQL is an open source relational database system which, as its name suggests,
uses SQL.

SQLAlchemy:
SQLAlchemy is an Object Relational Mapper (ORM), it is a layer between
object oriented Python and the database schema of Postgres.

Alembic:
Alembic is a useful module to manage migrations with SQLAlchemy in Python. Migrations occur when one wants to change
the database schema linked to the application, like adding a table or removing a column from a table. It can also be
used to write or delete data in a table. Alembic enables developers not to manually upgrade their database and to
easily revert any change: migrations go up and down. It is also useful to recreate databases from scratch,
by following the migration flow.
(using commands pip install alembic , alembic init)

To communicate with Postgres backend, and psycopg2, a libpq wrapper in Python.

POSTMAN:
Postman is an interactive and automatic tool for verifying the API. It works in the backend and makes sure that the
is working as expected. Postman can create a request and gives the response to make sure that it contains the element
that we want in the API. Postman allows us to build, test and modify the API

REST API - Representational state protocal
A RESTful API is an architectural style for an application program interface (API) that uses HTTP requests to access
and use data. That data can be used to GET, PUT, POST and DELETE data types, which refers to the reading, updating,
creating and deleting of operations concerning resources.

Limitations of FLASK:

1. Not suitable for big applications.
2. Community.
3. Full-Stack experience.
4. No admin site.
5. No login or authentication.
6. ORM.
7. Migrations can be difficult.


links:

Flask basics and snippets:

https://pythonbasics.org/flask-tutorial-hello-world/
https://python-adv-web-apps.readthedocs.io/en/latest/flask.html

for deployment using docker and DB postgres connectivity
https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396

'''