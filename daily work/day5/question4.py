  
import datetime

now = datetime.datetime.now()

print("Current date and time:", now)

print("Day of the week:", now.strftime("%A"))

print("Formatted date:", now.strftime("%d-%m-%Y"))
print("Formatted time:", now.strftime("%I:%M %p"))