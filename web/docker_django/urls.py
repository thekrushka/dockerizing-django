from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin2/', include(admin.site.urls)),
    url(r'^', include('docker_django.apps.todo.urls')),
]
