from django.contrib.auth.backends import BaseBackend
import bcrypt
import face_recon.recognition as recon
from authentication.models import User

class FacialAuth(BaseBackend):
    def authenticate(self, request, username="", encrypted_img="", password=""):
        # Check the username/password username/image and return a user.
        try:
            user = User.objects.get(username=username)
            #pwd_valid = bcrypt.checkpw(password=password, hashed_password=user.password)
            encrypted_img_db = user.encrypted_img_str
            img_valid = recon.recognize(recon.get_encrypted_picture_from_string(encrypted_img_db), encrypted_img)
            if img_valid:
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

