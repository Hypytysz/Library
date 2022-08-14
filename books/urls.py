from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.books, name='books'),
    path("details/<int:pk>", views.book, name="book"),
]