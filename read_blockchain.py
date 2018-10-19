from utils.blockchain_uitls import get_eth_provider

import settings
from web3 import Web3

# web3.py instance
provider_to_use = get_eth_provider(settings.NETWORK_TO_USE)
w3 = Web3(provider_to_use)
if settings.NETWORK_TO_USE == 'rinkeby':
    # this is necessary because of the special consensus mechanism of rinkeby:
    # https://web3py.readthedocs.io/en/stable/middleware.html#geth-style-proof-of-authority
    from web3.middleware import geth_poa_middleware
    # inject the PoA compatibility middleware to the innermost layer
    w3.middleware_stack.inject(geth_poa_middleware, layer=0)
# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[settings.ETHER_WALLET_ID_TO_USE]


latest_block = w3.eth.getBlock('latest')
try:
    latest_transaction_hash = latest_block['transactions'][-1]
except IndexError as e:
    latest_transaction_hash = None
if latest_transaction_hash:
    latest_transaction = w3.eth.getTransaction(latest_transaction_hash)

    # transform input data from bytes to text
    input = w3.toText(bytes(latest_transaction.input, 'utf-8'))
    
    # for now, it just print the input
    print(input)
