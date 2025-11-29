from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/reviews/add/", views.add_review, name="add_review"),
]
