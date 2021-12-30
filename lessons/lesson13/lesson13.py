import re

s = "87+65765765     --- fdgfdg54g54gfdgdf%3  HGFHGFfdsfg"
result = re.search(r"\d{,}", s)
print(result)