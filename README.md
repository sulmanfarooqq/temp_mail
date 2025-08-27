# Python Temp Email Library

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads)

**tempmail-python** is a Python library for generating and managing temporary email addresses using temporary email services. It provides functions for creating email addresses, checking for new messages, and retrieving message contents.

## Features

- Generate temporary email addresses
- Monitor inbox for new messages
- Retrieve message contents
- Desktop GUI application for easy use

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Command Line

```python
from tempmail import EMail

email = EMail()
print(email.address)  # e.g. abc123@1secmail.com

# Wait for a message
msg = email.wait_for_message()
print(msg.text_body)  # Email body text
```

### GUI Application

For a desktop application with a graphical interface:

1. Navigate to the `gui` directory
2. Run `create_shortcut.py` to create a desktop shortcut (Windows)
3. Double-click the "TempMail" icon on your desktop to start the application

Or run directly:
```bash
cd gui
python tempmail_gui.py
```

## License

tempmail-python is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.