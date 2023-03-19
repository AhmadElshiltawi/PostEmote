from django.urls import path
from . import views

urlpatterns = [
    # For the home path (www.our_url.com/), run views.index
    path('', views.index, name='index'),

    # For the signup path (www.our_url.com/signup), run views.signup
    path('signup', views.signup, name='signup'),
    
    path('suprised-react', views.suprised_react, name = "suprised-react"),
    
    path('happy-react', views.happy_react, name = "happy-react"),
    
    path('angry-react', views.angry_react, name = "angry-react"),
    
    path('sad-react', views.sad_react, name = "sad-react"),
    
    path('remove-post', views.remove_post, name = "remove-post"),

    # For the signin path (www.our_url.com/signin), run views.signin
    path('signin', views.signin, name='signin'),

    # For the sign out path (www.our_url.com/signout), run views.signin
    path('signout', views.signout, name='signout'),
]
