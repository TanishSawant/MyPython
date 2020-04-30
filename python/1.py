from web3 import Web3
import json

web3 = Web3(Web3.HTTPProvider('localhost:7545'))

abi = json.loads('[{"constant": false,"inputs": [],"name": "greeting","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "_greeting","type": "string"}],"name": "setGreeting","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [],"name": "greet","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"}]')

address = web3.toChecksumAddress('0x8c1b38F157273D5d30a741532052FE857EB97a9D')

contract = web3.eth.contract(address = address, abi = abi)
print(contract.functions.greet().call())