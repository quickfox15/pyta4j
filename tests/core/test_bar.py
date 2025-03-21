from src.core.bar import Bar
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def test_bar_trade_addition():
    print("Running Bar trade addition test")
    bar = Bar(timedelta(seconds=300), datetime(2023, 1, 1, tzinfo=ZoneInfo("UTC")))
    bar.add_trade(1.0, 100.0)
    assert bar.open_price == 100.0
    assert bar.high_price == 100.0
    assert bar.low_price == 100.0
    assert bar.close_price == 100.0
    assert bar.volume == 1.0
    assert bar.trades == 1
    print("Bar trade addition test passed")
    