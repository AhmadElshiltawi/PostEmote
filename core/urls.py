from django.urls import path
from . import views

urlpatterns = [
    # For the home path (www.our_url.com/), run views.index
    path('', views.index, name='index'),

    # For the signup path (www.our_url.com/signup), run views.signup
    path('signup', views.signup, name='signup'),

    # For the signin path (www.our_url.com/signin), run views.signin
    path('signin', views.signin, name='signin'),

    # For the sign out path (www.our_url.com/signout), run views.signin
    path('signout', views.signout, name='signout'),
]
