"""
15. what is allowed_host in django?

ALLOWED_HOSTS. A list of strings representing the host/domain names that this Django site
can serve. This is a security measure to prevent HTTP Host header attacks, which are possible
even under many seemingly-safe web server configurations.


The purpose of ALLOWED_HOSTS is to validate a request's HTTP Host header. Validation is
done to prevent rogue users from sending fake HTTP Host headers that can potentially
poison caches and password reset emails with links to malicious hosts.


#example:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
ALLOWED_HOSTS = ['*']
# Required Imports
from django.conf.urls.static import static
from django.conf import settings

# Below Urlpatterns
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



ALLOWED_HOSTS = ['www.example.com']
DEBUG = False
DEFAULT_FROM_EMAIL = 'webmaster@example.com'


"""