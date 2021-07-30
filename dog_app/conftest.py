import pytest

from dog_app.test_data.test_data import list_of_breeds


@pytest.fixture(params=list_of_breeds)
def param_fixture(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://dog.ceo",
        help="This is request url for Dog app"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")
