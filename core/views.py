from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from . import backend

# TODO: Set up the main page front end
def index(request):
    return render(request, 'index.html')


def signin(request):
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
                new_user = User.objects.create_user(username=username, email=email_address, password=password)
                new_user.save()

                return redirect('signin')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('signup')

    else:
        return render(request, 'sign-up.html')


# TODO: Set this to a button so that the user can sign out of the system
def signout(request):
    auth.logout(request)
    return redirect('signin')

# TODO: Set up the post and comment functionalities
