from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

class Bar:
    def __init__(self, duration, end_time):
        self.duration = duration  # timedelta
        self.end_time = end_time  # datetime with timezone
        self.open_price = 0.0
        self.high_price = 0.0
        self.low_price = float("inf")
        self.close_price = 0.0
        self.volume = 0.0
        self.trades = 0
    
    def add_trade(self, volume, price):
        self.trades += 1
        self.volume += volume
        self.open_price = price if self.trades == 1 else self.open_price
        self.high_price = max(self.high_price, price)
        self.low_price = min(self.low_price, price)
        self.close_price = price  # Last trade’s price
    
    def in_period(self, timestamp):
        start_time = self.end_time - self.duration
        return start_time <= timestamp <= self.end_time
    
    def get_open_price(self):
        return self.open_price
    
    def get_high_price(self):
        return self.high_price
    
    def get_low_price(self):
        return self.low_price
    
    def get_close_price(self):
        return self.close_price
    
    def get_volume(self):
        return self.volume
    
    def get_trades(self):
        return self.trades
    
    def get_end_time(self):
        return self.end_time