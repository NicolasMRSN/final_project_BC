from django.db import models
import face_recon.recognition as recon
import bcrypt

# Create your models here.


class FaceAuthUser(models.Model):
    """Application user database.
    """
    username = models.CharField(max_length=100)
    password = models.BinaryField()
    wallet_id = models.CharField(max_length=42)
    encrypted_img_str = models.TextField(max_length=3000)
    private_key = models.TextField(max_length=256)

    @classmethod
    def create(cls, username, password, wallet_id, encrypted_img, private_key):
        password = bcrypt.hashpw(password=password.encode(
            'utf-8'), salt=bcrypt.gensalt())
        encrypted_img_str = recon.get_encrypted_picture_str(
            encrypted_picture=encrypted_img)

        user = cls(username=username, password=password, wallet_id=wallet_id,
                   encrypted_img_str=encrypted_img_str, private_key=private_key)
        return user
