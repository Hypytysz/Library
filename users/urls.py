from django.urls import path, include

from authors.views import homepage


urlpatterns = [

    path('', homepage, name='homepage'),
]