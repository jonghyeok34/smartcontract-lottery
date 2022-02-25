import time
import pytest
from scripts.deploy_lottery import deploy_lottery
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, fund_with_link, get_account
from brownie import network


GAS_LIMIT_WEI = 1 * (10 ** 8) if network.show_active() =="rinkeby" else 6721975

def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from": account, "gas_limit": GAS_LIMIT_WEI, "allow_revert":True})
    lottery.enter({"from": account , "value": lottery.getEntranceFee(), "gas_limit": GAS_LIMIT_WEI})
    fund_with_link(lottery)    
    lottery.endLottery({"from": account, "gas_limit": GAS_LIMIT_WEI, "allow_revert":True})
    time.sleep(60)
    
    assert lottery.recentWinner() == account
    assert lottery.balance == 0