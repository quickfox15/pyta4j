class BarSeries:
    def __init__(self, name="Unnamed Series"):
        self.name = name
        self.bars = []
    
    def add_bar(self, bar):
        if bar.get_trades() > 0:
            self.bars.append(bar)
    
    def get_bar(self, index):
        return self.bars[index]
    
    def get_bar_count(self):
        return len(self.bars)
    
    def get_name(self):
        return self.name
    
    def get_series_period_description(self):
        if not self.bars:
            return "Empty Series"
        start = self.bars[0].get_end_time()
        end = self.bars[-1].get_end_time()
        return f"{start} - {end}"
    
    def function(self):  # Placeholder for NumFunction in TA4J
        return lambda x: x  # Identity function for now