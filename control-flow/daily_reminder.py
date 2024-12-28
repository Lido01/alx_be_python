Task = input("Enter your task: ")
Priority = input("Enter your task's priority (high/medium/low): ").lower()
Time_bound = input("Is it time bound? (yes/no):").lower()

match priority:
    case "high":
        level = "high"
    case "medium":
        level = "medium"
    case "low":
        level = "low"
if time_bound == "yes":
    print(f"Reminder: {Task} is a {level} priority task that requires immediate attention today!" )
else:
    print(f"Note: {Task} is a {level} priority task. Consider completing it when you have free time.")

