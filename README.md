# Python Temp Email Library

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads)

**tempmail-python** is a Python library for generating and managing temporary email addresses using the mail.tm service. It provides functions for creating email addresses, checking for new messages, and retrieving message contents.

## Getting Started

### Clone the repository

```bash
git clone https://github.com/sulmanfarooqq/temp_mail.git
cd temp_mail
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the test script

```bash
python test_tempmail.py
```

## Installation
You can install tempmail-python using pip:
```bash
pip install tempmail-python
```

Or you can install it from source:
```bash
pip install git+https://github.com/cubicbyte/tempmail-python.git
```

## Examples

Receive a message (e.g. activation code)
```python
from tempmail.mailtm_provider import MailTmProvider

email = MailTmProvider()
print(email.account["address"])  # e.g. abc123@punkproof.com

# ... request some email ...

msg = email.wait_for_message()
print(msg.text)  # Email body text
```

Get all messages in the inbox
```python
from tempmail.mailtm_provider import MailTmProvider

email = MailTmProvider()
inbox = email.get_inbox()

for msg in inbox:
    print(msg.subject, msg.text)
```

Wait for a message with a filter and timeout
```python
from tempmail.mailtm_provider import MailTmProvider

email = MailTmProvider()

def filter_hello_world(msg):
    return msg.subject == 'Hello World!'

msg = email.wait_for_message(timeout=60, filter=filter_hello_world)
print(msg.text)
```

## License
tempmail-python is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
Contribution: 2025-06-11 00:00

