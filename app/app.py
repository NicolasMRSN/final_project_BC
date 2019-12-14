# Use the follwing command to install the requirements.txt
# pip install -r requirements.txt
#
# Use the following command to run the code:
# python -m app
#
# Use the following command to add the project ID:
# export WEB3_INFURA_PROJECT_ID=c2037afdbccd4f6db2a449f9dae9a07f

from web3.auto.infura import w3

def run():
    print('We hate france')
    print(w3.eth.blockNumber)
    w3.eth.getBlock('latest')