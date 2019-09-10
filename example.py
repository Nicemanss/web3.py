from web3 import Web3

node = "https://node.myhpbwallet.com"
account = "0xb0617bf785b4ce32a00bdffc7e093ad82c2e0925"
web3 = Web3(Web3.HTTPProvider(node))

print("Is connected to",node,"?",web3.isConnected(),"\n")
print("Current Block Number:",int(web3.hpb.blockNumber,16),"\n")

balance = int(web3.hpb.getBalance(account),16)
print("Account:",account,"\n")
print("Balance:",web3.fromWei(balance, "ether"),"\n")
print("Version:",web3.net.version,"\n")
print("Listening:",web3.net.listening,"\n")
print("Peer Count:",web3.net.peerCount,"\n")
print("Account:",web3.hpb.protocolVersion,"\n")
print("Is Syncing:",web3.hpb.syncing,"\n")
print("Coinbase:",web3.hpb.coinbase,"\n")
print("Mining:",web3.hpb.mining,"\n")
print("Accounts:",web3.hpb.accounts,"\n")
print("Get Transaction Count:",web3.hpb.getTransactionCount("0x407d73d8a49eeb85d32cf465507dd71d507100c1"),"\n")
print("Get Transaction Count:",web3.hpb.getBlockTransactionCount("0x3A75D3"),"\n")
print("Get Transaction Count:",web3.hpb.getBlockTransactionCount("0x14e359841aa92a9befa315d866e3f9bbf4ea09662c30538064493f31ebc4ceee"),"\n")
print("Get Uncle Count:",web3.hpb.getUncleCount("0x14e359841aa92a9befa315d866e3f9bbf4ea09662c30538064493f31ebc4ceee"),"\n")
print("Get Uncle Count:",web3.hpb.getUncleCount("0x3A75D3"),"\n")
#print(web3.hpb.sendTransaction(),"\n")
print("Get Block:",web3.hpb.getBlock("0x1b4"),"\n")
print("Get Block:",web3.hpb.getBlock("0x14e359841aa92a9befa315d866e3f9bbf4ea09662c30538064493f31ebc4ceee"),"\n")
print("Get Transaction:",web3.hpb.getTransaction("0x7f19c141e526066d92331a4ecad637251e8f9d986faf3d79160b16c310c0a86a"),"\n")
print("Get Transaction:",web3.hpb.getTransactionByBlock("0x14e359841aa92a9befa315d866e3f9bbf4ea09662c30538064493f31ebc4ceee", "0x0"),"\n")
print("Get Transaction:",web3.hpb.getTransactionByBlock("0x3A75D3", "0x0"),"\n")
print("Get Transaction:",web3.hpb.getTransactionReceipt("0x7f19c141e526066d92331a4ecad637251e8f9d986faf3d79160b16c310c0a86a"),"\n")
print("Created new Account:",web3.hpb.newAccount('12345678'))
