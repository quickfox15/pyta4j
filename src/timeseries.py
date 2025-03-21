import numpy as np

class TimeSeries:
    def __init__(self, prices):
        self.prices = np.array(prices)

    def get_price(self, index):
        return self.prices[index]

if __name__ == "__main__":
    ts = TimeSeries([1, 2, 3])
    print(ts.get_price(1))  # Should print 2
