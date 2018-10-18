from web3 import Web3, HTTPProvider
import os
import settings
from solc import compile_source


def get_eth_provider(provider_name):
    # open a connection to a local ethereum node (ganache geth or simple in memory blockchain)
    if provider_name == "in_memory_test_rpc":
        return Web3.TestRPCProvider()

    eth_providers = {
        'local': HTTPProvider('http://localhost:9545'),
        'rinkeby': Web3.IPCProvider(settings.RINKEBY_SOCKET_FILE_PATH),
    }

    return eth_providers[provider_name]
