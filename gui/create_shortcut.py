import os
import sys
import ctypes
from ctypes import wintypes
import subprocess

def create_desktop_shortcut():
    """Create a desktop shortcut for the tempmail application"""
    try:
        # Get paths
        script_dir = os.path.dirname(os.path.abspath(__file__))
        bat_file = os.path.join(script_dir, "start_tempmail.bat")
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        shortcut_path = os.path.join(desktop, "TempMail.lnk")
        
        # Check if batch file exists
        if not os.path.exists(bat_file):
            print(f"Error: Batch file not found at {bat_file}")
            return False
        
        # Create shortcut using Windows COM interface
        # This is a simplified approach using a VBScript
        vbs_script = f'''
Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "{shortcut_path}"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{bat_file}"
oLink.WorkingDirectory = "{script_dir}"
oLink.IconLocation = "shell32.dll,1"
oLink.Save
'''
        
        # Write and execute VBScript
        vbs_file = os.path.join(script_dir, "create_shortcut.vbs")
        with open(vbs_file, "w") as f:
            f.write(vbs_script)
        
        # Execute the VBScript
        subprocess.run(["cscript.exe", "//nologo", vbs_file], check=True)
        
        # Clean up
        os.remove(vbs_file)
        
        print(f"Desktop shortcut created successfully at {shortcut_path}")
        return True
    except Exception as e:
        print(f"Failed to create desktop shortcut: {e}")
        return False

if __name__ == "__main__":
    if create_desktop_shortcut():
        print("You can now double-click the 'TempMail' icon on your desktop to start the application.")
    else:
        print("Failed to create desktop shortcut. You can still run the application by double-clicking 'start_tempmail.bat' in the gui folder.")
    
    input("Press Enter to exit...")