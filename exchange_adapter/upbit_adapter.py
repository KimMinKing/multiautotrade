class UpbitAdapter:
    def place_order(self, exchange, symbol, side, quantity):
        print(f"[UpbitAdapter] {side.upper()} {symbol} {quantity}개 주문 실행 (거래소: {exchange})")
