# Python Temp Email Library

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads)

**tempmail-python** is a Python library for generating and managing temporary email addresses using temporary email services. It provides functions for creating email addresses, checking for new messages, and retrieving message contents.

## Features

- Generate temporary email addresses
- Monitor inbox for new messages
- Retrieve message contents
- Desktop GUI application for easy use

## Installation

Make sure you have Python 3.7+ installed on your system.

## Usage

### Quick Start (GUI Application)

1. **One-click setup**:
   - Double-click `setup_gui.bat` to install dependencies and create a desktop shortcut

2. **Run the application**:
   - Double-click the "TempMail" icon on your desktop to start the application

### Command Line Usage

```python
from tempmail import EMail

email = EMail()
print(email.address)  # e.g. abc123@1secmail.com

# Wait for a message
msg = email.wait_for_message()
print(msg.text_body)  # Email body text
```

## GUI Application Features

- One-click temporary email generation
- Real-time email monitoring
- Easy-to-use graphical interface
- Copy email address to clipboard
- View email content in a readable format
- Refresh inbox manually
- Generate new email addresses

## How to Use the GUI

1. When you start the application, a temporary email address is automatically generated
2. Click "Copy" to copy the email address to your clipboard
3. Click "Start Listening" to begin monitoring for new emails
4. When emails arrive, they will appear in the messages list
5. Click on any message to view its content
6. Click "Refresh Inbox" to manually check for emails
7. Click "New Email" to generate a new temporary email address

## Project Structure

- `tempmail/` - Main library code
- `gui/` - Desktop GUI application
- `requirements.txt` - Python dependencies
- `setup_gui.bat` - Automated setup script

## Dependencies

- Python 3.7+
- requests
- pyperclip

## License

tempmail-python is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.