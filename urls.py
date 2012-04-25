from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'pyukbash.ui.views.landing', name='landing'),
    url(r'^submit$', 'pyukbash.ui.views.submit', name='submit'),
    url(r'^quote/(\d+)$', 'pyukbash.ui.views.quote_page', name='quote_page'),
    url(r'^vote/(\d+)/(up|down)$', 'pyukbash.ui.views.vote', name='vote'),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
