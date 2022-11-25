import httpx
from httpx._models import Response

from config import get_settings

settings = get_settings()


class CampfireBot:

    @staticmethod
    def send_message(message: str) -> Response:
        """ https://github.com/basecamp/bc3-api/blob/master/sections/chatbots.md#create-a-line """

        url = f'https://3.basecampapi.com/{settings.BASECAMP_ACCOUNT_ID}/integrations/{settings.BASECAMP_CHATBOT_KEY}/buckets/{settings.BASECAMP_PROJECT_ID}/chats/{settings.BASECAMP_CHAT_ID}/lines.json'

        response = httpx.post(url, data={'content': message})
        response.raise_for_status()

        return response
