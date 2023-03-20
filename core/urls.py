from django.urls import path
from . import views

urlpatterns = [
    # For the home path (www.our_url.com/), run views.index
    path('', views.index, name='index'),

    # For the signup path (www.our_url.com/signup), run views.signup
    path('signup', views.signup, name='signup'),
    
    path('surprising_sort', views.surprising_sort, name = 'surprising-sort'),
    
    path('happy_sort', views.happy_sort, name = 'happy-sort'),
    
    path('angry_sort', views.angry_sort, name = 'angry-sort'),
    
    path('sad_sort', views.sad_sort, name = 'sad-sort'),
    
    path('suprised-react', views.suprised_react, name = "suprised-react"),
    
    path('happy-react', views.happy_react, name = "happy-react"),
    
    path('angry-react', views.angry_react, name = "angry-react"),
    
    path('sad-react', views.sad_react, name = "sad-react"),
    
    path('remove-post', views.remove_post, name = "remove-post"),
    
    path('add-comment', views.add_comment, name = "add-comment"),
    
    path('disable-comments', views.disable_comments, name = "disable-comments"),
    
    path('enable-comments', views.enable_comments, name = "enable-comments"),

    # For the signin path (www.our_url.com/signin), run views.signin
    path('signin', views.signin, name='signin'),

    # For the sign out path (www.our_url.com/signout), run views.signin
    path('signout', views.signout, name='signout'),
]
