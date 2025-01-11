from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date and time in a readable format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
def calculate_future_date(days):
    # Get the current date and time
    current_date = datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days)

    # Format the future date in a readable format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)
# Call the function to display the current date and time
display_current_datetime()
# Prompt the user to enter the number of days
number_of_days = int(input("Enter the number of days to add to the current date: "))
# Call the function to calculate and display the future date
calculate_future_date(number_of_days)
