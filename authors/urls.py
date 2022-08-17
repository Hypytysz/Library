from django.urls import path, include
from . import views



urlpatterns = [

    path('', views.authors_list, name='authors'),
    path("<int:pk>", views.author_details, name="details"),
]