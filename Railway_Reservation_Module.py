# railway_reservation.py

import os

total_seats = 100
available_seats = total_seats
bookings = []
ticket_id_counter = 1  

user_data = "C:\\Users\\hp\\OneDrive\\Desktop\\project\\user_data.txt"
customer_details_file = "C:\\Users\\hp\\OneDrive\\Desktop\\project\\customer_details.txt"
ticket_file = "C:\\Users\\hp\\OneDrive\\Desktop\\project\\ticket_id.txt"

def create_title():
    title = "\033[10B\033[25C\033[1;34m" + "*" * 41 + "\n\033[25C*      Railway Reservation System      **\n\033[25C" + "*" * 41
    return title

def read_user_data():
    users = []
    try:
        with open(user_data, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    values = line.strip().split(",")
                    if len(values) == 6:
                        username, password, name, phone, email, age = values
                        users.append({
                            'username': username,
                            'password': password,
                            'name': name,
                            'phone': phone,
                            'email': email,
                            'age': age
                        })
                    else:
                        print(f"Invalid data in line: {line}")
    except FileNotFoundError:
        pass
    return users

def write_user_data(users):
    with open(user_data, "w") as file:
        for user in users:
            user_line = ",".join([user['username'], user['password'], user['name'], user['phone'], user['email'], user['age']])
            file.write(user_line + '\n')

def read_last_ticket_id():
    try:
        with open(ticket_file, "r") as file:
            last_ticket_id = int(file.read())
            return last_ticket_id
    except FileNotFoundError:
        return 1  

def write_last_ticket_id(ticket_id):
    with open(ticket_file, "w") as file:
        file.write(str(ticket_id))

def get_ticket_price(coach_choice):
    
    if coach_choice == 1:
        return 50  
    elif coach_choice == 2:
        return 100  
    elif coach_choice == 3:
        return 150  
    else:
        print("Invalid coach choice.")
        return 0 


def generate_ticket_id():
    global ticket_id_counter
    ticket_id = ticket_id_counter
    ticket_id_counter += 1
    write_last_ticket_id(ticket_id_counter)
    return ticket_id

def check_seat_availability():
    return available_seats

def calculate_total_price(num_tickets, ticket_price):
    return num_tickets * ticket_price

def book_ticket(num_tickets, available_seats, bookings, customer_details_file):
    try:
        num_tickets = int(input("Enter the number of tickets to book: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if available_seats >= num_tickets:
        ticket_ids = []
        total_price = 0  
        
        for _ in range(num_tickets):
            customer_name = input("Enter customer name: ")
            customer_age = input("Enter customer age: ")
            
            print("\033[1;33mCoach Types:")
            print("\033[1;36m1. Standard")
            print("\033[1;31m2. First Class")
            print("\033[1;35m3. Executive")
            
            coach_choice = int(input("\033[1;32mEnter your choice (1/2/3): "))
            ticket_price = get_ticket_price(coach_choice)  
            
            ticket_id = generate_ticket_id()
            ticket_ids.append(ticket_id)
            available_seats -= 1
            bookings.append({
                'ticket_id': ticket_id,
                'name': customer_name,
                'age': customer_age,
                'num_tickets': 1,
                'coach_type': coach_choice  
            })
            
            with open(customer_details_file, "a") as customer_file:
                line = f"Ticket ID: {ticket_id}, Name: {customer_name}, Age: {customer_age}, Coach Type: {coach_choice}\n"
                customer_file.write(line)
            
            total_price += ticket_price  
        
        ticket_ids_str = ', '.join(str(ticket_id) for ticket_id in ticket_ids)
        
        print(f"Tickets booked successfully! Your ticket ID(s): {ticket_ids_str}")
        return total_price
    else:
        print("Sorry, only", available_seats, "tickets available.")
    
def cancel_ticket(ticket_id, available_seats, bookings):
    updated_bookings = [booking for booking in bookings if booking['ticket_id'] != ticket_id]
    canceled_tickets = len(bookings) - len(updated_bookings)
    available_seats += canceled_tickets
    if canceled_tickets > 0:
        bookings[:] = updated_bookings
        return f"{canceled_tickets} ticket(s) canceled."
    return "Invalid cancellation request."

def signup(username, password, name, phone, email, age, users):
    users.append({
        'username': username,
        'password': password,
        'name': name,
        'phone': phone,
        'email': email,
        'age': age
    })
    write_user_data(users)
    print("Signup successful.")

def login(username, password, users):
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Login successful.")
            return user
    print("Invalid username or password.")
    return None


def signup_form(users):
    print("\n\033[1;32mSignup Form")
    username = input("\033[1;36mEnter a username: ")
    password = input("\033[1;33mEnter a password: ")
    name = input("\033[1;35mEnter your name: ")
    phone = input("\033[1;34mEnter your phone number: ")
    email = input("\033[1;31mEnter your email: ")
    age = input("\033[1;32mEnter your age: ")
    signup(username, password, name, phone, email, age, users)

def login_form(users):
    print("\n\033[1;33mLogin Form")
    username = input("\033[1;36mEnter your username: ")
    password = input("\033[1;33mEnter your password : ")
    return login(username, password, users)

def display_title():
    title = create_title()
    print(title)
    input("\nPress Enter to continue...\033[0m")
    clear_screen()

def signup_and_login(users):
    while True:
        print("\033[5B\033[10C\033[3;95m1. Signup")
        print("\033[3B\033[10C\033[3;36m2. Login")
        print("\033[3B\033[10C\033[3;91m3. Exit")

        choice = input("\033[3B\033[4;31mEnter your choice: ")

        if choice == "1":
            clear_screen()
            signup_form(users)
            clear_screen()
        elif choice == "2":
            clear_screen()
            if login_form(users):
                break
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

def railway_menu(users):
    while True:
        input("\033[1;34m\nPress Enter to continue...")
        clear_screen()
        print("\nRailway Reservation System")
        print("1. Check Seat Availability")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Logout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            available_seats = check_seat_availability()
            print("Available seats:", available_seats)
        elif choice == "2":
            num_tickets = int(input("Enter the number of tickets to book: "))
            total_price = book_ticket(num_tickets, available_seats, bookings, customer_details_file)
            print("Total Price: $", total_price) 
        elif choice == "3":
            ticket_id = int(input("Enter the ticket ID to cancel: "))
            result = cancel_ticket(ticket_id, available_seats, bookings)
            print(result)
        elif choice == "4":
            print("Logging out. Goodbye!")
            input("\033[1;34m\nPress Enter to continue...")
            clear_screen()
            signup_and_login(users)
            break
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
