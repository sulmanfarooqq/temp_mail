# TempMail GUI Application

A desktop GUI application for temporary email addresses using the tempmail-python library.

## Features

- One-click temporary email generation
- Real-time email monitoring
- Easy-to-use graphical interface
- Copy email address to clipboard
- View email content in a readable format
- Refresh inbox manually
- Generate new email addresses

## Installation

1. Make sure you have Python 3.7+ installed on your system
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Method 1: Desktop Shortcut (Recommended)
1. Run `create_shortcut.py` to create a desktop shortcut
2. Double-click the "TempMail" icon on your desktop to start the application

### Method 2: Batch File
1. Navigate to the `gui` directory
2. Double-click on `start_tempmail.bat`

### Method 3: Python Script
1. Navigate to the `gui` directory
2. Run `python tempmail_gui.py`

## How to Use

1. When you start the application, a temporary email address is automatically generated
2. Click "Copy" to copy the email address to your clipboard
3. Click "Start Listening" to begin monitoring for new emails
4. When emails arrive, they will appear in the messages list
5. Click on any message to view its content
6. Click "Refresh Inbox" to manually check for emails
7. Click "New Email" to generate a new temporary email address

## Dependencies

- Python 3.7+
- requests
- pyperclip

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.