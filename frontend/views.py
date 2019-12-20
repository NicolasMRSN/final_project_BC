from django.shortcuts import render
from authentication.models import User

# Create your views here.
def frontend(request):
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
    return render(request, 'frontend.html', context)