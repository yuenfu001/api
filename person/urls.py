from django.urls import path
from .views import update_person, person
urlpatterns = [
    path("person/", person, name='list'),
    path("person/<str:pk>/", update_person, name='unique'),
]
