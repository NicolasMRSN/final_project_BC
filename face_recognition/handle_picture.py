import cv2
import os
import numpy

def take_picture():
    """

    :return: numpy.ndarray, picture of the user.
    """
    camera = cv2.VideoCapture(0)
    retval, im = camera.read()
    del (camera)
    return im

def format_picture_jpeg(user, im):
    """

    :param user: str, ID of the user
    :param im: numpy.ndarray, picture took by handle_picture.take_picture()
    :return: str, name of the .jpeg file.
    """
    if isinstance(user, str) is False:
        return 84
    if isinstance(im, numpy.ndarray) is False:
        return 84
    print("Taking image...")
    working_directory = os.getcwd()
    file = working_directory + "/" + user + ".jpeg"
    cv2.imwrite(file, im)
    return file

def send_encrypted_picture_to_server():
    """

    :return: void.
    """
    return
