from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Post, Comment, SuprisedReact, HappyReact, AngryReact, SadReact
from django.contrib.auth.decorators import login_required
from . import backend

@login_required(login_url='signin')
def index(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if 'profile-picture' in request.FILES:
            profile.profile_image = request.FILES['profile-picture']
            profile.save()
            return redirect('/')

        elif 'post-image' in request.FILES:
            new_post = Post(profile=profile, post_image=request.FILES['post-image'])
            new_post.save()
            return redirect('/')

        # elif 'comment' in request.POST:
        #     cur_post_id = request.POST['post_id']
        #     cur_comment = request.POST['comment']
        #     current_post = Post.objects.get(post_id=cur_post_id)
        #     new_comment = Comment(post=current_post, profile=profile, comment=cur_comment)
        #     new_comment.save()
        #     return redirect('/')
    
    return render(request, 'index.html', {'profile': profile, 'posts': Post.objects.all().order_by('created'), 'comments': Comment.objects.all()})

@login_required(login_url='signin')
def surprising_sort(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if 'profile-picture' in request.FILES:
            profile.profile_image = request.FILES['profile-picture']
            profile.save()
            return redirect('/')

        elif 'post-image' in request.FILES:
            new_post = Post(profile=profile, post_image=request.FILES['post-image'])
            new_post.save()
            return redirect('/')

        # elif 'comment' in request.POST:
        #     cur_post_id = request.POST['post_id']
        #     cur_comment = request.POST['comment']
        #     current_post = Post.objects.get(post_id=cur_post_id)
        #     new_comment = Comment(post=current_post, profile=profile, comment=cur_comment)
        #     new_comment.save()
        #     return redirect('/')

    return render(request, 'index.html', {'profile': profile, 'posts': Post.objects.all().order_by('shocked_likes'), 'comments': Comment.objects.all()})

@login_required(login_url='signin')
def happy_sort(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if 'profile-picture' in request.FILES:
            profile.profile_image = request.FILES['profile-picture']
            profile.save()
            return redirect('/')

        elif 'post-image' in request.FILES:
            new_post = Post(profile=profile, post_image=request.FILES['post-image'])
            new_post.save()
            return redirect('/')

        # elif 'comment' in request.POST:
        #     cur_post_id = request.POST['post_id']
        #     cur_comment = request.POST['comment']
        #     current_post = Post.objects.get(post_id=cur_post_id)
        #     new_comment = Comment(post=current_post, profile=profile, comment=cur_comment)
        #     new_comment.save()
        #     return redirect('/')

    return render(request, 'index.html', {'profile': profile, 'posts': Post.objects.all().order_by('happy_likes'), 'comments': Comment.objects.all()})

@login_required(login_url='signin')
def angry_sort(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if 'profile-picture' in request.FILES:
            profile.profile_image = request.FILES['profile-picture']
            profile.save()
            return redirect('/')

        elif 'post-image' in request.FILES:
            new_post = Post(profile=profile, post_image=request.FILES['post-image'])
            new_post.save()
            return redirect('/')

        # elif 'comment' in request.POST:
        #     cur_post_id = request.POST['post_id']
        #     cur_comment = request.POST['comment']
        #     current_post = Post.objects.get(post_id=cur_post_id)
        #     new_comment = Comment(post=current_post, profile=profile, comment=cur_comment)
        #     new_comment.save()
        #     return redirect('/')

    return render(request, 'index.html', {'profile': profile, 'posts': Post.objects.all().order_by('angry_likes'), 'comments': Comment.objects.all()})

@login_required(login_url='signin')
def sad_sort(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if 'profile-picture' in request.FILES:
            profile.profile_image = request.FILES['profile-picture']
            profile.save()
            return redirect('/')

        elif 'post-image' in request.FILES:
            new_post = Post(profile=profile, post_image=request.FILES['post-image'])
            new_post.save()
            return redirect('/')

        elif 'comment' in request.POST:
            cur_post_id = request.POST['post_id']
            cur_comment = request.POST['comment']
            current_post = Post.objects.get(post_id=cur_post_id)
            new_comment = Comment(post=current_post, profile=profile, comment=cur_comment)
            new_comment.save()
            return redirect('/')

    return render(request, 'index.html', {'profile': profile, 'posts': Post.objects.all().order_by('sad_likes'), 'comments': Comment.objects.all()})

@login_required(login_url='signin')
def suprised_react(request):
    # get profile of user reacting and post
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(post_id=request.POST.get('post_id'))
        
        # check if the user has reacted to this post in any way
        suprised_filter = SuprisedReact.objects.filter(post=post, profile=profile).first()
        happy_filter = HappyReact.objects.filter(post=post, profile=profile).first()
        angry_filter = AngryReact.objects.filter(post=post, profile=profile).first()
        sad_filter = SadReact.objects.filter(post=post, profile=profile).first()
        
        if suprised_filter == None and happy_filter == None and angry_filter == None and sad_filter == None:
            new_react = SuprisedReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.shocked_likes += 1
            post.save()
        elif happy_filter:
            happy_filter.delete()
            post.happy_likes -= 1
            new_react = SuprisedReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.shocked_likes += 1
            post.save()
        elif angry_filter:
            angry_filter.delete()
            post.angry_likes -= 1
            new_react = SuprisedReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.shocked_likes += 1
            post.save()
        elif sad_filter:
            sad_filter.delete()
            post.sad_likes -= 1
            new_react = SuprisedReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.shocked_likes += 1
            post.save()
        else:
            suprised_filter.delete()
            post.shocked_likes -= 1
            post.save()
        data = {
            'react': 'suprised',
            'suprisedCount': post.shocked_likes,
            'happyCount': post.happy_likes,
            'angryCount': post.angry_likes,
            'sadCount': post.sad_likes
        }
        return JsonResponse(data, safe=False)
    return redirect('/')
    
@login_required(login_url='signin')
def happy_react(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(post_id=request.POST.get('post_id'))
        
        suprised_filter = SuprisedReact.objects.filter(post=post, profile=profile).first()
        happy_filter = HappyReact.objects.filter(post=post, profile=profile).first()
        angry_filter = AngryReact.objects.filter(post=post, profile=profile).first()
        sad_filter = SadReact.objects.filter(post=post, profile=profile).first()
        
        if suprised_filter == None and happy_filter == None and angry_filter == None and sad_filter == None:
            new_react = HappyReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.happy_likes += 1
            post.save()
        elif suprised_filter:
            suprised_filter.delete()
            post.shocked_likes -= 1
            new_react = HappyReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.happy_likes += 1
            post.save()
        elif angry_filter:
            angry_filter.delete()
            post.angry_likes -= 1
            new_react = HappyReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.happy_likes += 1
            post.save()
        elif sad_filter:
            sad_filter.delete()
            post.sad_likes -= 1
            new_react = HappyReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.happy_likes += 1
            post.save()
        else:
            happy_filter.delete()
            post.happy_likes -= 1
            post.save()
        data = {
            'react': 'suprised',
            'suprisedCount': post.shocked_likes,
            'happyCount': post.happy_likes,
            'angryCount': post.angry_likes,
            'sadCount': post.sad_likes
        }
        return JsonResponse(data, safe=False)
    return redirect('/')

@login_required(login_url='signin')
def angry_react(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(post_id=request.POST.get('post_id'))
        
        suprised_filter = SuprisedReact.objects.filter(post=post, profile=profile).first()
        happy_filter = HappyReact.objects.filter(post=post, profile=profile).first()
        angry_filter = AngryReact.objects.filter(post=post, profile=profile).first()
        sad_filter = SadReact.objects.filter(post=post, profile=profile).first()
        
        if suprised_filter == None and happy_filter == None and angry_filter == None and sad_filter == None:
            new_react = AngryReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.angry_likes += 1
            post.save()
        elif happy_filter:
            happy_filter.delete()
            post.happy_likes -= 1
            new_react = AngryReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.angry_likes += 1
            post.save()
        elif suprised_filter:
            suprised_filter.delete()
            post.shocked_likes -= 1
            new_react = AngryReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.angry_likes += 1
            post.save()
        elif sad_filter:
            sad_filter.delete()
            post.sad_likes -= 1
            new_react = AngryReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.angry_likes += 1
            post.save()
        else:
            angry_filter.delete()
            post.angry_likes -= 1
            post.save()
        data = {
            'react': 'suprised',
            'suprisedCount': post.shocked_likes,
            'happyCount': post.happy_likes,
            'angryCount': post.angry_likes,
            'sadCount': post.sad_likes
        }
        return JsonResponse(data, safe=False)
    return redirect('/')

@login_required(login_url='signin')
def sad_react(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(post_id=request.POST.get('post_id'))
        
        suprised_filter = SuprisedReact.objects.filter(post=post, profile=profile).first()
        happy_filter = HappyReact.objects.filter(post=post, profile=profile).first()
        angry_filter = AngryReact.objects.filter(post=post, profile=profile).first()
        sad_filter = SadReact.objects.filter(post=post, profile=profile).first()
        
        if suprised_filter == None and happy_filter == None and angry_filter == None and sad_filter == None:
            new_react = SadReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.sad_likes += 1
            post.save()
        elif happy_filter:
            happy_filter.delete()
            post.happy_likes -= 1
            new_react = SadReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.sad_likes += 1
            post.save()
        elif angry_filter:
            angry_filter.delete()
            post.angry_likes -= 1
            new_react = SadReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.sad_likes += 1
            post.save()
        elif suprised_filter:
            suprised_filter.delete()
            post.shocked_likes -= 1
            new_react = SadReact.objects.create(post=post, profile=profile)
            new_react.save()
            post.sad_likes += 1
            post.save()
        else:
            sad_filter.delete()
            post.sad_likes -= 1
            post.save()
        data = {
            'react': 'suprised',
            'suprisedCount': post.shocked_likes,
            'happyCount': post.happy_likes,
            'angryCount': post.angry_likes,
            'sadCount': post.sad_likes
        }
        return JsonResponse(data, safe=False)
    return redirect('/')

@login_required(login_url='signin')
def remove_post(request):
    if request.method == 'POST':
        post = Post.objects.get(post_id=request.POST.get('post_id'))
        post.delete()
        index(request)
    return redirect('/')

@login_required(login_url='signin')
def add_comment(request):
    if request.method == 'POST':
        canComment = False
        post = Post.objects.get(post_id=request.POST.get('post_id'))
        profile = Profile.objects.get(user=request.user)
        comment = request.POST.get("comment")
        reaction = ''
        if SuprisedReact.objects.filter(post=post, profile=profile).first():
            canComment = True
            reaction = 'Surprised'
            new_comment = Comment.objects.create(post=post, profile=profile, comment=comment, reaction=reaction)
            new_comment.save()
            index(request)
        if HappyReact.objects.filter(post=post, profile=profile).first():
            canComment = True
            reaction = 'Happy'
            new_comment = Comment.objects.create(post=post, profile=profile, comment=comment, reaction=reaction)
            new_comment.save()
            index(request)
        if AngryReact.objects.filter(post=post, profile=profile).first():
            canComment = True
            reaction = 'Angry'
            new_comment = Comment.objects.create(post=post, profile=profile, comment=comment, reaction=reaction)
            new_comment.save()
            index(request)
        if SadReact.objects.filter(post=post, profile=profile).first():
            canComment = True
            reaction = 'Sad'
            new_comment = Comment.objects.create(post=post, profile=profile, comment=comment, reaction=reaction)
            new_comment.save()
            index(request)
        data = {
            'canComment': canComment,
            'reaction': reaction
        }
        return JsonResponse(data, safe=False)
    return redirect('/')

@login_required(login_url='signin')
def disable_comments(request):
    profile = Profile.objects.get(user=request.user)
    profile.allow_comments = False
    profile.save()
    return redirect('/')

@login_required(login_url='signin')
def enable_comments(request):
    profile = Profile.objects.get(user=request.user)
    profile.allow_comments = True
    profile.save()
    return redirect('/')

def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if not backend.validate_credential_not_null(username):
            messages.info(request, 'Username cannot be left blank!')
            return redirect('signin')

        if not backend.validate_credential_not_null(password):
            messages.info(request, 'Password cannot be left blank!')
            return redirect('signin')

        # If backend.authenticate_user returns a user, then the user has been logged in
        # If backend.authenticate_user doesn't return anything, then no account without the proper
        # credentials was found`
        user = backend.authenticate_user(request, username, password)

        if user is None:
            messages.info(request, 'Incorrect username or password')
            return redirect('signin')
        else:
            return redirect("/")

    else:
        return render(request, 'sign-in.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        # Get the values of the post method. These are what's used to sign up the user
        email_address = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if email_address == "":
            messages.info(request, 'Email cannot be left blank!')
            return redirect('signup')

        if username == "":
            messages.info(request, 'Username cannot be left blank!')
            return redirect('signup')

        if password == "":
            messages.info(request, 'Password cannot be left blank!')
            return redirect('signup')

        # Make sure the password and confirm-password are the same
        if password == confirm_password:
            # Check if the email exists
            if User.objects.filter(email=email_address).exists():
                messages.info(request, 'Email is already taken!')
                return redirect('signup')
            # Check if the username exists
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken!')
                return redirect('signup')
            # Everything checks out
            else:
                # Create a new user object and save it to the database
                backend.create_user(username, email_address, password)

                return redirect('signin')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('signup')

    else:
        return render(request, 'sign-up.html')


# TODO: Set this to a button so that the user can sign out of the system
@login_required(login_url='signin')
def signout(request):
    if request.user.is_authenticated:
        backend.sign_out(request)
    return redirect('signin')

# TODO: Set up the post and comment functionalities
