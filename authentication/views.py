from django.shortcuts import render, redirect
from authentication.models import FaceAuthUser
from authentication.forms import login
from blockchain.auth_backend import FacialAuth
import face_recon.handle_picture as hd
import face_recon.recognition as recon
from datetime import datetime
import bcrypt

# Create your views here.
facial_auth = FacialAuth()

def login_password(request):
    if request.method == 'POST':
        form = login.LoginPassword(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                valid = facial_auth.authenticate(
                    request, username=username, password=form.cleaned_data['password'])
                if valid:
                    return redirect('user_view')
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
                facial_auth = FacialAuth()
                valid = facial_auth.authenticate(
                    request, username=username, encrypted_img=encrypted_img)
                if valid is not None:
                    return redirect('user_view', private_key=user.private_key)
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


def users_list(request):
    users = FaceAuthUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users_list.html', context)


def user_view(request):
    if facial_auth.get_user() is None:
        return redirect('login_password')
    context = {
        'user': facial_auth.get_user()
    }
    return render(request, 'user_view.html', context)


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
