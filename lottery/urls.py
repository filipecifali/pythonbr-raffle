from django.urls import path

from lottery import views

urlpatterns = [
    path('', views.register, name='register')
]
