from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^todos/', include('todos.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
