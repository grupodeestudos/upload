from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('upload.main.views',
    # Examples:
    url(r'^$', 'index', name='upload-index'),
    url(r'^new', 'new', name='upload-new'),
    #url(r'^del/(?P<id>[0-9]+)', 'del', name='upload-del'),
    url(r'^download/(?P<id>[0-9]+)', 'download', name='upload-download'),
    url(r'^remove/(?P<id>[0-9]+)', 'remove', name='remove-file'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
