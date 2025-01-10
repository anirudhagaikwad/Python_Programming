"""
The program offers three options: displaying a specific month's calendar, displaying an entire year's calendar, and exiting the program.
"""
import calendar

def display_month_calendar():
    """Display a specific month's calendar based on user input."""
    year = int(input("Enter the year (e.g., 2024): "))
    month = int(input("Enter the month (1-12): "))
    try:
        print("\n" + calendar.month(year, month))
    except ValueError:
        print("Invalid month or year. Please try again.")

def display_year_calendar():
    """Display the calendar for an entire year based on user input."""
    year = int(input("Enter the year (e.g., 2024): "))
    try:
        print("\n" + calendar.TextCalendar().formatyear(year))
    except ValueError:
        print("Invalid year. Please try again.")

def main_menu():
    """Menu-driven program to display a calendar."""
    while True:
        print("\n--- Calendar Menu ---")
        print("1. Display specific month's calendar")
        print("2. Display specific year's calendar")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                display_month_calendar()
            elif choice == 2:
                display_year_calendar()
            elif choice == 3:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number (1-3).")

# Run the program
main_menu()
