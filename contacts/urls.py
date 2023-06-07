
from django.urls import path
from . import views

urlpatterns = [
    path('inqury', views.inqury, name='inqury'),
]
