from web3.middleware import geth_poa_middleware
from web3 import Web3
import json
import requests
from time import sleep


def stargate(rpc_link, privatekey):
    w3 = Web3(Web3.HTTPProvider(rpc_link))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    account = w3.eth.account.from_key(privatekey)
    contract_address = '0xbf22f0f184bCcbeA268dF387a49fF5238dD23E40'
    contract_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_stargateEthVault","type":"address"},{"internalType":"address","name":"_stargateRouter","type":"address"},{"internalType":"uint16","name":"_poolId","type":"uint16"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"addLiquidityETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"poolId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stargateEthVault","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stargateRouter","outputs":[{"internalType":"contract IStargateRouter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256","name":"_amountLD","type":"uint256"},{"internalType":"uint256","name":"_minAmountLD","type":"uint256"}],"name":"swapETH","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
    swap_contract = w3.eth.contract(address = contract_address, abi = contract_abi)

    api_endpoint = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
    response = requests.get(api_endpoint)
    eth_price = response.json()['ethereum']['usd']
    
    stargate_fee = (1/eth_price)*1.5
    balance = w3.eth.get_balance(account.address)
    value = w3.to_wei('0.00212175', 'ether')

    transaction = swap_contract.functions.swapETH(
        111, account.address, account.address, w3.to_wei(0.0008, 'ether'), w3.to_wei(0.00078, 'ether')
    ).build_transaction({
            'from': account.address,
            'value': value,
            'gas': 3300000,
            'gasPrice': w3.eth.gas_price,
            'nonce': w3.eth.get_transaction_count(account.address),
    })

    try:
        signed_tx = w3.eth.account.sign_transaction(transaction, privatekey)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash 
    except Exception as e:
        print("Error during sending tx. Trying again... [NO_NATIVE_SPENDED]")
        sleep(10)
        return stargate(rpc_link, privatekey)