import bcrypt
import face_recon.recognition as recon
from authentication.models import User

class FacialAuth():
    def authenticate(self, request, username=None, encrypted_img=None, password=None):
        # Check the username/password username/image and return a user.
        try:
            user = User.objects.get(username=username)
            pwd_valid = False
            img_valid = False
            if encrypted_img is None:
                password = password.encode('utf-8')
                hashed_pw = user.password.encode('utf-8')
                pwd_valid = bcrypt.checkpw(password=password, hashed_password=hashed_pw)
            else:
                encrypted_img_db = user.encrypted_img_str
                img_valid = recon.recognize(recon.get_encrypted_picture_from_string(encrypted_img_db), encrypted_img)
            if img_valid or pwd_valid:
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

