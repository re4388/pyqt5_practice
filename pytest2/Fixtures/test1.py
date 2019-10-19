from highest_rated import (
	highest_rated,
	oldest,
)


def test_highest_rated():
    series = [
        ("The Office", 2005, 8.8),
        ("Scrubs", 2001, 8.4),
        ("IT Crowd", 2006, 8.5),
        ("Parks and Recreation", 2009, 8.6),
        ("Seinfeld", 1989, 8.9),
    ]
    assert highest_rated(series) == "Seinfeld"

def test_oldest():
    series = [
            ("The Office", 2005, 8.8),
            ("Scrubs", 2001, 8.4),
            ("IT Crowd", 2006, 8.5),
            ("Parks and Recreation", 2009, 8.6),
            ("Seinfeld", 1989, 8.9),
        ]
assert oldest(series) == "Seinfeld"


################### below use fixture  ############################################

@pytest.fixture
def comedy_series():
    return [
        ("The Office", 2005, 8.8),
        ("Scrubs", 2001, 8.4),
        ("IT Crowd", 2006, 8.5),
        ("Parks and Recreation", 2009, 8.6),
        ("Seinfeld", 1989, 8.9),
    ]

def test_highest_rated(comedy_series):
    assert highest_rated(comedy_series) == "Seinfeld"

def test_oldest(comedy_series):
    assert oldest(comedy_series) == "Seinfeld"






@pytest.fixture(autouse=True)
def setup_locale():
    locale.setlocale(locale.LC_ALL, "en_US")
    yield
    locale.setlocale(locale.LC_ALL, None)

def test_currency_us():
    assert locale.currency(10.5) == "$10.50"






def test_empty(tmpdir):
    assert os.path.isdir(tmpdir)
    assert os.listdir(tmpdir) == []


def test_save_curves(tmpdir):
    data = dict(status_code=200, values=[225, 300])
    fn = tmpdir.join('somefile.json')
    write_json(fn, data)
    assert fn.read() == '{"status_code": 200, "values": [225, 300]}'


@pytest.fixture(scope='session')
def images_dir(tmpdir_factory):
    directory = tmpdir_factory.mktemp('images')
    download_images('https://example.com/samples.zip', directory)
    extract_images(directory / 'samples.zip')
    return directory

def test_blur_filter(images_dir):
    output_image = apply_blur_filter(images_dir / 'rock1.png')
    # ...


import getpass

def user_login(name):
    password = getpass.getpass()
    check_credentials(name, password)
    # ...

def test_login_success(monkeypatch):
    monkeypatch.setattr(getpass, "getpass", lambda: "valid-pass")
    assert user_login("test-user")

def test_login_wrong_password(monkeypatch):
    monkeypatch.setattr(getpass, "getpass", lambda: "wrong-pass")
    with pytest.raises(AuthenticationError, match="wrong password"):
        user_login("test-user")



import subprocess
def start_service(service_name):
    subprocess.run(f"docker run {service_name}")


import subprocess
import services

def test_start_service(monkeypatch):
    commands = []
    monkeypatch.setattr(subprocess, "run", commands.append)
    services.start_service("web")
    assert commands == ["docker run web"]


from textwrap import dedent

def script_main(args):
    if not args:
        show_usage()
        return 0
        # ...

def show_usage():
    print("Create/update webhooks.")
    print(" Usage: hooks REPO URL")

def test_usage(capsys):
    script_main([])
    captured = capsys.readouterr()
    assert captured.out == dedent("""\
                                Create/update webhooks.
                                Usage: hooks REPO URL
                                """)



@pytest.fixture
def tmp_path(request) -> Path:
    with TemporaryDirectory(prefix=request.node.name) as d:
        yield Path(d)

def test_tmp_path(tmp_path):
    assert list(tmp_path.iterdir()) == []




class WindowManager:
    pass


@pytest.fixture
def manager():
    return WindowManager()

def test_windows_creation(manager):
    window = manager.new_help_window("pipes_help.rst")
    assert window.title() == "Pipe Setup Help"


def create_window_manager():
    return WindowManager()

def test_windows_creation():
    manager = create_window_manager()
    window = manager.new_help_window("pipes_help.rst")
    assert window.title() == "Pipe Setup Help"

def test_windows_creation():
    manager = WindowManager()
    window = manager.new_help_window("pipes_help.rst")
    assert window.title() == "Pipe Setup Help"