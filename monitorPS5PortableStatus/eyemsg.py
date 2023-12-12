import os

def send_imessage(contact: str, message: str):
    applescript_command = f'''
    tell application "Messages"
        send "{message}" to buddy "{contact}" of (service 1 whose service type is iMessage)
    end tell
    '''
    os.system(f"osascript -e '{applescript_command}'")
