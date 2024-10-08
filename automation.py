import pyautogui
import time
import keyboard
import random
import threading

# Get screen size
screen_width, screen_height = pyautogui.size()

# List of common application window titles (can be expanded for more accuracy)
browsers = ['chrome', 'firefox', 'edge', 'brave', 'opera']
editors = ['code', 'sublime', 'notepad', 'pycharm', 'atom']

# Flags to control automation
automation_running = False
stop_automation = False

# Function to simulate mouse movement, screen change, and app/tab switching
def automate_mouse_and_switch_apps():
    global automation_running, stop_automation

    while not stop_automation:
        if automation_running:
            # Generate random positions across the whole screen
            random_x = random.randint(0, screen_width - 1)
            random_y = random.randint(0, screen_height - 1)

            # Move mouse to a random position on the screen
            pyautogui.moveTo(random_x, random_y, duration=1)

            # Simulate screen change by moving mouse to far left or far right (change screens)
            if random.choice([True, False]):  # Randomly decide to change screens
                if random.choice([True, False]):
                    pyautogui.moveTo(0, random_y, duration=1)  # Move to far left (change to left screen)
                else:
                    pyautogui.moveTo(screen_width - 1, random_y, duration=1)  # Move to far right (change to right screen)

            # Simulate switching between all open applications using Alt+Tab multiple times
            if random.choice([True, False]):  # Randomly decide to switch applications
                num_tabs = random.randint(1, 5)  # Random number of Tab presses (adjust range as needed)

                # Hold Alt and press Tab multiple times
                pyautogui.keyDown('alt')
                for _ in range(num_tabs):
                    pyautogui.press('tab')
                    time.sleep(0.2)  # Short delay between Tab presses
                pyautogui.keyUp('alt')  # Release Alt key

                print(f"Switched through {num_tabs} applications using Alt+Tab")

                # Simulate browser or editor tab switching
                if random.choice([True, False]):  # Randomly decide to change browser or editor tabs
                    current_app = random.choice(browsers + editors)  # Simulate switching between browsers or editors

                    if current_app in browsers:
                        print("Switching browser tabs...")
                        # Randomly choose to switch forward or backward in tabs
                        if random.choice([True, False]):
                            pyautogui.hotkey('ctrl', 'tab')  # Switch to the next browser tab
                        else:
                            pyautogui.hotkey('ctrl', 'shift', 'tab')  # Switch to the previous browser tab
                        print("Switched browser tabs")

                    elif current_app in editors:
                        print("Switching editor tabs...")
                        # Randomly choose to switch forward or backward in editor tabs
                        if random.choice([True, False]):
                            pyautogui.hotkey('ctrl', 'tab')  # Switch to the next editor tab
                        else:
                            pyautogui.hotkey('ctrl', 'shift', 'tab')  # Switch to the previous editor tab
                        print("Switched editor tabs")

            # Sleep for 2 seconds before the next movement or screen switch
            time.sleep(2)

# Function to start the automation
def start_automation():
    global automation_running, stop_automation
    if not automation_running:
        print("Starting automation...")
        automation_running = True
        stop_automation = False
        threading.Thread(target=automate_mouse_and_switch_apps).start()

# Function to stop the automation
def stop_automation_func():
    global automation_running, stop_automation
    print("Stopping automation...")
    automation_running = False
    stop_automation = True

# Function to listen for start/stop shortcuts
def listen_for_shortcuts():
    # Start on Alt+R
    keyboard.add_hotkey('alt+r', start_automation)
    # Stop on Alt+S
    keyboard.add_hotkey('alt+s', stop_automation_func)

    # Keep the script running to listen for shortcuts
    keyboard.wait()

if __name__ == "__main__":
    print("Listening for shortcuts... Press 'Alt+R' to start and 'Alt+S' to stop automation.")
    listen_for_shortcuts()
