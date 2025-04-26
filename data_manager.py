class DataManager:
    def __init__(self):
        pass
    def fetch(self):
        print('[DataManager] 데이터 수집')
        # 가짜 데이터 리턴
        return {'BTC/USDT': {'price': 70000}}
    def get_price(self, symbol, interval):
        pass
    def get_balance(self, adapter):
        pass