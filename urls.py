from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'pyukbash.ui.views.landing', name='landing'),
    url(r'^submit$', 'pyukbash.ui.views.submit', name='submit'),
)
