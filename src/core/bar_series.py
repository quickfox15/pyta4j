class BarSeries:
    def __init__(self, name):
        self.name = name
        self.bars = []

    def add_bar(self, bar):
        self.bars.append(bar)

    def get_bar_count(self):
        return len(self.bars)

    def get_bar(self, index):
        return self.bars[index]

    def get_name(self):
        return self.name

    def get_series_period_description(self):
        if not self.bars:
            return "(empty)"
        return f"{self.bars[0].end_time} - {self.bars[-1].end_time}"