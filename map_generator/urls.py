from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'map_generator.views.map_view', name='map'),
)
