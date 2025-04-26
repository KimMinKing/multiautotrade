class ExchangeAdapterFactory:
    def __init__(self):
        pass

    def get_adapter(self, exchange_name):
        if exchange_name == 'upbit':
            from .upbit_adapter import UpbitAdapter
            return UpbitAdapter()
        else:
            raise ValueError(f"Unknown exchange: {exchange_name}")
