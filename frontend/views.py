from django.shortcuts import render
from authentication.models import User
from 'blockchain_func/blockchain' import Blockchain
# Create your views here.
def frontend(request):
    """Show all information stored about a single user.

    Args:
        pk (str): [description]

    Returns:
        render: show_user.html
    """
    bc = Blockchain()
    bc.setAccounts()
    user = bc.accounts
    transaction = bc.getTransactions()
    context = {
        'user' : user,
        'transaction': transaction
    }
    return render(request, 'frontend.html', context)