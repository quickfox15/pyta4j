from datetime import timedelta

class Bar:
    def __init__(self, duration, end_time):
        self.duration = duration
        self.end_time = end_time
        self.trades = 0
        self.volume = 0.0
        self.open_price = None
        self.high_price = None
        self.low_price = None
        self.close_price = None

    def in_period(self, timestamp):
        start_time = self.end_time - self.duration
        return start_time <= timestamp < self.end_time  # Matches TA4J

    def add_trade(self, volume, price):
        self.trades += 1
        self.volume += volume
        if self.open_price is None:
            self.open_price = price
        self.high_price = max(self.high_price or price, price)
        self.low_price = min(self.low_price or price, price)
        self.close_price = price