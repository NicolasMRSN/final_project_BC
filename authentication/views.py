from django.shortcuts import render, redirect
from authentication.models import User
from authentication.forms import login
from blockchain.auth_backend import FacialAuth
import face_recon.handle_picture as hd
import face_recon.recognition as recon
from datetime import datetime
import bcrypt

# Create your views here.
def login_password(request):
    if request.method == 'POST':
        form = login.LoginPassword(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                user = User.objects.get(username=username)
                facial_auth = FacialAuth()
                valid = facial_auth.authenticate(request, username=username, password=form.cleaned_data['password'])
                if valid is not None:
                    return redirect('user_view', id=user)
                else:
                    form = login.LoginFace
            except User.DoesNotExist:
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
                user = User.objects.get(username=username)
                timestamp = datetime.now()
                encrypted_img = recon.encrypt_picture(hd.format_picture_jpeg(hd.take_picture(), timestamp.strftime("%Y%m%d%H%M%S%f")))
                facial_auth = FacialAuth()
                valid = facial_auth.authenticate(request, username=username, encrypted_img=encrypted_img)
                if valid is not None:
                    return redirect('user_view', id=user)
                else:
                    form = login.LoginFace
            except User.DoesNotExist:
                form = login.LoginFace
    else:
        form = login.LoginFace
    context = {
        'form': form
    }
    return render(request, 'login_face.html', context)


def users_list(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'users_list.html', context)

def user_view(request, user=None):
    if user is None:
        return redirect('login_face')
    context = {
        'user' : user
    }
    return render(request, 'user_view.html', context)

def register(request):
    if request.method == 'POST':
        form = login.Register(request.POST)
        if form.is_valid():
            timestamp = datetime.now()
            salt = bcrypt.gensalt()
            password = form.cleaned_data['password'].encode('utf8')
            hashed = bcrypt.hashpw(password, salt)
            user = User()
            user.set_username(form.cleaned_data['username'])
            user.set_password(hashed)
            user.set_wallet_id(form.cleaned_data['wallet'])
            user.set_private_key(form.cleaned_data['pk'])
            encrypted_img = recon.encrypt_picture(hd.format_picture_jpeg(hd.take_picture(), timestamp.strftime("%Y%m%d%H%M%S%f")))
            user.set_encrypted_img(encrypted_img)
            user.save()

    form = login.Register
    context = {
        'form': form
    }
    return render(request, 'register.html', context)