from django.urls import path
from . import views
urlpatterns = [
    path('', views.books_list, name='books_list'),
    path("details/<int:pk>", views.book_details, name="book_details"),
]