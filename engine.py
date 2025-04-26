import time
import threading
from datetime import datetime
from utils.logger import logger
from utils.time_utils import should_execute_strategy
class Engine:
    def __init__(self, strategy_manager, order_manager, event_dispatcher):
        self.strategy_manager = strategy_manager
        self.order_manager = order_manager
        self.event_dispatcher = event_dispatcher
        self.is_running = False
        self.thread = None

    def start(self):
        self.is_running = True
        logger.info("자동매매 엔진 시작합니다...")
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        while self.is_running:
            now = datetime.now()

            for strategy in self.strategy_manager.get_strategies():
                # logger.info(f"전략 체크 중: {strategy.name}")

                if should_execute_strategy(strategy, now):
                    threading.Thread(target=self.execute_strategy, args=(strategy,), daemon=True).start()

            self.event_dispatcher.handle_events()
            time.sleep(1)



    def execute_strategy(self, strategy):
        """전략을 비동기로 실행"""
        try:
            # 실제 데이터 받아와야 하는데, 지금은 예시 데이터
            fake_data = [123, 456]
            if strategy.should_run(fake_data):
                strategy.execute(fake_data)
                logger.info(f"{strategy.name} 실행 완료")
        except Exception as e:
            logger.error(f"{strategy.name} 실행 중 오류 발생: {e}")

    def wait_for_finish(self):
        if self.thread is not None:
            self.thread.join()
