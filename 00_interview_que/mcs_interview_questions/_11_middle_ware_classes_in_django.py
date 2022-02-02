"""
11.middle ware classes in django?


In a nutshell, a Middleware is a regular Python class that hooks into Django's request/response
life cycle. Those classes holds pieces of code that are processed upon every request/response your
Django application handles.

The Middleware classes does’t have to subclass anything and it can live anywhere in your Python path.
The only thing Django cares about is the path you register in the project settings MIDDLEWARE_CLASSES.

11.1.Your Middleware class should define at least one of the following methods:

11.1.1: Called during request:

    process_request(request)
    process_view(request, view_func, view_args, view_kwargs)

11.1.2:Called during response:

    process_exception(request, exception) (only if the view raised an exception)
    process_template_response(request, response) (only for template responses)
    process_response(request, response)

The Middleware classes are called twice during the request/response life cycle.
you define the Middlewares in the MIDDLEWARE_CLASSES configuration is important.

built-in Middleware classes the django-admin startproject command sets up:

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

During the request cycle, the Middleware classes are executed top-down, meaning it will first
execute SecurityMiddleware, then SessionMiddleware all the way until XFrameOptionsMiddleware.
For each of the Middlewares it will execute the process_request() and process_view() methods.

At this point, Django will do all the work on your view function. After the work is done
(e.g. querying the database, paginating results, processing information, etc), it will return a
response for the client.

During the response cycle, the Middleware classes are executed bottom-up, meaning it will first
execute XFrameOptionsMiddleware, then MessageMiddleware all the way until SecurityMiddleware.
For each of the Middlewares it will execute the process_exception(), process_template_response()
and process_response() methods.

Finally Django will deliver the response for the client. It is important to note that process_exception()
is only executed if a exception occurs inside the view function and process_template_response() is only
executed if there is a template in the response.




"""