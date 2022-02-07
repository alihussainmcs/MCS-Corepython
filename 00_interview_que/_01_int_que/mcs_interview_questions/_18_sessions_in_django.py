"""
18. sessions in django?

The session is a semi-permanent and two-way communication between the server and the browser.

Sessions are the mechanism used by Django (and most of the Internet) for keeping track of the
"state" between the site and a particular browser. Sessions allow you to store arbitrary data
per browser, and have this data available to the site whenever the browser connects.

For security reasons, Django has a session framework for cookies handling. Sessions are used
to abstract the receiving and sending of cookies, data is saved on server side (like in database), and
the client side cookie just has a session ID for identification. Sessions are also useful to avoid
cases where the user browser is set to ‘not accept’ cookies.

==>Setting Up Sessions:

In Django, enabling session is done in your project settings.py, by adding some lines to the
MIDDLEWARE_CLASSES and the INSTALLED_APPS options. This should be done while creating the project,
but it's always good to know, so MIDDLEWARE_CLASSES should have

'django.contrib.sessions.middleware.SessionMiddleware'

==>And INSTALLED_APPS should have −

'django.contrib.sessions'

By default, Django saves session information in database (django_session table or collection), but
you can configure the engine to store information using other ways like: in file or in cache

==>Some More Possible Actions Using Sessions

    set_expiry (value) − Sets the expiration time for the session.

    get_expiry_age() − Returns the number of seconds until this session expires.

    get_expiry_date() − Returns the date this session will expire.

    clear_expired() − Removes expired sessions from the session store.

    get_expire_at_browser_close() − Returns either True or False, depending on whether the user’s
    session cookies have expired when the user’s web browser is closed.

Django considers the importance of sessions over the website and therefore provides you with
middleware and inbuilt app which will help you generate these session IDs without much hassle.

A session is a mechanism to store information on the server side during the interaction with the
web application.

In Django, by default session stores in the database and also allows file-based and cache based
sessions. It is implemented via a piece of middleware and can be enabled by using the following code.

Put django.contrib.sessions.middleware.SessionMiddleware in MIDDLEWARE and django.contrib.sessions
in INSTALLED_APPS of settings.py file.
To set and get the session in views, we can use request.session and can set multiple times too.


"""