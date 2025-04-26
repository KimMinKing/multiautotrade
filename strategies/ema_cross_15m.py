# strategies/ema_cross_15m.py
class EMACross15mStrategy:
    def __init__(self, interval_minutes=15):
        self.interval_minutes = interval_minutes
        self.name = "EMA Cross 15m Strategy"
    
    def should_run(self, data):
        # 15분봉 EMA 교차 전략 구현
        return True  # 실제 로직으로 교체

    def execute(self, data):
        # 전략 실행 (매매/시그널 발송)
        pass
