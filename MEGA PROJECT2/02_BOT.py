import pyautogui
import time
import pyperclip  # Make sure to install this module using pip if you haven't already
from openai import OpenAI



client = OpenAI(
    api_key="your_api_key"
)



def is_last_message_from_sender(chatlog,sender_name="mom"):
    #split chatlog into individual message 
    messages= chatlog.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    else:
        return False
     
pyautogui.click(1320, 1050)    # Adjust AMOUNT  ACCORDING TO YOU
time.sleep(1)

while True:

    # Step 2: Drag to select text
    time.sleep(0.5)  # Wait for any UI delay after clicking
    pyautogui.moveTo(720, 310 ) # Adjust AMOUNT ACCORDING TO YOU 
    pyautogui.mouseDown()
    pyautogui.moveTo(1103, 894, duration=0.5)  # Adjust duration  AND AMOUNT if needed
    pyautogui.mouseUp()

    # Step 3: Copy selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(701,327)   # Adjust AMOUNT ACCORDING TO YOU
    time.sleep(1)  # Give a moment for copying to finish

    # Step 4: Store clipboard content in a variablez
    text_content = pyperclip.paste()

    # Print the content to verify
    print("Copied Text:", text_content)



    if is_last_message_from_sender(text_content):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a person named kush  who speaks hindi as well as  english .you are from india and you are  a coder . You analyize chat history  and respond like Kush. output should be the next chat response as the Kush "},
                {
                    "role": "user",
                    "content": text_content
                }
            ]
        )

        response= completion.choices[0].message.content
        pyperclip.copy(response)



        # Click at the specified coordinates
        pyautogui.click(1480, 949)  # Adjust AMOUNT  ACCORDING TO YOU
        time.sleep(2)

        # Paste the text (replace 'your text here' with the actual text you want to paste)
        text_to_paste = ''
        pyautogui.write(text_to_paste)

        # Press Enter
        pyautogui.press('enter') 


 