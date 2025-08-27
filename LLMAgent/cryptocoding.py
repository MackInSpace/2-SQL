from lumibot.entities import Asset
from lumibot.backtesting import CcxtBacktesting
from lumibot.strategies.strategy import Strategy
from datetime import datetime
from colorama import Fore
import random

class MLTrader(Strategy):

    def initialize(self, cash_at_risk: float = 0.2, coin: str = 'BTC'):
        self.set_market("24/7")
        self.sleeptime = '1D'
        self.last_trade = None
        self.cash_at_risk = cash_at_risk
        self.coin = coin

    def position_sizing(self):
        cash = self.get_cash()
        last_price = self.get_last_price(
            Asset(symbol=self.coin, asset_type=Asset.AssetType.CRYPTO),
            quote=Asset(symbol='USD', asset_type="crypto")
        )
        if last_price == None:
            quantity = 0
        else:
            quantity = cash * self.cash_at_risk / last_price
        return cash, last_price, quantity
    
    def on_trading_iteration(self):
        cash, last_price, quantity = self.position_sizing()

        if last_price != None:
            if cash > (quantity * last_price):
                choice = random.choice([0, 1, 2])

                if choice == 0:
                    pass
                elif choice == 1:
                    if self.last_trade == "sell":
                        self.sell_all()