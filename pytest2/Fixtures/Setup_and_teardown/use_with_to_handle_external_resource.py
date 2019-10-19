@pytest.fixture
def comedy_series():
    file = open("series.csv", "r", newline="")
    return list(csv.reader(file))

@pytest.fixture
def some_fixture():
    value = setup_value()
    yield value
    teardown_value(value)


@pytest.fixture
def comedy_series():
    file = open("series.csv", "r", newline="")
    yield list(csv.reader(file))
    file.close()

@pytest.fixture
def comedy_series():
    with open("series.csv", "r", newline="") as file:
    return list(csv.reader(file))