"""
12. what are the signals in django?


Django includes a “signal dispatcher” which helps decoupled applications get notified when actions
occur elsewhere in the framework. In a nutshell, signals allow certain senders to notify a set of
receivers that some action has taken place.They’re especially useful when many pieces of code may
be interested in the same events.

A list of all the signals that Django sends. All built-in signals are sent using the send() method.

Django provides a set of built-in signals that let user code get notified by Django itself of certain
actions.

    12.1.django.db.models.signals.pre_save & django.db.models.signals.post_save

        Sent before or after a model’s save() method is called.

    12.2.django.db.models.signals.pre_delete & django.db.models.signals.post_delete

        Sent before or after a model’s delete() method or queryset’s delete() method is called.

    12.3.django.db.models.signals.m2m_changed

        Sent when a ManyToManyField on a model is changed.

    12.4.django.core.signals.request_started & django.core.signals.request_finished

        Sent when Django starts or finishes an HTTP request.

12.1.model signals:

    1.pre_init:

    2.post_init:

    3.pre_save

    4. post_save

    5.pre_delete

    6.post_delete

    7.m2m_changed

    8.class prepared

12.2.management signals
    1.pre_migrate
    2. post_migrate

12.3.request/response signals
    1.request_started
    2. request_finished
    3.got_request_exception

12.4.test signals
    1.setting_changed
    2.template_rendered

12.4.Database Wrappers

Signals sent by the database wrapper when a database connection is initiated.
    1.connection_created



"""