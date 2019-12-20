import face_recognition
import handle_picture
import numpy as np

def encrypt_picture(im):
    """
    :param im: str, name of the file which will be encrypt, must be a .jpeg file.
    :return: numpy.ndarray, encrypted picture.
    """
    if isinstance(im, str) is False:
        return 84
    if im[-5:] != ".jpeg":
        return 84
    recon_pic = face_recognition.load_image_file(im)
    encrypted_picture = face_recognition.face_encodings(recon_pic)[0]
    return encrypted_picture

def get_encrypted_picture_from_string(encrypted_picture_str):
    """
    :param user: str, ID of the user who ask for authentication for retrieving the linked encrypted picture
    :return: numpy.ndarray, ecnrypted picture linked to the user account
    """
    if isinstance(encrypted_picture_str, str) is False:
        return 84
    return np.fromstring(string=encrypted_picture_str, sep=';')


def get_encrypted_picture_str(encrypted_picture):
    """
    :param encrypted_picture: numpy.ndarray
    :return: str corresponding to the encrypted picture. Empty str if error
    """
    if isinstance(encrypted_picture, np.ndarray) is False:
        return ''
    encrypted_picture_str = ''
    try:
        for number in encrypted_picture:
            encrypted_picture_str += str(number) + ';'
    except:
        encrypted_picture_str = ''
    return encrypted_picture_str

def recognize(im_from_db, im_to_check):
    """
    :param im_from_server: numpy.ndarray, encrypted image linked to the account of the user you want to be verified
    :param im_to_check: numpy.ndarray, encrypted image of the user who wants to be verified
    :return: Boolean, True if verified, False if not verified.
    """
    if isinstance(im_from_server, np.ndarray) is False or isinstance(im_from_db, np.ndarray) is False:
        return False
    ret = face_recognition.compare_faces([im_from_server], im_to_check)
    return ret[0]

