# main.py

import Railway_reservation as rail

def run_railway_reservation_system():
    users = rail.read_user_data()
    rail.display_title()
    rail.signup_and_login(users)
    rail.railway_menu(users)

if __name__ == "__main__":
    run_railway_reservation_system()
