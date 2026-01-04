# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for priority with validation
priority = input("Priority (high/medium/low): ").lower()
while priority not in ("high", "medium", "low"):
    priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Output the reminder
print(message)
