from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

def initialize_ganache():
    client = Web3(Web3.HTTPProvider(ganache_url))
    return client