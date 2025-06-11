import requests
import time
from typing import List, Optional, Callable
from dataclasses import dataclass
from datetime import datetime

class MailTmProvider:
    API_BASE = "https://api.mail.tm"

    def __init__(self):
        self.session = requests.Session()
        self.account = self.create_account()
        self.token = self.get_token()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def create_account(self):
        # Get available domains
        domains_resp = self.session.get(f"{self.API_BASE}/domains")
        domains_resp.raise_for_status()
        domains = domains_resp.json()["hydra:member"]
        domain = domains[0]["domain"]

        # Generate random username
        import random, string
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        address = f"{username}@{domain}"

        # Create account
        data = {"address": address, "password": "Password123!"}
        resp = self.session.post(f"{self.API_BASE}/accounts", json=data)
        resp.raise_for_status()
        return data

    def get_token(self):
        data = {"address": self.account["address"], "password": self.account["password"]}
        resp = self.session.post(f"{self.API_BASE}/token", json=data)
        resp.raise_for_status()
        return resp.json()["token"]

    def get_inbox(self) -> List['MailTmProvider.Message']:
        resp = self.session.get(f"{self.API_BASE}/messages")
        resp.raise_for_status()
        messages = resp.json()["hydra:member"]
        full_messages = []
        for msg in messages:
            full_msg = self.get_message_detail(msg["id"])
            full_messages.append(full_msg)
        return full_messages

    def get_message_detail(self, message_id: str) -> 'MailTmProvider.Message':
        resp = self.session.get(f"{self.API_BASE}/messages/{message_id}")
        resp.raise_for_status()
        data = resp.json()
        return self.Message.from_dict(data)

    def wait_for_message(self, timeout: Optional[int] = 60,
                         filter: Callable[['MailTmProvider.Message'], bool] = lambda _: True) -> 'MailTmProvider.Message':
        timeout_time = time.time() + timeout if timeout is not None else None
        while timeout is None or time.time() < timeout_time:
            inbox = self.get_inbox()
            for msg in inbox:
                if filter(msg):
                    return msg
            time.sleep(5)
        raise TimeoutError("Timed out waiting for message")

    @dataclass
    class Message:
        id: str
        from_addr: str
        subject: str
        intro: str
        text: str
        html: str
        date: datetime

        @classmethod
        def from_dict(cls, data):
            return cls(
                id=data["id"],
                from_addr=data["from"]["address"],
                subject=data["subject"],
                intro=data.get("intro", ""),
                text=data.get("text", ""),
                html=data.get("html", ""),
                date=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
            )
