from django.urls import path
from . import views



urlpatterns = [
    path('', views.authors_list, name='homepage'),
    path("details/<int:pk>", views.author_details, name="details"),
]