from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'videocentro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/', 'actor.views.signin', name='signin'),
    url(r'^signup/', 'actor.views.signup', name='signup'),
    url(r'^peliculas/', 'pelicula.views.peliculas_view', name='peliculas_view'),

)
