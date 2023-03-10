from django.contrib.auth.models import User, auth
from . import models


def validate_credential_not_null(credential):
    if credential == "":
        return False
    else:
        return True


def authenticate_user(request, username, password):
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return user
    else:
        return None


def create_user(username, email_address, password):
    new_user = User.objects.create_user(username=username, email=email_address, password=password)
    new_user.save()

    auth.authenticate(username=username, password=password)

    profile = models.Profile(user=new_user)
    profile.save()

    return new_user


def sign_out(requests):
    auth.logout(requests)
