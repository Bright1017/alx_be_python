# daily_reminder.py

# Prompt the user for task details
task = input("Enter the task description: ").strip()
priority = input("Enter the task priority (high, medium, low): ").strip().lower()
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()

# Initialize the base reminder
reminder = f"Your task: '{task}'"

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task} is of high priority"
    case "medium":
        reminder = f"'{task} is of medium priority"
    case "low":
        reminder = f"'{task} is of low priority"
    case _:
        reminder = "has an unknown priority level"

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    print(f"Note: {reminder}. consider completing it when you have free time.")
# Print the customized reminder
print(reminder)