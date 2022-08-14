from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='homepage' ),
    path('authors', views.authors_list, name='authors'),
    path("details/<int:pk>", views.author_details, name="details"),
]