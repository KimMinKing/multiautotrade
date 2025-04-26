# engine.py

import time
import threading
from utils.logger import logger

class Engine:
    def __init__(self, strategy_manager, order_manager, event_dispatcher):
        self.strategy_manager = strategy_manager
        self.order_manager = order_manager
        self.event_dispatcher = event_dispatcher
        self.is_running = False
        self.thread = None  # <- 스레드 객체 저장할 변수 추가

    def start(self):
        self.is_running = True
        logger.info("자동매매 엔진 시작합니다...")
        self.thread = threading.Thread(target=self.run)  # daemon 지움
        self.thread.start()

    def run(self):
        while self.is_running:
            logger.info("엔진 실행 중...")

            for strategy in self.strategy_manager.get_strategies():
                logger.info(f"전략 실행 중: {strategy.name}")

                if strategy.should_run([123, 456]):  # 예시
                    strategy.execute([123, 456])

            self.event_dispatcher.handle_events()
            time.sleep(1)

    def wait_for_finish(self):
        if self.thread is not None:
            self.thread.join()  # <- 메인에서 기다릴 때 사용
