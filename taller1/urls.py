from django.conf.urls import include, url
from django.contrib import admin
#from . import Noticias

urlpatterns = [
    # Examples:
    # url(r'^$', 'taller1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^noticia/id(?P<noticia_id>[0-9]+)', 'Noticias.views.vistaprincipal'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacto/','contacto.views.vistacontacto'),
]
