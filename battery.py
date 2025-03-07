import psutil
from win10toast import ToastNotifier

# Get battery information
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

# Debugging prints
print(f"Battery Percentage: {percent}%")
print(f"Charger Plugged In: {plugged}")

# Check if battery is low and not charging
if percent <= 30 and not plugged:
    print("Battery is low! Sending notification...")  # Debugging print
    toaster = ToastNotifier()
    toaster.show_toast("Battery Low", f"{percent}% Battery remaining!", duration=5)
else:
    print("Battery is sufficient or charging. No notification needed.")

