from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/profile/$', 'cmstemplates.views.usuario'),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^annotated/$', 'cmstemplates.views.mostrar'),
    url(r'^annotated/(\d+)', 'cmstemplates.views.buscar'),
    url(r'^annotated/anadir', 'cmstemplates.views.pagina_nueva'),
    url(r'^admin/', include(admin.site.urls)),
)
