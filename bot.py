import pyautogui
import time
import pyperclip  # Make sure you have pyperclip installed for clipboard handling

# function
def perform_actions():
    # Click on the icon at (860, 737)
    pyautogui.click(x=393, y=53)
    time.sleep(1)  # Wait for the UI to update or for any animations to complete
    
    # Click and drag to select the text from (795, 354) to (1225, 690)
    pyautogui.mouseDown(x=319, y=103)
    pyautogui.moveTo(x=719, y=440, duration=1)  # Adjust duration for the drag speed
    pyautogui.mouseUp()
    
    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    # pyautogui.click(1253,573)
    time.sleep(1)  # Wait for the clipboard operation to complete
    
    # Retrieve the text from the clipboard
    copied_text = pyperclip.paste()

     # Click at (242, 222)
    pyautogui.click(x=927, y=741)
    time.sleep(1)  # Wait for the target field to be active
    
    # Paste the copied text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Wait for the paste operation to complete
    
    # Press Enter
    pyautogui.press('enter')
    
    return copied_text

# Execute the function and print the result
text = perform_actions()
print("Copied text:", text)
