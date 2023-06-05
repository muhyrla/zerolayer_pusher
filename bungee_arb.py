from web3 import Web3
import json
from web3.middleware import geth_poa_middleware
from time import sleep
import random

arbitrum_rpc_url = 'https://rpc.ankr.com/arbitrum'            # Если не нравится анкр, поменяйте на любую другую

w3 = Web3(Web3.HTTPProvider(arbitrum_rpc_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def bugee_refuel(rpc_link, privatekey, chainid):
    w3 = Web3(Web3.HTTPProvider(rpc_link))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    account = w3.eth.account.from_key(privatekey)
    
    amount_to_swap = 0.00053  # тута менять сколько арб менять, можете прописать условие как чуть ниже, если на определенную сеть нужно больше(меньше)

    # if chainid == NEEDED_CHAIN_ID 
    #     amount_to_swap = 0.0011
    # else:
    #     amount_to_swap = 0.00053 

    # CONTRACT SECTION
    contract_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"destinationReceiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"destinationChainId","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Donation","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sender","type":"address"}],"name":"GrantSender","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sender","type":"address"}],"name":"RevokeSender","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes32","name":"srcChainTxHash","type":"bytes32"}],"name":"Send","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdrawal","type":"event"},{"inputs":[{"components":[{"internalType":"uint256","name":"chainId","type":"uint256"},{"internalType":"bool","name":"isEnabled","type":"bool"}],"internalType":"struct GasMovr.ChainData[]","name":"_routes","type":"tuple[]"}],"name":"addRoutes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable[]","name":"receivers","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes32[]","name":"srcChainTxHashes","type":"bytes32[]"},{"internalType":"uint256","name":"perUserGasAmount","type":"uint256"},{"internalType":"uint256","name":"maxLimit","type":"uint256"}],"name":"batchSendNativeToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"chainConfig","outputs":[{"internalType":"uint256","name":"chainId","type":"uint256"},{"internalType":"bool","name":"isEnabled","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"destinationChainId","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"depositNativeToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"chainId","type":"uint256"}],"name":"getChainData","outputs":[{"components":[{"internalType":"uint256","name":"chainId","type":"uint256"},{"internalType":"bool","name":"isEnabled","type":"bool"}],"internalType":"struct GasMovr.ChainData","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"}],"name":"grantSenderRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"processedHashes","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"}],"name":"revokeSenderRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes32","name":"srcChainTxHash","type":"bytes32"},{"internalType":"uint256","name":"perUserGasAmount","type":"uint256"},{"internalType":"uint256","name":"maxLimit","type":"uint256"}],"name":"sendNativeToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"senders","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"chainId","type":"uint256"},{"internalType":"bool","name":"_isEnabled","type":"bool"}],"name":"setIsEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"setPause","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"setUnPause","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawBalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"}],"name":"withdrawFullBalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
    contract_address = '0xc0E02AA55d10e38855e13B64A8E1387A04681A00'
    swap_contract = w3.eth.contract(contract_address, abi=contract_abi)
    
    # RANDOM SECTION
    random_path = random.uniform(0.00000001,0.000001)
    random_gas = random.randint(1000,200000)

    # TRANSACTION ARGUMENTS
    value = w3.to_wei(amount_to_swap+random_path, 'ether') 
    toaddress = account.address

    # TRANSACTION FORMING
    try:
        transaction = swap_contract.functions.depositNativeToken(
            chainid, toaddress
        ).build_transaction({
            'from': account.address,
            'value': value,
            'gas': 2700000+random_gas,
            'gasPrice': w3.eth.gas_price,
            'nonce': w3.eth.get_transaction_count(account.address),
        })

        signed_tx = w3.eth.account.sign_transaction(transaction, privatekey)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash
    except:
        print("Error during sending tx. Trying again... [NO_NATIVE_SPENDED]")
        sleep(10)
        return bugee_refuel(rpc_link,privatekey,chainid,amount_to_swap)
    

class RandomChainId:
    def __init__(self, data):
        self.data = data

    def process_chain(self):
        if self.data:
            random_value = random.choice(self.data)
            self.data.remove(random_value)
            return random_value
        else:
            return None


def wait_for_tx(hash, rpc):
    w3 = Web3(Web3.HTTPProvider(rpc))
    tx_receipt = None
    while tx_receipt is None:
        sleep(2)
        tx_receipt = w3.eth.get_transaction_receipt(hash)
    if tx_receipt.status == 0:
        print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print("WARN! Something went wrong, probably you need to check.")
        print(tx_receipt.transactionHash.hex())
        print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        sleep(99999)
        return False
    else:
        return True


class RandomSleep:
    def __init__(self):
        pass

    def sleep(self):
        sleep_time = random.randint(1, 5)
        sleep(sleep_time)


if __name__ == "__main__":
    with open('privatekeys.txt', 'r') as f:
        private_keys = f.readlines()
    print("Starting...")
    rs = RandomSleep()
    if w3.is_connected():
        for private_key in private_keys:
            private_key = private_key.replace('\n', '')
            chain_list = []                                     # Сети по которым надо раскидать, учитывайте, что они должны быть в банги, айди смотреть https://chainlist.org/
            chains = RandomChainId(chain_list)
            
            wait_for_tx(bugee_refuel(arbitrum_rpc_url,private_key,chains.process_chain()),arbitrum_rpc_url)
            print('Successfully sent for Bungee')
            rs.sleep()
            wait_for_tx(bugee_refuel(arbitrum_rpc_url,private_key,chains.process_chain()),arbitrum_rpc_url)
            print('Successfully sent for Bungee')
            rs.sleep()
            wait_for_tx(bugee_refuel(arbitrum_rpc_url,private_key,chains.process_chain()),arbitrum_rpc_url)
            print('Successfully sent for Bungee')
            rs.sleep()

            with open('done.txt', 'a') as f:
                f.write(f'{private_key}\n')
            print(f"Done with {private_key}!")
            print('-----------------------------------')
        print("Done!")
        sleep(999999)