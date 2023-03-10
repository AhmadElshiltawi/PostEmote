from django.contrib.auth.models import auth


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

def sign_out(requests):
    auth.logout(requests)