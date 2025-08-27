import sys
import os
import subprocess

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the GUI script
    gui_script = os.path.join(script_dir, "tempmail_gui.py")
    
    # Check if the GUI script exists
    if not os.path.exists(gui_script):
        print(f"Error: GUI script not found at {gui_script}")
        input("Press Enter to exit...")
        return
    
    # Try to run the GUI script
    try:
        subprocess.run([sys.executable, gui_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running the GUI application: {e}")
        input("Press Enter to exit...")
    except FileNotFoundError:
        print("Error: Python interpreter not found")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()