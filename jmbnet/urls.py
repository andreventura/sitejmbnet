from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^jmbnet/', include('jmbnet.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^$','django.contrib.auth.views.login', {'template_name': 'loginform.html'}),
    (r'^auth/logout/$','django.contrib.auth.views.logout_then_login'),
    (r'^menuprincipal/$','jmbnet.menuprincipal.views.menuprincipal'),
    (r'^menuprincipal/compras$','jmbnet.compras.views.compras'),
    (r'^compras/cliente$','jmbnet.compras.views.insert'),
    (r'^files/(.*)','django.views.static.serve',{'document_root':'/home/ventura/sitejmbnet/jmbnet/files'}),
)
    # (r'^auth/login/$','django.contrib.auth.views.login', {'template_name': 'loginform.html'}),
