# main.py

from strategy_manager import StrategyManager
from engine import Engine
from order_manager import OrderManager
from event_dispatcher import EventDispatcher
from console_ui import ConsoleUI
from utils.logger import logger
import time

def main():
    strategy_manager = StrategyManager()
    order_manager = OrderManager()
    event_dispatcher = EventDispatcher()
    engine = Engine(strategy_manager, order_manager, event_dispatcher)
    console_ui = ConsoleUI()

    user_choice = console_ui.get_user_choice()
    
    if user_choice == "existing":
        strategy_manager.add_existing_strategies()
        logger.info("기존 전략이 추가되었습니다.")
        engine.start()

        # 여기를 이렇게 바꾼다
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Ctrl+C 감지됨. 엔진을 종료합니다...")
            engine.is_running = False  # 엔진 멈춤
            logger.info("프로그램이 종료되었습니다.")

    elif user_choice == "exit":
        logger.info("프로그램을 종료합니다.")
        return
    else:
        logger.error("잘못된 선택입니다.")

if __name__ == "__main__":
    main()
