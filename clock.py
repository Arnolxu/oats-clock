# Oats' Clock implemented in Python
# Import
import datetime

# Calculate seconds passed since midnight
now = datetime.datetime.now()
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
seconds = (now - midnight).seconds

# Calculate hours, minutes and seconds
crhour = str(int(seconds / 4320) + 1)
crmins = str(int((seconds - int(crhour) * 4320) / 216))
crsecs = str(int(seconds - int(crhour) * 4320 - int(crmins) * 216))

# Add 0 so 1:1:1 -> 01:01:001
crhour = '0' * (2 - len(crhour)) + crhour
crmins = '0' * (2 - len(crmins)) + crmins
crsecs = '0' * (3 - len(crsecs)) + crsecs

# Print it
print(crhour + ":" + crmins + ":" + crsecs)
