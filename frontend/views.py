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
    user = FaceAuthUser.objects.get(pk=1)
    global current_user_id
    current_user_id = user.pk
    bc = Blockchain()
    bc.setAccounts()
    users = FaceAuthUser.objects.all()
    transactions = bc.getTransactions()
    if request.method == 'POST':
        form = Transaction(request.POST)
        if form.is_valid():
            bc.make_transaction(form.cleaned_data["receiver"], form.cleaned_data["private_key"], form.cleaned_data["amount"])
    form = Transaction
    bc.setTransactions()
    context = {
        'users' : users,
        'transactions': bc.transactions,
        'form': form
    }
    return render(request, 'frontend.html', context)