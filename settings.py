import os
project_directory =os.path.dirname(os.path.abspath(__file__))
RINKEBY_SOCKET_FILE_PATH = '/tmp/rinkeby/geth.ipc'
MAINNET_SOCKET_FILE_PATH = ''
NETWORK_TO_USE = 'local'  # choose between 'local' --> ganache (use this if you are developing with truffle and start
# the local blockchain with truffle develop) 'in_memory_test_rpc' --> simple in memory blockchain (use this if you are
# not using truffle to start the development blockchain)  or 'rinkeby' --> rinkeby testnet
CONTRACTS_FOLDER = contracts_folder = os.path.join(os.path.join(project_directory, 'truffle_project'), 'contracts')
ETHER_WALLET_ID_TO_USE = 0 #insert your wallet
