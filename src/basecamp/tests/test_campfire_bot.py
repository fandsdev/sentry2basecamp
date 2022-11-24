import pytest

from basecamp.campfire_bot import CampfireBot
from httpx._exceptions import HTTPStatusError


@pytest.fixture
def success_response(httpx_mock):
    httpx_mock.add_response(
        method='POST',
        status_code=200,
    )


@pytest.fixture
def bad_response(httpx_mock):
    httpx_mock.add_response(
        method='POST',
        status_code=400,
    )


@pytest.fixture
def bot():
    return CampfireBot()


@pytest.mark.usefixtures('success_response')
def test_good_response(bot):
    result = bot.send_message('Hello World!')

    assert result.status_code == 200


@pytest.mark.usefixtures('bad_response')
def test_bad_response(bot):
    with pytest.raises(HTTPStatusError):
        bot.send_message('Hello World!')
