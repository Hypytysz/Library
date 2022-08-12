from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='homepage' ),
    path('authors_list', views.authors_list, name='authors_list'),
    path("details/<int:pk>", views.author_details, name="details"),
]