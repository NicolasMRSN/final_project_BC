import face_recognition
import handle_picture
import time
import numpy.core.multiarray

def encrypt_picture(im):
    """
    :param im: str, name of the file which will be encrypt, must be a .jpeg picture.
    :return: numpy.ndarray, encrypted picture.
    """
    if im[-5:] != ".jpeg":
        return 84
    recon_pic = face_recognition.load_image_file(im)
    encrypted_picture = face_recognition.face_encodings(recon_pic)[0]
    print(type(encrypted_picture))
    print(encrypted_picture)
    return encrypted_picture

def get_user_encrypted_picture_from_server(user):
    """

    :param user: str, ID of the user who ask for authentication for retrieving the linked encrypted picture
    :return: numpy.ndarray, ecnrypted picture linked to the user account
    """
    return

def recognize(im_from_server, im_to_check):
    """

    :param im_from_server: numpy.ndarray, encrypted image linked to the account of the user you want to be verified
    :param im_to_check: numpy.ndarray, encrypted image of the user who wants to be verified
    :return: Boolean, True if verified, False if not verified.
    """
    if isinstance(im_from_server, numpy.ndarray)
    ret = face_recognition.compare_faces([im_from_server], im_to_check)
    return ret[0]