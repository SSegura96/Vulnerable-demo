import re

txt = "https://www.google.com"
pattern = "^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"
x = re.search(pattern, txt)
if (x):
    print("Valid email")
else:
    print("Invalid email")