from license_manager import LicenseManager
from automation import move_mouse
import time

def main():
    email = input("Enter your email: ")
    lm = LicenseManager()

    if lm.check_license(email):
        print("License active. Starting full version...")
        move_mouse()
    elif lm.check_trial(email):
        print("Trial active. Starting trial version...")
        move_mouse()
    else:
        start_trial = input("Trial expired. Start a new trial? (y/n): ")
        if start_trial.lower() == 'y':
            lm.start_trial(email)
            move_mouse()
        else:
            license_key = input("Enter license key to activate: ")
            lm.activate_license(license_key, email)

if __name__ == "__main__":
    main()
