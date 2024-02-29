from brownie import FundMe

from utils import get_account


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account})
    print(fund_me)


def main():
    deploy_fund_me()
