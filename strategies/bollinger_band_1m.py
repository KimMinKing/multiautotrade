# strategies/bollinger_band_1m.py
class BollingerBand1mStrategy:
    def __init__(self):
        self.name = "Bollinger Band 1m Strategy"
    
    def should_run(self, data):
        # 1분봉 볼린저 밴드 전략 구현
        # 예시: 볼린저 밴드 기준으로 매수/매도 시그널 발생 여부 확인
        return True  # 실제 로직으로 교체

    def execute(self, data):
        # 전략 실행 (매매/시그널 발송)
        pass
