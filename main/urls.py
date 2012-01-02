from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('upload.main.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^new', 'new'),
    url(r'^del/(?P<id>[0-9]+)', 'del'),
    url(r'^download/(?P<id>[0-9]+)', 'download')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
