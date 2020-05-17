from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^token-auth/?$', views.CustomAuthToken.as_view()),
    url(r'^register/?$', views.CreateUserView.as_view()),
]