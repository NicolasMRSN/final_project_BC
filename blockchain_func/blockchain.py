from web3 import Web3
import frontend.views

class Blockchain():

    ganache_url = "http://127.0.0.1:7545"
    accounts = None
    client = None
    transactions_hashes = []
    transactions = []

    def __init__(self):
        self.connectClient()

    def connectClient(self):
        try:
            self.client = Web3(Web3.HTTPProvider(self.getURL()))
            return True
        except:
            print("Connection to the web3 client failed.")
            return False

    def getClient(self):
        return self.client

    def setURL(self, url):
        self.ganache_url = url

    def getURL(self):
        return self.ganache_url

    def getTransactionsHashes(self):
        return self.transactions_hashes

    def getTransactions(self):
        return self.transactions

    def setTransactions(self):
        if self.transactions_hashes is []:
            return []
        for hash in self.transactions_hashes:
            transaction = self.client.eth.getTransaction(hash)
            self.transactions.append([transaction["from"], transaction["to"], self.client.fromWei(transaction["value"], 'ether'), self.client.toHex(transaction["blockHash"])])
    
    def setAccounts(self):
        self.accounts = self.client.eth.accounts

    def make_transaction(self, receiver, private_key, amount):
        nonce = self.client.eth.getTransactionCount(self.accounts[frontend.views.current_user_id - 1])

        tx = {
            'nonce': nonce,
            'to': receiver,
            'value': self.client.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': self.client.toWei('50', 'gwei')
        }

        signed_tx = self.client.eth.account.signTransaction(tx, private_key)
        tx_hash = self.client.toHex(self.client.eth.sendRawTransaction(signed_tx.rawTransaction))
        self.transactions_hashes.append(tx_hash)
