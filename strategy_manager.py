# strategy_manager.py
from strategies.bollinger_band_1m import BollingerBand1mStrategy
from strategies.ema_cross_15m import EMACross15mStrategy
from utils.logger import logger

class StrategyManager:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)
        logger.info(f"[{strategy.name}] 전략이 추가되었습니다.")
    
    def add_existing_strategies(self):
        # 기존 전략을 임시로 추가
        bb_strategy = BollingerBand1mStrategy()
        ema_strategy = EMACross15mStrategy(15)

        self.add_strategy(bb_strategy)
        self.add_strategy(ema_strategy)

    def get_strategies(self):
        return self.strategies
