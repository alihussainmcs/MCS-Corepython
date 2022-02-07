"""
24. blueprint of flask?


Basically, a flask blueprint is a way for you to organize your flask application into smaller
and re-usable application. Just like a normal flask application, a blueprint defines a collection
of views, templates and static assets.


#What is the use of blueprints in Flask?

Flask uses a concept of blueprints for making application components and supporting common
patterns within an application or across applications. Blueprints can greatly simplify how
large applications work and provide a central means for Flask extensions to register operations
on applications.


Each Flask Blueprint is an object that works very similarly to a Flask application. They both can
have resources, such as static files, templates, and views that are associated with routes.
However, a Flask Blueprint is not actually an application. It needs to be registered in an
application before you can run it.

A Blueprint is a way to organize a group of related views and other code. Rather than registering
views and other code directly with an application, they are registered with a blueprint. Then the
blueprint is registered with the application when it is available in the factory function.

Flask will have two blueprints, one for authentication functions and one for the blog posts functions.
The code for each blueprint will go in a separate module. Since the blog needs to know about
authentication, you’ll write the authentication one first.


There are other optional arguments that you can provide to alter the Blueprint’s behavior:

    static_folder: the folder where the Blueprint’s static files can be found

    static_url_path: the URL to serve static files from

    template_folder: the folder containing the Blueprint’s templates

    url_prefix: the path to prepend to all of the Blueprint’s URLs

    subdomain: the subdomain that this Blueprint’s routes will match on by default

    url_defaults: a dictionary of default values that this Blueprint’s views will receive

    root_path: the Blueprint’s root directory path, whose default value is obtained from the Blueprint’s
    import name

Blueprint objects also provide other methods that you may find useful:

    .error_handler() to register an error handler function
    .before_request() to execute an action before every request
    .after_request() to execute an action after every request
    .app_template_filter() to register a template filter at the application level

project layout:

ecommerce/
|
├── static/
|   ├── logo.png
|   ├── main.css
|   ├── generic.js
|   └── product_view.js
|
├── templates/
|   ├── login.html
|   ├── forgot_password.html
|   ├── signup.html
|   ├── checkout.html
|   ├── cart_view.html
|   ├── index.html
|   ├── products_list.html
|   └── product_view.html
|
├── app.py
├── config.py
└── models.py

static/ contains the application’s static files.
templates/ contains the application’s templates.
models.py contains the definition of the application’s models.
app.py contains the application logic.
config.py contains the application configuration parameters.


If you use a separate directory for each Flask Blueprint and its resources, then the project
layout would look as follows:

ecommerce/
|
├── api/
|   ├── __init__.py
|   └── api.py
|
├── auth/
|   ├── templates/
|   |   └── auth/
|   |       ├── login.html
|   |       ├── forgot_password.html
|   |       └── signup.html
|   |
|   ├── __init__.py
|   └── auth.py
|
├── cart/
|   ├── templates/
|   |   └── cart/
|   |       ├── checkout.html
|   |       └── view.html
|   |
|   ├── __init__.py
|   └── cart.py
|
├── general/
|   ├── templates/
|   |   └── general/
|   |       └── index.html
|   |
|   ├── __init__.py
|   └── general.py
|
├── products/
|   ├── static/
|   |   └── view.js
|   |
|   ├── templates/
|   |   └── products/
|   |       ├── list.html
|   |       └── view.html
|   |
|   ├── __init__.py
|   └── products.py
|
├── static/
|   ├── logo.png
|   ├── main.css
|   └── generic.js
|
├── app.py
├── config.py
└── models.py

"""