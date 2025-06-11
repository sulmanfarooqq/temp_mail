import time
import random
import string
from typing import List, Optional, Callable
from dataclasses import dataclass
from datetime import datetime

class MockTempMail:
    def __init__(self):
        self.username = ''.join(random.choices(string.ascii_lowercase, k=10))
        self.domain = 'mockmail.com'
        self.address = f'{self.username}@{self.domain}'
        self._inbox = []
        self._message_id = 0

    def get_inbox(self) -> List['MockTempMail.MessageInfo']:
        return self._inbox

    def wait_for_message(self, timeout: Optional[int] = 60,
                         filter: Callable[['MockTempMail.Message'], bool] = lambda _: True) -> 'MockTempMail.Message':
        timeout_time = time.time() + timeout if timeout is not None else None
        while timeout is None or time.time() < timeout_time:
            for msg_info in self._inbox:
                if filter(msg_info.message):
                    return msg_info.message
            time.sleep(1)
        raise TimeoutError('Timed out waiting for message')

    def receive_message(self, from_addr: str, subject: str, body: str):
        self._message_id += 1
        msg = self.Message(
            id=self._message_id,
            from_addr=from_addr,
            subject=subject,
            date_str=datetime.now().isoformat(),
            body=body,
            message=self
        )
        msg_info = self.MessageInfo(
            id=self._message_id,
            from_addr=from_addr,
            subject=subject,
            date_str=datetime.now().isoformat(),
            message=msg
        )
        self._inbox.append(msg_info)

    @dataclass
    class MessageInfo:
        id: int
        from_addr: str
        subject: str
        date_str: str
        message: 'MockTempMail.Message'

    @dataclass
    class Message:
        id: int
        from_addr: str
        subject: str
        date_str: str
        body: str
        message: 'MockTempMail'
