from django.shortcuts import render
from authentication.models import User

# Create your views here.
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
