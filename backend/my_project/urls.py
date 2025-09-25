from django.contrib import admin
from django.urls import path, include
from . import api

urlpatterns = [
    path('', include(api.router.urls)),
    path('api/auth/',
         include('rest_framework.urls', namespace='rest_framework')),
    path('', include('my_app.urls')),
    path('admin/', admin.site.urls),
]
