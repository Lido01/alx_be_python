task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time bound? (yes/no): ").lower()
match priority:
    case "high":
        level = "high"
        if time_bound == "yes":
            print(f"Reminder: { task} is a {level} priority task that requires immediate attention today!" )
        else:
            print(f"Note: { task} is a {level} priority task. Consider completing it when you have free time.")
    case "medium":
        level = "medium"
        if time_bound == "yes":
            print(f"Reminder: { task} is a {level} priority task that requires immediate attention today!" )
        else:
             print(f"Note: { task} is a {level} priority task. Consider completing it when you have free time.")
    case "low":
        level = "low"
        if time_bound == "yes":
            print(f"Reminder: { task} is a {level} priority task that requires immediate attention today!" )
        else:
            print(f"Note: { task} is a {level} priority task. Consider completing it when you have free time.") 
 