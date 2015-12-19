#UTXO Finder by Federico de Faveri

##Install and execute

Simply place the .py file in the directory of your choice and run "python utxoFinder.py" on your terminal window.
(You need the "requests" library installed to use this program)

##What the program does

This very simple program written in python will ask the user for a Bitcoin address.

Once the address is given the program will query the BlockChain.info API, which will scan the public bitcoin blockchain for any unspent outputs (UTXO) belonging to that address.

A JSON document containing a list of all the transactions will be received by the program, which will then iterate thru the list and print to stdout the important values for each transaction: 

1 - The Transaction ID
2 - The Transaction Index Number
3 - The Amount of BTC available to spend by the address' owner


##Understanding our BTC Wallet balance

When we look at our wallet balance we see that we have X amount of BTC available to spend, but how does the wallet software get this information since there is no central authority keeping track of our funds?


Let's say Bob is the owner of a bitcoin wallet. Bob checks his balance on BlockChain.info, a web-based BTC wallet client.

Bob's wallet balance is a collection of one or more unspent transaction outputs (UTXO) recorded in the BlockChain (The public ledger), that are "locked" to Bob, the wallet owner, by means of cryptography.
Only Bob has the correct cryptographic key to unlock these transaction outputs (UTXO) and spend them.

When Bob's wallet software (BlockChain.info in this case) gives him a "balance" it simply sums the value of all these UTXOs, which are found by scanning the public BlockChain.


I hope this was a cool insight on how the BTC wallet balance works.

Thanks for your attention!