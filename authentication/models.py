from django.db import models
import face_recon.recognition as recon
import bcrypt

# Create your models here.
class User(models.Model):
    """Application user database.
    """
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    wallet_id = models.CharField(max_length=42)
    encrypted_img_str = models.TextField(max_length=3000)
    private_key = models.TextField(max_length=256)

    def User(self, username="", password="", wallet_id="", encrypted_img="", private_key=""):
        return

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = bcrypt.hashpw(password=password, salt=bcrypt.gensalt())

    def set_wallet_id(self, wallet_id):
        self.wallet_id = wallet_id

    def set_encrypted_img(self, encrypted_img):
        self.encrypted_img_str = recon.get_encrypted_picture_str(encrypted_picture=encrypted_img)

    def set_private_key(self, private_key):
        self.private_key = private_key

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_wallet_id(self):
        return self.wallet_id

    def get_encrypted_img_str(self):
        return self.encrypted_img_str

    def get_private_key(self):
        return self.private_key
