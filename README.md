# Python Temp Email Library

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads)

**tempmail-python** is a Python library for generating and managing temporary email addresses using temporary email services. It provides functions for creating email addresses, checking for new messages, and retrieving message contents.

## Features

- Generate temporary email addresses
- Monitor inbox for new messages
- Retrieve message contents
- Desktop GUI application for easy use
- Supports multiple email providers (1secmail, Mail.tm)

## Project Structure

```
tempmail-python-main/
├── gui/
│   ├── __init__.py              # Makes gui a Python package
│   ├── create_shortcut.py       # Creates desktop shortcut
│   ├── README.md                # GUI-specific documentation
│   ├── run_gui.py               # Launcher script for GUI
│   ├── start_tempmail.bat       # Windows batch file to start GUI
│   └── tempmail_gui.py          # Main GUI application
├── tempmail/
│   ├── __init__.py              # Library entry point
│   ├── mailtm_provider.py       # Mail.tm email provider
│   ├── mock_provider.py         # Mock provider for testing
│   ├── providers.py             # 1secmail email provider
│   └── utils.py                 # Utility functions
├── .gitignore                   # Git ignore patterns
├── LICENSE                      # MIT License
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── setup_gui.bat                # Automated setup script
└── setup.py                     # Package setup
```

## Installation

1. **Prerequisites**:
   - Python 3.7+ installed and added to your PATH
   - Internet connection

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Quick Start (GUI Application)

1. **One-click setup**:
   - Double-click `setup_gui.bat` to install dependencies and create a desktop shortcut

2. **Run the application**:
   - Double-click the "TempMail" icon on your desktop to start the application

### Command Line Usage

```python
# Using 1secmail provider (default)
from tempmail import EMail

email = EMail()
print(email.address)  # e.g. abc123@1secmail.com

# Wait for a message
msg = email.wait_for_message()
print(msg.text_body)  # Email body text

# Using Mail.tm provider (often more reliable)
from tempmail.mailtm_provider import MailTmProvider

email = MailTmProvider()
print(email.account["address"])  # e.g. xyz789@domain.com

msg = email.wait_for_message()
print(msg.text)  # Email body text
```

## GUI Application Features

- **One-click temporary email generation**: Automatically creates a new temporary email on startup
- **Real-time email monitoring**: Continuously checks for new emails
- **Easy-to-use graphical interface**: Clean and intuitive interface
- **Copy email address**: One-click copy to clipboard
- **View email content**: Read email content in a readable format
- **Refresh inbox**: Manually check for emails
- **Generate new email**: Create a new temporary email address

## How to Use the GUI

1. **Start the application**:
   - Double-click the "TempMail" icon on your desktop
   - Or run `start_tempmail.bat` in the `gui` folder

2. **Using the email address**:
   - The application automatically generates a temporary email address
   - Click "Copy" to copy the address to your clipboard
   - Use this address to receive emails

3. **Monitoring emails**:
   - Click "Start Listening" to begin monitoring for new emails
   - When emails arrive, they will appear in the messages list
   - Click on any message to view its content in the bottom panel

4. **Other functions**:
   - "Refresh Inbox": Manually check for emails
   - "New Email": Generate a new temporary email address
   - "Stop Listening": Stop monitoring for new emails

## API Keys and Services

This library uses free temporary email services that do not require API keys:

- **1secmail**: Default provider (1secmail.com, 1secmail.net, etc.)
- **Mail.tm**: Alternative provider (mail.tm)

These services are free to use and do not require registration or API keys. The library communicates directly with their public APIs.

## Creating a Desktop Icon

### Method 1: Automated Setup (Recommended)
1. Double-click `setup_gui.bat`
2. The script will automatically:
   - Install required dependencies
   - Create a desktop shortcut named "TempMail"

### Method 2: Manual Setup
1. Navigate to the `gui` directory
2. Run `python create_shortcut.py`
3. This will create a "TempMail" icon on your desktop

## Troubleshooting

### Common Issues

1. **"Module not found" errors**:
   - Make sure you've run `pip install -r requirements.txt`
   - Ensure Python is added to your PATH

2. **Emails not arriving**:
   - Some email providers block sending to temporary email services
   - Try using the Mail.tm provider (often more reliable)
   - Delivery times can vary from immediate to several minutes

3. **GUI not starting**:
   - Run `setup_gui.bat` to ensure all dependencies are installed
   - Check that Python is properly installed and in your PATH

### Testing Email Reception

To test if the service is working:
1. Run the GUI application
2. Copy the generated email address
3. Visit a website that sends verification emails (like a sign-up page)
4. Use the temporary email address there
5. Check if you receive the verification email in the GUI

## Dependencies

- Python 3.7+
- requests >= 2.19.0
- pyperclip >= 1.8.0

## License

tempmail-python is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.