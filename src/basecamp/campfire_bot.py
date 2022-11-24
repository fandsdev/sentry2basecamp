import httpx
from httpx._models import Response

from config import get_settings

settings = get_settings()


class CampfireBot:
    def send_message(self, message: str) -> Response:
        """ https://github.com/basecamp/bc3-api/blob/master/sections/chatbots.md#create-a-line """

        url = f'https://3.basecampapi.com/{settings.BASECAMP_ACCOUNT_ID}/integrations/{settings.BASECAMP_CHATBOT_KEY}/buckets/1/chats/2/lines.json'

        response = httpx.post(url, data={'content': message})
        response.raise_for_status()

        return response
