import os
import pyautogui
import time

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to 'input.txt'
file_path = os.path.join(current_dir, "input.txt")

# Function to simulate typing like a human
def type_like_human(text, interval=0.1):
    for char in text:
        pyautogui.typewrite(char)  # Type each character
        time.sleep(interval)  # Wait between each keystroke

# Read your regular text from the file 'input.txt'
with open(file_path, "r") as file:
    regular_text = file.read()

# Brief delay to switch to the Word document
print("Switch to the Word document now...")
time.sleep(5)

# Type out the regular text in the Word document
type_like_human(regular_text, interval=0.05)