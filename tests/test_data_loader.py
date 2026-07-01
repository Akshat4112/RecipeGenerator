from data_loader import load_recipes


def test_load_recipes_returns_dataframe():
    df = load_recipes()
    assert len(df) > 0
    expected_cols = {"Url", "Instructions", "Ingredients", "Day", "Name", "Year", "Month", "Weekday"}
    assert expected_cols.issubset(set(df.columns))


def test_load_recipes_drops_index_columns():
    df = load_recipes()
    assert "Unnamed: 0" not in df.columns
    assert "index" not in df.columns
