from django.urls import path, include

from . import views

urlpatterns = [
    path('about/my_app/', views.index, name="index"),
]
