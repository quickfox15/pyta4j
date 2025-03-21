from src.loaders.csv_trades_loader import CsvTradesLoader
from src.indicators.close_price_indicator import ClosePriceIndicator
from src.indicators.sma_indicator import SMAIndicator

def main():
    # Load the bar series
    series = CsvTradesLoader.load_bitstamp_series()

    # Get the close price of the first bar
    first_close_price = series.get_bar(0).close_price
    print(f"First close price: {first_close_price}")

    # Use ClosePriceIndicator
    close_price = ClosePriceIndicator(series)
    print(f"First close price matches indicator: {first_close_price == close_price.get_value(0)}")

    # Calculate 5-bar SMA
    short_sma = SMAIndicator(close_price, 5)
    print(f"5-bars-SMA value at the 2nd index: {short_sma.get_value(2)}")  # New
    print(f"5-bars-SMA value at the 42nd index: {short_sma.get_value(42)}")


    print(f"5-bars-SMA (NumPy) at 42: {short_sma.get_value_numpy(42)}")
    print(f"5-bars-SMA (pandas) at 42: {short_sma.get_value_pandas(42)}")

if __name__ == "__main__":
    main()