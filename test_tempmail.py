from tempmail.mailtm_provider import MailTmProvider
import time

email = MailTmProvider()
print("Temporary email address:", email.account["address"])

print("Waiting for new messages. Press Ctrl+C to stop.")

received_ids = set()

try:
    while True:
        try:
            msg = email.wait_for_message(timeout=60)  # Wait up to 60 seconds
            if msg.id not in received_ids:
                print("New message received:")
                print(f"From: {msg.from_addr}")
                print(f"Subject: {msg.subject}")
                content = msg.text if msg.text else msg.html
                print(f"Text: {content}")
                received_ids.add(msg.id)
            else:
                # Suppress duplicate message print to avoid clutter
                pass
        except TimeoutError:
            print("No new messages received within timeout, continuing to wait...")
        time.sleep(5)  # Add delay to avoid hitting rate limits
except KeyboardInterrupt:
    print("\\nStopped waiting for messages.")
except Exception as e:
    print(f"Error while waiting for message: {e}")
