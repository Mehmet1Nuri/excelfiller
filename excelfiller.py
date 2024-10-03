import pyautogui
import keyboard

form_data = {
    "data": [
        {
            "name": "Liam Brown",
            "email": "liam.brown@example.com",
            "phone": "(555) 123-4567"
        },
        {
            "name": "Emma Davis",
            "email": "emma.davis@example.com",
            "phone": "(555) 765-4321"
        },
        {
            "name": "Olivia Wilson",
            "email": "olivia.wilson@example.com",
            "phone": "(555) 246-8101"
        },
        {
            "name": "Noah Johnson",
            "email": "noah.johnson@example.com",
            "phone": "(555) 135-7924"
        },
        {
            "name": "Sophia Martinez",
            "email": "sophia.martinez@example.com",
            "phone": "(555) 987-6543"
        },
        {
            "name": "James Garcia",
            "email": "james.garcia@example.com",
            "phone": "(555) 321-7654"
        },
        {
            "name": "Ava Rodriguez",
            "email": "ava.rodriguez@example.com",
            "phone": "(555) 654-3210"
        },
        {
            "name": "William Hernandez",
            "email": "william.hernandez@example.com",
            "phone": "(555) 456-7890"
        },
        {
            "name": "Isabella Lee",
            "email": "isabella.lee@example.com",
            "phone": "(555) 789-0123"
        },
        {
            "name": "Elijah Walker",
            "email": "elijah.walker@example.com",
            "phone": "(555) 135-2468"
        }
    ]
}
while True:
    if keyboard.is_pressed('esc'):

        for entry in form_data["data"]:
            pyautogui.typewrite(entry["name"])  
            pyautogui.press('right')  
            pyautogui.typewrite(entry["email"])  
            pyautogui.press('right')
            pyautogui.typewrite(entry["phone"])  
            pyautogui.press('down') 
            pyautogui.press('left')
            pyautogui.press('left') 
        break
    if keyboard.is_pressed('esc'):
        break  
