from web3 import Web3

node = "https://node.myhpbwallet.com"
account = "0xb0617bf785b4ce32a00bdffc7e093ad82c2e0925"
web3 = Web3(Web3.HTTPProvider(node))

print("Is connected to",node,"?",web3.isConnected())
print("Current Block Number:",int(web3.hpb.blockNumber,16))

balance = int(web3.hpb.getBalance(account),16)
print("Account:",account)
print("Balance:",web3.fromWei(balance, "ether"))
