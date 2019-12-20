from django.shortcuts import render
from django.http import HttpResponseRedirect
from authentication.models import User
from authentication.forms import login
from face_recognition

# Create your views here.
def login_password(request):
    if request.method == 'POST':
        form = login.LoginPassword(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
                return HttpResponseRedirect('users/' + str(user.pk))
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
                user = User.objects.get(username=form.cleaned_data['username'])

                return HttpResponseRedirect('users/' + str(user.pk))
            except User.DoesNotExist:
                form = login.LoginFace
    else:
        form = login.LoginFace
    context = {
        'form': form
    }
    return render(request, 'login_password.html', context)


def users_list(request):
    """Show a list of all stored users.

    Returns:
        render: user_list.html
    """
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'users_list.html', context)

def user_view(request, pk):
    """Show all information stored about a single user.

    Args:
        pk (str): [description]

    Returns:
        render: show_user.html
    """
    user = User.objects.get(pk=pk)
    context = {
        'user' : user
    }
    return render(request, 'user_view.html', context)
