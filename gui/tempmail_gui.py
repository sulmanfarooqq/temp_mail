import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
from datetime import datetime
import pyperclip

from tempmail import EMail


class TempMailGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TempMail - Temporary Email")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize email provider
        self.email_provider = None
        self.email_address = ""
        self.is_listening = False
        self.listener_thread = None
        self.received_messages = []
        
        # Create UI
        self.create_widgets()
        
        # Initialize email on startup
        self.initialize_email()
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Email address frame
        email_frame = ttk.LabelFrame(main_frame, text="Email Address", padding="10")
        email_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        email_frame.columnconfigure(0, weight=1)
        
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(email_frame, textvariable=self.email_var, width=50, state="readonly")
        self.email_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        self.copy_btn = ttk.Button(email_frame, text="Copy", command=self.copy_email)
        self.copy_btn.grid(row=0, column=1, padx=(5, 0))
        
        # Controls frame
        controls_frame = ttk.Frame(main_frame)
        controls_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.start_btn = ttk.Button(controls_frame, text="Start Listening", command=self.toggle_listening)
        self.start_btn.grid(row=0, column=0, padx=(0, 5))
        
        self.refresh_btn = ttk.Button(controls_frame, text="Refresh Inbox", command=self.refresh_inbox)
        self.refresh_btn.grid(row=0, column=1, padx=(5, 5))
        
        self.new_email_btn = ttk.Button(controls_frame, text="New Email", command=self.new_email)
        self.new_email_btn.grid(row=0, column=2, padx=(5, 0))
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(main_frame, textvariable=self.status_var)
        self.status_label.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        # Messages list
        messages_frame = ttk.LabelFrame(main_frame, text="Messages", padding="10")
        messages_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        messages_frame.columnconfigure(0, weight=1)
        messages_frame.rowconfigure(0, weight=1)
        
        # Create Treeview for messages
        columns = ("from", "subject", "date")
        self.messages_tree = ttk.Treeview(messages_frame, columns=columns, show="headings", height=8)
        self.messages_tree.heading("from", text="From")
        self.messages_tree.heading("subject", text="Subject")
        self.messages_tree.heading("date", text="Date")
        self.messages_tree.column("from", width=150)
        self.messages_tree.column("subject", width=300)
        self.messages_tree.column("date", width=120)
        
        # Scrollbar for messages
        messages_scrollbar = ttk.Scrollbar(messages_frame, orient=tk.VERTICAL, command=self.messages_tree.yview)
        self.messages_tree.configure(yscrollcommand=messages_scrollbar.set)
        
        self.messages_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        messages_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Bind selection event
        self.messages_tree.bind("<<TreeviewSelect>>", self.on_message_select)
        
        # Message content
        content_frame = ttk.LabelFrame(main_frame, text="Message Content", padding="10")
        content_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        content_frame.columnconfigure(0, weight=1)
        content_frame.rowconfigure(0, weight=1)
        
        self.message_text = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=70, height=10)
        self.message_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure row weights for resizing
        main_frame.rowconfigure(3, weight=1)
        main_frame.rowconfigure(4, weight=2)
    
    def initialize_email(self):
        """Initialize the email provider and create a new email address"""
        try:
            self.status_var.set("Creating email address...")
            self.root.update_idletasks()
            
            # Using 1secmail provider (default) for better compatibility
            self.email_provider = EMail()
            self.email_address = self.email_provider.address
            self.email_var.set(self.email_address)
            
            self.status_var.set(f"Email created: {self.email_address}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create email address: {str(e)}")
            self.status_var.set("Failed to create email")
    
    def copy_email(self):
        """Copy email address to clipboard"""
        try:
            pyperclip.copy(self.email_address)
            self.status_var.set("Email address copied to clipboard")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}")
    
    def toggle_listening(self):
        """Toggle message listening on/off"""
        if not self.is_listening:
            self.start_listening()
        else:
            self.stop_listening()
    
    def start_listening(self):
        """Start listening for new messages"""
        if not self.is_listening:
            self.is_listening = True
            self.start_btn.config(text="Stop Listening")
            self.status_var.set("Listening for new messages...")
            
            # Start listener in a separate thread
            self.listener_thread = threading.Thread(target=self.listen_for_messages, daemon=True)
            self.listener_thread.start()
    
    def stop_listening(self):
        """Stop listening for new messages"""
        self.is_listening = False
        self.start_btn.config(text="Start Listening")
        self.status_var.set("Stopped listening")
    
    def listen_for_messages(self):
        """Listen for new messages in a separate thread"""
        received_ids = set()
        
        try:
            while self.is_listening:
                try:
                    # Wait for a message with a timeout
                    msg = self.email_provider.wait_for_message(timeout=30)
                    if msg.id not in received_ids:
                        # Add to received messages
                        received_ids.add(msg.id)
                        self.received_messages.append(msg)
                        
                        # Update UI in main thread
                        self.root.after(0, self.add_message_to_ui, msg)
                        
                        self.root.after(0, lambda: self.status_var.set(
                            f"New message received from {msg.from_addr}"))
                except TimeoutError:
                    # Timeout is expected, just continue listening
                    pass
                except Exception as e:
                    if self.is_listening:  # Only show error if we're still supposed to be listening
                        self.root.after(0, lambda e=e: messagebox.showerror(
                            "Error", f"Error while waiting for message: {str(e)}"))
                    break
        except Exception as e:
            self.root.after(0, lambda e=e: messagebox.showerror(
                "Error", f"Error in listener thread: {str(e)}"))
    
    def refresh_inbox(self):
        """Manually refresh the inbox"""
        try:
            self.status_var.set("Refreshing inbox...")
            self.root.update_idletasks()
            
            # Get all messages
            inbox = self.email_provider.get_inbox()
            
            # Clear existing messages in UI
            for item in self.messages_tree.get_children():
                self.messages_tree.delete(item)
            
            # Add messages to UI
            self.received_messages = []
            for msg_info in inbox:
                msg = msg_info.message
                self.received_messages.append(msg)
                self.add_message_to_ui(msg)
            
            self.status_var.set(f"Inbox refreshed. {len(inbox)} messages found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh inbox: {str(e)}")
            self.status_var.set("Failed to refresh inbox")
    
    def add_message_to_ui(self, msg):
        """Add a message to the UI"""
        # Format date
        try:
            date_str = msg.date.strftime("%Y-%m-%d %H:%M")
        except:
            date_str = msg.date_str if hasattr(msg, 'date_str') else "Unknown"
        
        # Insert into treeview
        self.messages_tree.insert("", 0, values=(
            msg.from_addr,
            msg.subject,
            date_str
        ), tags=(len(self.received_messages)-1,))
    
    def on_message_select(self, event):
        """Handle message selection"""
        selection = self.messages_tree.selection()
        if selection:
            item = selection[0]
            # Get the tag which corresponds to the message index
            tags = self.messages_tree.item(item, "tags")
            if tags:
                index = int(tags[0])
                if 0 <= index < len(self.received_messages):
                    msg = self.received_messages[index]
                    # Display message content
                    content = msg.text_body if msg.text_body else msg.html_body if msg.html_body else msg.body
                    self.message_text.delete(1.0, tk.END)
                    self.message_text.insert(tk.END, content)
    
    def new_email(self):
        """Create a new email address"""
        if self.is_listening:
            self.stop_listening()
        
        # Clear messages
        for item in self.messages_tree.get_children():
            self.messages_tree.delete(item)
        self.received_messages = []
        self.message_text.delete(1.0, tk.END)
        
        # Create new email
        self.initialize_email()


def main():
    root = tk.Tk()
    app = TempMailGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()