import sys
import os

# Add the parent directory to the Python path
parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, parent_dir)

def main():
    try:
        # Import and run the GUI
        from gui.tempmail_gui import main as gui_main
        gui_main()
    except ImportError as e:
        print(f"Error importing GUI: {e}")
        print("Make sure all dependencies are installed.")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"Error running the GUI application: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()