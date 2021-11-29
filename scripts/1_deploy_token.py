from brownie import ZToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

def main():
    account = get_account()
    z_token = ZToken.deploy(initial_supply, {"from": account})
    print(z_token.name())