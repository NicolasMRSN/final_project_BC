from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from authentication.models import User

class FacialAuth(BaseBackend):
    def authenticate(self, request, username=None, image=None, password=None):
        # Check the username/password username/image and return a user.
        try:
            user = User.objects.get(username=username)
            pwd_valid = check_password(password, user.password)
            img_valid = False
            if pwd_valid or img_valid:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

