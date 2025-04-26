# order_manager.py

class OrderManager:
    def __init__(self):
        self.orders = []  # 주문 목록

    def place_order(self, order):
        # 주문 전송 로직 구현
        print(f"주문 전송: {order}")
        self.orders.append(order)

    def cancel_order(self, order_id):
        # 주문 취소 로직 구현
        print(f"주문 취소: {order_id}")
        self.orders = [order for order in self.orders if order['id'] != order_id]

    def get_orders(self):
        # 현재 진행 중인 주문 반환
        return self.orders
