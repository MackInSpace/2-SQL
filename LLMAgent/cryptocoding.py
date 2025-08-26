from lumibot.entities import Assets
from lumibot.backtesting import CcxtBacktesting
from lumibot.strategies.strategy import Strategy
from datetime import datetime
from colorama import Fore
import random

class MLTrader(Strategy):

    def initialize(self, cash_at_risk: float = 0.2, coin: str = 'BTC'):
        self.set_market("24/7")