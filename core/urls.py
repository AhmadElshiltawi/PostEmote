from django.urls import path
from . import views

urlpatterns = [
    # For the home path (www.our_url.com/), run views.index
    path('', views.index, name='index'),

    # For the signup path (www.our_url.com/signup), run views.signup
    path('signup', views.signup, name='signup'),
]
