# The minimal-python-web3-read-blockchain-example
This is an example of how to use the blockchain from an App using python. The objetive is create the easiest way to:
- Read the blockchain (you need a full node for now).
- Read the transaction info (for now, just from the preselected address).
- Print the input data.

## Objetives to resolve
- Read the transactions of any address (not just preselected).
- Just filter the transactions for a stablished rules of the input data.
- Put the input data in a DB.
- Send tx directly without the need of doing manual with Metamask.


## Instructions
Start a local node that connects the the blockchain that listens either to:
- the mainnet (geth)
- an official testnet (geth --rinkeby)
- or on your local machine in memory (ganache)

Set the right network in the settings.py file.

To test with ganache either install and run ganache locally or install truffle and run the command truffle develop.

Connect your metamask wallet to your blockchain (local or public whichever your local machine is running).

Make a transaction in metamask between two accounts.

```sh
install python 3.6
```
Activate the local python virtual environment: 
```sh
source ./project_env/bin/activate
run python read_blockchain.py 
```

This will print the input of the last transaction of the blockchain.
