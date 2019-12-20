from django.contrib.auth.backends import BaseBackend
import bcrypt
import face_recon
from authentication.models import User

class FacialAuth(BaseBackend):
    def authenticate(self, request, username=None, image=None, password=None):
        # Check the username/password username/image and return a user.
        try:
            user = User.objects.get(username=username)
            pwd_valid = bcrypt.checkpw(password=password, hashed_password=user.password)
            img_valid = face_recon.recognize()
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

