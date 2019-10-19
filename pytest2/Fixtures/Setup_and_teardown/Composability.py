@pytest.fixture
def series():
    with open("series.csv", "r", newline="") as file:
        return list(csv.reader(file))

@pytest.fixture
    def comedy_series(series):
        return [x for x in series if x[GENRE] == "comedy"]


def test_highest_rated(comedy_series):
    assert highest_rated(comedy_series) == "Seinfeld"

def test_oldest(comedy_series):
    assert oldest(comedy_series) == "Seinfeld"