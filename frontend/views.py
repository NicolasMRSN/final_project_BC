from django.shortcuts import render
from blockchain_func.blockchain import Blockchain
from authentication.models import FaceAuthUser
from blockchain.auth_backend import FacialAuth
from frontend.forms.transaction import Transaction

# Create your views here.
def frontend(request):
    """Show all information stored about a single user.

    Args:
        pk (str): [description]

    Returns:
        render: show_user.html
    """

    bc = Blockchain()
    users = FaceAuthUser.objects.all()
    transactions = bc.getTransactions()
    print(transactions)
    user = FacialAuth.get_user()
    print(username)
    if request.method == 'POST':
        form = Transaction(request.POST)
        if form.is_valid():
            print(form.cleaned_data["receiver"])
            print(form.cleaned_data["amount"])

    form = Transaction

    context = {
        'users' : users,
        'transaction': transactions,
        'form': form
    }
    return render(request, 'frontend.html', context)