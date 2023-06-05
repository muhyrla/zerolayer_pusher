### Features

- Spread native around chains
- Bridge tokens FTM -> BSC

# Interact with LayerZero projects

![](https://seeklogo.com/images/L/layerzero-network-logo-E5BFAD4B57-seeklogo.com.png?v=637922930860000000)


Before using, you should install web3 lib:

    pip install web3

# [Fantom --> BSC using STG token](https://github.com/muhyrla/zerolayer_pusher/tree/main/fantom_to_bsc-STG)

### Additional install

    pip install requests

Download **everything** from folder in heading, and create

**privatekeys.txt**

and keep all private keys in there, they **should contain at least 3 $FTM**


we use 1inch to swap FTM -> WFTM -> STG
we use stargate to bridge STG[FTM] -> STG[BSC]

so this will finally count as interaction with L0.

# [Spread native from Arbitrum on other chains](https://github.com/muhyrla/zerolayer_pusher/blob/main/bungee_arb.py)

Download everything from folder in heading, and create

**privatekeys.txt**

and keep all private keys in there, they should contain native token, to proceed


------------
You can edit value you need to swap in native (base is 1$)
https://github.com/muhyrla/zerolayer_pusher/blob/89681d874d788ca50ae3c22fcd616ca6f984a7ea/bungee_arb.py#L17-L22

You can edit chains you need to spread
https://github.com/muhyrla/zerolayer_pusher/blob/89681d874d788ca50ae3c22fcd616ca6f984a7ea/bungee_arb.py#L106


------------



