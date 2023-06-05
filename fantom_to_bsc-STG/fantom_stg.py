from web3 import Web3
from web3.middleware import geth_poa_middleware
from time import sleep
import random

arbitrum_rpc_url = 'https://rpc.ankr.com/arbitrum'
fantom_rpc_url = 'https://1rpc.io/ftm'

w3 = Web3(Web3.HTTPProvider(arbitrum_rpc_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


from fantom import inch_swap, inch_allowance, inch_swap_stg, stargate


def wait_for_tx(hash, rpc):
    w3 = Web3(Web3.HTTPProvider(rpc))
    tx_receipt = None
    while tx_receipt is None:
        sleep(2)
        try:
            tx_receipt = w3.eth.get_transaction_receipt(hash)
            RandomSleep()
        except Exception as e:
            wait_for_tx(hash, rpc)
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
            
            wait_for_tx(inch_swap(fantom_rpc_url, private_key),fantom_rpc_url)
            print('Swaped FTM -> WFTM')
            wait_for_tx(inch_allowance(fantom_rpc_url, private_key),fantom_rpc_url)
            print('Create allowance')
            wait_for_tx(inch_swap_stg(fantom_rpc_url, private_key),fantom_rpc_url)
            print('Swaped WFTM -> STG')
            wait_for_tx(stargate(fantom_rpc_url, private_key),fantom_rpc_url)
            print('Swaped STG[250] -> STG[102]')

            with open('done.txt', 'a') as f:
                f.write(f'{private_key}\n')
            print(f"Done with {private_key}!")
            print('———————————————————————————————')
        print("end working with accounts.")
        sleep(999999)