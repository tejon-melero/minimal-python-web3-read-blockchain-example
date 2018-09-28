import React, {Component} from 'react'
import VotingContract from '../build/contracts/Voting.json'
import getWeb3 from './utils/getWeb3'

import './css/oswald.css'
import './css/open-sans.css'
import './css/pure-min.css'
import './App.css'

class App extends Component {
    constructor(props) {
        super(props)

        this.state = {
            votingOptions: null,
            VotingInstance: null,
            accounts: null,
            web3: null
        }
    }

    componentWillMount() {
        // Get network provider and web3 instance.
        // See utils/getWeb3 for more info.

        getWeb3
            .then(results => {
                this.setState({
                    web3: results.web3
                })

                // Instantiate contract once web3 provided.
                this.instantiateContract()
            })
            .catch(() => {
                console.log('Error finding web3.')
            })
    }

    instantiateContract() {

        const contract = require('truffle-contract')
        const Voting = contract(VotingContract)
        Voting.setProvider(this.state.web3.currentProvider)

        // Declaring this for later so we can chain functions on SimpleEscrow.
        var VotingInstance;

        // Get accounts.
        this.state.web3.eth.getAccounts((error, accounts) => {
            Voting.deployed().then((instance) => {
                VotingInstance = instance;
                this.setState({votingInstance: instance});
                this.setState({accounts: accounts});
                this.setState({addressOfCurrentWallet: accounts[0]})


                VotingInstance.getVotingOptions(accounts[0]).then((result) => {
                    // Update state with the result.
                    console.log('the voting options are: ', result);
                    this.setState({votingOptions: result});
                });

            })
        })
    }


    render() {
        return (
            <div className="App">
                <nav className="navbar pure-menu pure-menu-horizontal">
                    <a href="#" className="pure-menu-heading pure-menu-link">Voting Example</a>
                </nav>

                <main className="container">
                    <div className="pure-g">
                        <div className="pure-u-1-1">
                            <h1>Simple Escrow</h1>
                            <p><strong>voting options: {this.state.votingOptions} </strong></p>

                        </div>
                    </div>
                </main>
            </div>
        );
    }
}
export default App
