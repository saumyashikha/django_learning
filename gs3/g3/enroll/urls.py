from django.urls import path
from . import views

urlpatterns = [
    path('enroll/', views.stuinfo),
]