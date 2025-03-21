from src.core.bar import Bar
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def test_bar_trade_addition():
    print("Running Bar trade addition test")
    bar = Bar(timedelta(seconds=300), datetime(2023, 1, 1, tzinfo=ZoneInfo("UTC")))
    bar.add_trade(1.0, 100.0)
    assert bar.get_open_price() == 100.0
    assert bar.get_high_price() == 100.0
    assert bar.get_low_price() == 100.0
    assert bar.get_close_price() == 100.0
    assert bar.get_volume() == 1.0
    assert bar.get_trades() == 1
    print("Bar trade addition test passed")