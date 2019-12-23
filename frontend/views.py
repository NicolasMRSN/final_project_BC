from django.shortcuts import render
from authentication.models import FaceAuthUser

# Create your views here.
def frontend(request):
    """Show all information stored about a single user.

    Args:
        pk (str): [description]

    Returns:
        render: show_user.html
    """
    user = FaceAuthUser.objects.get(pk=pk)
    context = {
        'user' : user
    }
    return render(request, 'frontend.html', context)