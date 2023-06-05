# testbridge optisim to goerli 

from web3.middleware import geth_poa_middleware
from web3 import Web3
import json
import requests

def testbridge(rpc_link, privatekey):
    w3 = Web3(Web3.HTTPProvider(rpc_link))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    account = w3.eth.account.from_key(privatekey)
    contract_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_weth","type":"address"},{"internalType":"address","name":"_oft","type":"address"},{"internalType":"address","name":"_swapRouter","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"oft","outputs":[{"internalType":"contract IOFTCore","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolFee","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"uint16","name":"dstChainId","type":"uint16"},{"internalType":"address","name":"to","type":"address"},{"internalType":"address payable","name":"refundAddress","type":"address"},{"internalType":"address","name":"zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"adapterParams","type":"bytes"}],"name":"swapAndBridge","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"swapRouter","outputs":[{"internalType":"contract ISwapRouter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"weth","outputs":[{"internalType":"contract IWETH","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
    contract_address = '0x0A9f824C05A74F577A536A8A0c673183a872Dff4'
    swap_contract = w3.eth.contract(contract_address, abi=contract_abi) # type: ignore

    amountIn = w3.to_wei(0.00007, 'ether')
    amountOutMin = w3.to_wei(1.10, 'ether')
    dstChainId = 154
    adapterParams = ''



    transaction = swap_contract.functions.swapAndBridge(
        amountIn, amountOutMin, dstChainId, account.address, account.address, '0x0000000000000000000000000000000000000000', adapterParams 
        ).build_transaction({
                'from': account.address,
                'value': amountIn,  # ???
                'gas': 2000000,
                'gasPrice': w3.eth.gas_price,
                'nonce': w3.eth.get_transaction_count(account.address),
        })
    print(transaction)

#need 2 review