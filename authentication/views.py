from django.shortcuts import render, redirect
from authentication.models import FaceAuthUser
from authentication.forms import login
from blockchain.auth_backend import FacialAuth
import face_recon.handle_picture as hd
import face_recon.recognition as recon
from datetime import datetime
import bcrypt

facial_auth = FacialAuth()

# Create your views here.
current_user_id = 0 # global variable

def login_password(request):
    if request.method == 'POST':
        form = login.LoginPassword(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                valid = facial_auth.authenticate(
                    request, username=username, password=form.cleaned_data['password'])
                if valid:
                    return redirect('frontend')
                else:
                    form = login.LoginPassword()
            except FaceAuthUser.DoesNotExist:
                form = login.LoginPassword
    else:
        form = login.LoginPassword
    context = {
        'form': form
    }
    return render(request, 'login_password.html', context)


def login_face(request):
    if request.method == 'POST':
        form = login.LoginFace(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                user = FaceAuthUser.objects.get(username=username)
                timestamp = datetime.now()
                encrypted_img = recon.encrypt_picture(hd.format_picture_jpeg(
                    hd.take_picture(), timestamp.strftime("%Y%m%d%H%M%S%f")))
                valid = facial_auth.authenticate(
                    request, username=username, encrypted_img=encrypted_img)
                if valid:
                    return redirect('frontend')
                else:
                    form = login.LoginFace
            except FaceAuthUser.DoesNotExist:
                form = login.LoginFace
    else:
        form = login.LoginFace
    context = {
        'form': form
    }
    return render(request, 'login_face.html', context)


def register(request):
    if request.method == 'POST':
        form = login.Register(request.POST)
        if form.is_valid():
            timestamp = datetime.now()
            encrypted_img = recon.encrypt_picture(hd.format_picture_jpeg(
                hd.take_picture(), timestamp.strftime("%Y%m%d%H%M%S%f")))
            user = FaceAuthUser.create(username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                                       wallet_id=form.cleaned_data['wallet'], encrypted_img=encrypted_img, private_key=form.cleaned_data['pk'])
            user.save()

    form = login.Register
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
