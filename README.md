# minimal-python-web3-read-blockchain-example

start a local node that connects the the blockchain that listens either to 
- the mainnet (geth)
- an official testnet (geth --rinkeby)
- or on your local machine in memory (ganache)

set the right network in the settings.py file

to test with ganache either install and run ganache locally or install truffle and run the command truffle develop

connect your metamask wallet to your blockchain (local or public whichever your local machine is running)

make a transaction in metamask between two accounts

install python 3.6
activate the local python virtual environment: 
source ./project_env/bin/activate
run python read_blockchain.py 

this will print the input of the last transaction of the blockchain