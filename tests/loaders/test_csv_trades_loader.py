from src.loaders.csv_trades_loader import CsvTradesLoader

def test_csv_trades_loader(capsys):
    CsvTradesLoader.main()
    captured = capsys.readouterr()
    assert "Series: Bitstamp Series" in captured.out
    assert "Number of bars:" in captured.out
    # If CSV is present, we could add more specific checks later
