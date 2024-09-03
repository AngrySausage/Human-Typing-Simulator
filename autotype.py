import pyautogui
import time

# Function to simulate typing like a human
def type_like_human(text, interval=0.1):
    for char in text:
        pyautogui.typewrite(char)  # Type each character
        time.sleep(interval)  # Wait between each keystroke

# Read your regular text from the file 'test.txt'
with open("/Users/kitbernsee/Documents/GitHub/Word-History-Bypass/input.txt", "r") as file:
    regular_text = file.read()

# Brief delay to switch to the Word document
print("Switch to the Word document now...")
time.sleep(5)

# Type out the regular text in the Word document
type_like_human(regular_text, interval=0.05)