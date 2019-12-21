import initialize_ganache

client = initialize_ganache.initialize_ganache()

def make_transaction(sender, receiver, private_key, amount):
    nonce = client.eth.getTransactionCount(sender)

    tx = {
        'nonce': nonce,
        'to': receiver,
        'value': client.toWei(amount, 'ether'),
        'gas': 2000000,
        'gasPrice': client.toWei('50', 'gwei')
    }

    signed_tx = client.eth.account.signTransaction(tx, private_key)
    tx_hash = client.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(client.toHex(tx_hash))
    return client.toHex(tx_hash)

def get_transaction(hash_transaction):
    print(client.eth.getTransaction(hash_transaction))
    value = client.eth.getTransaction(hash_transaction)
    return client.eth.getTransaction(hash_transaction)