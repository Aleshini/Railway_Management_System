# Railway_Management_System

## Overview

The "Railway Reservation System" is a terminal-based application developed in Python that simulates a simple railway ticket booking system. It allows users to check seat availability, book tickets, cancel bookings, and manage user accounts through a signup and login system. The program handles various operations such as ticket price calculation, seat allocation, and ticket cancellation, while ensuring data persistence through file handling.

## Features
- **User Account Management:** Users can sign up and log in to their accounts.
    User data is securely stored and retrieved from a text file.
- **Seat Availability Check:** Users can check the number of available seats before booking.
- **Ticket Booking:** Users can book tickets by selecting the number of seats and the preferred coach type.
    Available coach types include Standard, First Class, and Executive, each with different pricing.
- **Ticket Cancellation:** Users can cancel previously booked tickets using their unique ticket ID.
- **Data Persistence:** User details, booking information, and ticket IDs are stored in text files, ensuring data is saved between sessions.

## Getting Started

To run the Railway Reservation System on your local machine, follow these steps:

1.Clone this repository to your local machine:
```bash
git clone https://github.com/YourUsername/Railway_Reservation_System.git
```
2.Navigate to the project directory:

```bash
cd Railway_Reservation_System
```
3.Run the program:

```bash
python railway_reservation.py
```
## Usage
User Signup and Login:

New users can sign up by providing their username, password, and personal details.
Existing users can log in using their credentials.
Main Menu Options:

1.Check Seat Availability: Displays the number of seats available for booking.

2.Book Ticket: Allows users to book tickets by entering the number of tickets, customer details, and selecting the coach type.

3.Cancel Ticket: Users can cancel a booking by providing the ticket ID.

4.Logout: Logs out the current user and returns to the login/signup menu.

5.Exit: Exits the system.

File Paths:

   1.user_data.txt: Stores user account information.
   
   2.customer_details.txt: Logs details of booked tickets.
   
   3.ticket_id.txt: Tracks the last used ticket ID to ensure unique ticket generation.

## Contributing
If you'd like to contribute to this project, please fork the repository, make your changes, and create a pull request with a detailed description of your contributions.

## Acknowledgments
The Railway Reservation System was created by Shalini Juyal to provide a basic understanding of file handling, user authentication, and data persistence in Python.
