# TempMail GUI Application

A desktop GUI application for temporary email addresses.

## Quick Start

1. Run `setup_gui.bat` from the main folder to install dependencies and create a desktop shortcut
2. Double-click the "TempMail" icon on your desktop to start the application

## Features

- One-click temporary email generation
- Real-time email monitoring
- Copy email address to clipboard
- View email content in a readable format
- Refresh inbox manually
- Generate new email addresses

## Manual Installation

If you prefer to install manually:

1. Install required dependencies:
   ```
   pip install -r ../requirements.txt
   ```

2. Create desktop shortcut:
   ```
   python create_shortcut.py
   ```

## Usage

1. Double-click the "TempMail" icon on your desktop
2. The application automatically generates a temporary email address
3. Click "Copy" to copy the address to your clipboard
4. Click "Start Listening" to monitor for incoming emails
5. Received emails appear in the messages list
6. Click on any message to view its content

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.