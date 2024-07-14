import re

# Validate date
date_pattern = "[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}"
match = re.match(date_pattern, '24-28-2022')  # Returns Match object
print(match)
if match:
    print("yes")
else:
    print("no")

# Extract date from a string
date_extract_pattern = "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
re.findall(date_extract_pattern, 'I\'m on vacation from 1/18/2021 till 1/29/2021')  # returns ['1/18/2021', '1/29/2021']
