import csv
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from src.core.bar import Bar
from src.core.bar_series import BarSeries

class CsvTradesLoader:
    @staticmethod
    def load_bitstamp_series():
        print("Starting load_bitstamp_series")
        series = BarSeries("Bitstamp Series")
        
        try:
            print("Attempting to open CSV")
            with open("resources/bitstamp_trades_from_20131125_usd.csv", "r", encoding="utf-8") as f:
                csv_reader = csv.reader(f)
                next(csv_reader)
                lines = list(csv_reader)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return series

        if not lines:
            return series

        lines.reverse()
        begin_time = datetime.fromtimestamp(int(lines[0][0]), tz=ZoneInfo("UTC"))
        end_time = datetime.fromtimestamp(int(lines[-1][0]), tz=ZoneInfo("UTC"))
        CsvTradesLoader._build_series(series, begin_time, end_time, 300, lines)
        return series

    @staticmethod
    def _build_series(series, begin_time, end_time, duration, lines):
        bar_duration = timedelta(seconds=duration)
        bar_end_time = begin_time
        i = 0

        while bar_end_time < end_time:
            bar_end_time += bar_duration
            bar = Bar(bar_duration, bar_end_time)
            
            while i < len(lines):
                trade_time = datetime.fromtimestamp(int(lines[i][0]), tz=ZoneInfo("UTC"))
                if bar.in_period(trade_time):
                    trade_price = float(lines[i][1])
                    trade_volume = float(lines[i][2])
                    bar.add_trade(trade_volume, trade_price)
                    i += 1
                else:
                    break
            
            if bar.get_trades() > 0:
                series.add_bar(bar)

    @staticmethod
    def main():
        print("Entering main")
        series = CsvTradesLoader.load_bitstamp_series()
        print(f"Series: {series.get_name()} ({series.get_series_period_description()})")
        print(f"Number of bars: {series.get_bar_count()}")
        if series.get_bar_count() > 0:
            first_bar = series.get_bar(0)
            print("First bar:")
            print(f"\tVolume: {first_bar.get_volume()}")
            print(f"\tNumber of trades: {first_bar.get_trades()}")
            print(f"\tClose price: {first_bar.get_close_price()}")

if __name__ == "__main__":
    CsvTradesLoader.main()
