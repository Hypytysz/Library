from django.urls import path, include
from posts import views

urlpatterns = [
    path("", views.posts, name="posts"),
    path('__debug__/', include('debug_toolbar.urls')),
    path("details/<int:pk>", views.post_details, name="postdetails")
]