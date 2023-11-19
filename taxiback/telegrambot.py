import datetime
from django.conf import settings
import requests


class TelegramBot:
    def __init__(self, chat_id: str, token: str = settings.TOKEN_BOT) -> None:
        self.chat_id = chat_id
        self.token = token
        self.url = f"https://api.telegram.org/bot{self.token}"
        self.max_length_text = 1024

    def send(self, url: str, data: dict, files: bytes = None) -> requests.Response:
        res = requests.post(url, data=data, files=files)
        return res

    def send_message(self, text: str, parse_mode: str = None) -> requests.Response:
        return self.send(
            url=f"{self.url}/sendMessage",
            data={
                "parse_mode": parse_mode,
                "chat_id": self.chat_id,
                "text": text[: self.max_length_text] if len(text) > self.max_length_text else text,
            },
        )

    def send_error_message_from_response(self, response: requests.Response) -> requests.Response:
        try:
            body = response.json()
        except Exception:
            body = response.text

        text = f"""Ошибка при отправке бонусов
        Тело: {body}
        Статус: {response.status_code}
        Дата и время отправки: {datetime.now()}
        """
        return self.send_message(text)

    def send_file(self, files: str, caption: str = "") -> requests.Response:
        return self.send(
            url=f"{self.url}/sendDocument", data={"chat_id": self.chat_id, "caption": caption}, files=files
        )