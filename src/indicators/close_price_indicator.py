class ClosePriceIndicator:
    def __init__(self, series):
        self.series = series

    def get_value(self, index):
        return self.series.get_bar(index).close_price