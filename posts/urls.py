from django.urls import path, include
from posts import views

urlpatterns = [
    path("", views.posts, name="posts"),
    path('__debug__/', include('debug_toolbar.urls')),
    path("details/<int:pk>", views.post_details, name="postdetails"),
    path("edit/<int:pk>", views.post_edit, name="edit"),
    path("delete/<int:pk>", views.delete_post, name="delete"),
]