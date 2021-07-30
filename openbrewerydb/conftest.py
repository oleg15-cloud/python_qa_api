import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://api.openbrewerydb.org",
        help="This is request url for Dog app"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")
