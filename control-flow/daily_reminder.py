# daily_reminder.py

# Prompt the user for task details
task = input("Enter the task description: ").strip()
priority = input("Enter the task priority (high, medium, low): ").strip().lower()
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"Your task: '{task}' is of high priority"
    case "medium":
        reminder = f"Your task: '{task}' is of medium priority"
    case "low":
        reminder = f"Your task: '{task}' is of low priority"
    case _:
        reminder = f"Your task: '{task}' has an unknown priority level"

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print(reminder)

