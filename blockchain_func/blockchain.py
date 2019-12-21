from web3 import Web3


class Blockchain():

    ganache_url = "http://127.0.0.1:7545"
    client = None

    def __init__(self):
        self.connectClient()


    def connectClient(self):
        try:
            self.client = Web3(Web3.HTTPProvider(ganache_url))
        except:
            print("Connection to the web3 client failed.")

    def getClient(self):
        return self.client

    def setURL(self, url):
        self.ganache_url = url

    def getURL(self):
        return self.ganache_url

    def make_transaction(self, sender, receiver, private_key, amount):
        nonce = self.client.eth.getTransactionCount(sender)

        tx = {
            'nonce': nonce,
            'to': receiver,
            'value': client.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': client.toWei('50', 'gwei')
        }

        signed_tx = self.client.eth.account.signTransaction(tx, private_key)
        tx_hash = self.client.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(self.client.toHex(tx_hash))
        return self.client.toHex(tx_hash)

    def get_transaction(self, hash_transaction):
        print(self.client.eth.getTransaction(hash_transaction))
        value = self.client.eth.getTransaction(hash_transaction)
        return self.client.eth.getTransaction(hash_transaction)