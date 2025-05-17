# Hotel Management System

# List to keep track of booked rooms
booked_rooms = []

# List of all rooms (101 to 105 for simplicity)
rooms = [101, 102, 103, 104, 105]

def show_menu():
    print("------ Welcome to Simple Hotel ------")
    print("1. Show Available Rooms")
    print("2. Book a Room")
    print("3. Show Booked Rooms")
    print("4. Checkout")
    print("5. Exit")

def show_available_rooms():
    print("\nAvailable Rooms:")
    for room in rooms:
        if room not in booked_rooms:
            print("Room", room)
    print()

def book_room():
    show_available_rooms()
    room = int(input("Enter room number you want to book: "))
    if room in rooms and room not in booked_rooms:
        name = input("Enter your name: ")
        booked_rooms.append(room)
        print("Room", room, "booked successfully for", name, "\n")
    else:
        print("Sorry, that room is not available or doesn't exist.\n")

def show_booked_rooms():
    print("\nBooked Rooms:")
    if len(booked_rooms) == 0:
        print("No rooms booked yet.")
    else:
        for room in booked_rooms:
            print("Room", room)
    print()

def checkout():
    room = int(input("Enter room number to checkout: "))
    if room in booked_rooms:
        booked_rooms.remove(room)
        print("Room", room, "is now available.\n")
    else:
        print("That room is not currently booked.\n")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        show_available_rooms()
    elif choice == "2":
        book_room()
    elif choice == "3":
        show_booked_rooms()
    elif choice == "4":
        checkout()
    elif choice == "5":
        print("Thank you for using the hotel system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
