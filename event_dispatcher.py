# event_dispatcher.py

class EventDispatcher:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        # 새로운 이벤트 추가
        print(f"이벤트 추가: {event}")
        self.events.append(event)

    def handle_events(self):
        # 이벤트 처리 (예: 주문 발생 시)
        for event in self.events:
            print(f"이벤트 처리: {event}")
            # 실제 이벤트 처리 로직 추가
        self.events.clear()  # 처리된 이벤트 삭제
